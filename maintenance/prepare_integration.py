"""One-shot, pinned integration preparation. Never pushes or deploys anything."""
import copy
import json
import subprocess
from pathlib import Path

HEADS = {
  1:'2fbb6033b8e8b111b3f00ec977ec92eda82101df',
  4:'29984f64a215c973ac89cb3d3cafba97aff3762c',
  5:'67e52b60fabe5bdc8a74646fe73ad0e59ae2ea1a',
  6:'455f5eb1a17cc36e4a8e7bc1471b3011d82c3eb2',
  10:'dff9065670579ca08e819e4fb7f4668ac44cfae0',
  11:'282404e5cfe53bd568950872b8b9b2f7377e4930',
  12:'e630438a5521a8908c8219e76beabcbb01e6e90a',
  13:'e7be633ee2bce853cc516d62e37330d232b3513c',
  14:'0f8c827832ab680d762983845b42cb60e6367d85',
  15:'e1960db7043ca083bf1456423dcc3a1e2f3c9525',
  16:'79522d540dbe23f87e84e148591d455b39456979',
}
ORDER = [1,4,5,6,10,11,12,13,14,16,15]
ALLOWED_FILES = {'package.json','package-lock.json'}

def git(*args):
    return subprocess.check_output(['git',*args],text=True).strip()

def at(sha,path):
    return json.loads(git('show',f'{sha}:{path}'))

def replace(path, old, new):
    p=Path(path); text=p.read_text()
    if old not in text:
        raise RuntimeError(f'Expected reviewed source fragment missing: {path}')
    p.write_text(text.replace(old,new))

def append(path,text):
    p=Path(path);p.write_text(p.read_text()+text)

lock=json.loads(Path('package-lock.json').read_text())
packages=lock['packages']; touched={}; report=[]
for pr in ORDER:
    ref=f'refs/review/{pr}'
    subprocess.run(['git','fetch','--no-tags','origin',f'refs/pull/{pr}/head:{ref}'],check=True)
    sha=git('rev-parse',ref)
    if sha != HEADS[pr]:
        raise RuntimeError(f'PR {pr} moved since review; stop before integration')
    base=git('merge-base','HEAD',sha)
    changed=set(git('diff','--name-only',base,sha).splitlines())
    if not changed <= ALLOWED_FILES:
        raise RuntimeError(f'Unexpected files in PR {pr}: {changed}')
    before=at(base,'package-lock.json')['packages']; after=at(sha,'package-lock.json')['packages']
    for key in sorted(set(before)|set(after)):
        if before.get(key)==after.get(key):continue
        value=after.get(key)
        if key in touched and packages.get(key)!=value:
            if not (pr==15 and touched[key]==16 and (key=='' or key=='node_modules/next' or key.startswith('node_modules/@next/'))):
                raise RuntimeError(f'Unreviewed overlap at {key} in PR {pr}')
        if value is None:packages.pop(key,None)
        else:packages[key]=copy.deepcopy(value)
        touched[key]=pr
        report.append({'pr':pr,'path':key,'before':before.get(key,{}).get('version'),'after':(value or {}).get('version')})
for key,value in packages.items():
    resolved=value.get('resolved','')
    if resolved and not resolved.startswith('https://registry.npmjs.org/'):
        raise RuntimeError(f'Unreviewed registry origin: {key}')
    if value.get('link'):raise RuntimeError(f'Unexpected link dependency: {key}')
lock['packages']=dict(sorted(packages.items()))
Path('package-lock.json').write_text(json.dumps(lock,indent=2)+'\n')
pkg=at(HEADS[15],'package.json')
pkg['dependencies'].update({'next':'16.3.5','react':'19.2.8','react-dom':'19.2.8'})
pkg['devDependencies']['eslint-config-next']='16.3.5'
pkg['engines']={'node':'>=22.12.0'}
pkg['scripts'].update({'lint':'eslint src eslint.config.mjs next.config.ts postcss.config.mjs --max-warnings=0','typecheck':'tsc --noEmit','test:dependencies':'node --test tests/dependencies.test.cjs'})
Path('package.json').write_text(json.dumps(pkg,indent=2)+'\n')
Path('review-output').mkdir(exist_ok=True)
Path('review-output/dependency-deltas.json').write_text(json.dumps(report,indent=2)+'\n')
Path('review-output/parents.txt').write_text('\n'.join(HEADS.values())+'\n')

replace('campus/assets/state.js','MAX_IMPORT = 200000','MAX_IMPORT = 1024 * 1024')
replace('campus/assets/state.js',"text.length > MAX_IMPORT) throw new Error('Archivo demasiado grande (máximo 200 KB).');", "new TextEncoder().encode(text).byteLength > MAX_IMPORT) throw new Error('Archivo demasiado grande (máximo 1 MiB en UTF-8).');")
append('campus/assets/state.js','''\n/** Reanudar en la primera fase pendiente, o en cierre si ya se confirmaron todas. */
export function nextLabStep(lab) {
  const pending = lab.steps.findIndex(value => !value);
  return pending < 0 ? lab.steps.length - 1 : pending;
}
''')
replace('campus/assets/app.js','MAX_IMPORT, emptyState','MAX_IMPORT, nextLabStep, emptyState')
replace('campus/assets/app.js','if(s===undefined)s=Math.max(0,ls.steps.findIndex(x=>!x));','if(s===undefined)s=nextLabStep(ls);')
replace('campus/assets/app.js','function render(focus=true){','function render(focus=true, remember=true){')
replace('campus/assets/app.js',"state.lastRoute=link(m.id,'/practica/'+l.id)","if(remember)state.lastRoute=link(m.id,'/practica/'+l.id)")
replace('campus/assets/app.js',"state.lastRoute=link(m.id);}persist();}","if(remember)state.lastRoute=link(m.id);}if(remember)persist();}")
replace('campus/assets/app.js','La copia supera 200 KB.','La copia supera 1 MiB en UTF-8.')
replace('campus/assets/app.js','state=incoming;stepMemory.clear();render(false);','state=incoming;stepMemory.clear();render(false,false);')
replace('campus/tests/state.test.mjs','import {emptyState,','import {MAX_IMPORT,nextLabStep,emptyState,')
replace('campus/tests/state.test.mjs',"' '.repeat(200001)","' '.repeat(MAX_IMPORT+1)")
append('campus/tests/state.test.mjs','''\ntest('límite medido en bytes UTF-8, no unidades UTF-16',()=>{assert.throws(()=>parseImport('界'.repeat(Math.floor(MAX_IMPORT/3)+1),course),/1 MiB/);});
test('exportación Unicode de todos los módulos se puede reimportar',()=>{const s=emptyState(course);for(const m of Object.values(s.modules))m.notes='界'.repeat(3000);const text=JSON.stringify(s,null,2);assert.ok(new TextEncoder().encode(text).byteLength>200000);assert.deepEqual(parseImport(text,course),s);});
test('reanudar práctica nueva en preparación',()=>{assert.equal(nextLabStep({steps:[false,false,false,false,false]}),0);});
test('reanudar en primera fase pendiente',()=>{assert.equal(nextLabStep({steps:[true,true,false,false,false]}),2);});
test('práctica terminada reabre en cierre, no en preparación',()=>{assert.equal(nextLabStep({steps:[true,true,true,true,true]}),4);});
''')
replace('campus/tests/browser.py',"if __name__=='__main__':unittest.main(verbosity=2)",'''    def test_21_tabs_do_not_echo_storage_updates(self):
        self.goto('#/modulo/M05')
        other=self.context.new_page()
        other.goto(self.base+'/#/modulo/M06')
        other.locator('#read-check').wait_for()
        self.page.evaluate("window.storageEvents=0; window.addEventListener('storage',()=>window.storageEvents++)")
        other.evaluate("window.storageEvents=0; window.addEventListener('storage',()=>window.storageEvents++)")
        self.page.locator('#read-check').check()
        self.page.wait_for_timeout(500)
        events=self.page.evaluate('window.storageEvents')+other.evaluate('window.storageEvents')
        self.assertLessEqual(events,4,'A storage event must not be written back to other tabs')
        self.assertTrue(other.evaluate('(key)=>JSON.parse(localStorage.getItem(key)).modules.M05.read',KEY))
        self.assertEqual(self.state()['lastRoute'],'#/modulo/M05')
        other.close()
    def test_22_completed_wizard_reopens_at_closure(self):
        self.goto('#/modulo/M05/practica/L05A')
        for _ in range(5):
            self.page.locator('[data-action=step-done]').click()
        self.page.reload()
        self.page.locator('[data-action=step-done]').wait_for()
        self.assertEqual(self.page.locator('[data-action=step][aria-current=step]').get_attribute('data-step'),'4')
    def test_23_unicode_export_can_be_imported(self):
        self.goto('#/modulo/M01')
        state=self.state()
        for module in state['modules'].values():module['notes']='界'*3000
        payload=json.dumps(state,ensure_ascii=False).encode('utf-8')
        self.assertGreater(len(payload),200000)
        self.goto('#/progreso')
        self.page.once('dialog',lambda d:d.accept())
        self.page.locator('#import-file').set_input_files({'name':'unicode-progress.json','mimeType':'application/json','buffer':payload})
        self.page.wait_for_timeout(150)
        self.assertEqual(self.state()['modules']['M32']['notes'],'界'*3000)
if __name__=='__main__':unittest.main(verbosity=2)
''')
cp=Path('campus/package.json');v=json.loads(cp.read_text());v['version']='2.0.1';cp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
replace('campus/build.py',"'version':'2.0.0'","'version':'2.0.1'")
replace('campus/README.md','Versión 2.0.0','Versión 2.0.1')
append('campus/README.md','''\n## Mantenimiento 2.0.1

Se evita reescribir localStorage al recibir un evento de otra pestaña. Una práctica con cinco fases confirmadas se reabre en el cierre. Las copias JSON admiten hasta 1 MiB medido en UTF-8 para permitir recuperar las notas Unicode de todos los módulos. Se conserva el esquema de progreso v1 y su clave.

Las dependencias Next.js de la raíz se validan separadamente; no se incorporan al campus estático. Véase el registro de mantenimiento de septiembre de 2026 en docs/maintenance/.
''')
replace('.github/workflows/campus.yml',"'.github/workflows/campus.yml']", "'.github/workflows/campus.yml', 'package.json', 'package-lock.json']")
p=Path('src/app/layout.tsx');s=p.read_text();s=s.replace('import { Geist, Geist_Mono } from "next/font/google";\n','');a=s.index('const geistSans =');b=s.index('export const metadata',a);s=s[:a]+s[b:];s=s.replace('title: "Create Next App",','title: "Fundamentos de ciberseguridad · Aplicación de referencia",').replace('description: "Generated by create next app",','description: "Aplicación de referencia. El campus estático se compila desde campus/.",').replace('<html lang="en">','<html lang="es">').replace('className={`${geistSans.variable} ${geistMono.variable} antialiased`}','className="antialiased"');p.write_text(s)
p=Path('src/app/globals.css');s=p.read_text().replace('@import "tailwindcss";','@import "tailwindcss";\n@custom-variant dark (&:where(.dark, .dark *));').replace('--foreground: #171717;','--foreground: #171717;\n  --font-geist-sans: Arial, Helvetica, sans-serif;\n  --font-geist-mono: "Courier New", monospace;\n  color-scheme: light;');a=s.index('@media (prefers-color-scheme: dark)');b=s.index('\nbody {',a);p.write_text(s[:a]+s[b:])
print('Prepared 11 pinned PRs and bounded campus fixes. Validation still required.')
