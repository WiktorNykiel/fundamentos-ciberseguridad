"""One-off, hash-guarded source migration. Does not fetch or execute external data."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ALLOWED={'campus/assets/app.js','campus/assets/catalog.js','campus/assets/navigation.js','campus/index.html','campus/build.py','campus/check_release.py','campus/provenance.py','campus/package.json','campus/tests/browser.py','campus/tests/cloudflare_smoke.py'}
changes=json.loads((Path(__file__).parent/'editorial-migration.json').read_text('utf-8'))
if set(changes)!=ALLOWED:raise ValueError('Unexpected migration scope')
outputs={}
for name,item in changes.items():
    path=ROOT/name
    if path.is_symlink() or not path.resolve().is_relative_to(ROOT):raise ValueError('Unsafe input')
    source=path.read_text('utf-8');digest=hashlib.sha256(source.encode()).hexdigest()
    if digest==item['after']:continue
    if digest!=item['before']:raise ValueError('Preimage changed: '+name)
    cursor=0;parts=[]
    for first,last,replacement in item['edits']:
        if not cursor<=first<=last<=len(source):raise ValueError('Invalid patch offsets')
        parts.extend([source[cursor:first],replacement]);cursor=last
    parts.append(source[cursor:]);result=''.join(parts)
    if hashlib.sha256(result.encode()).hexdigest()!=item['after']:raise ValueError('Postimage mismatch: '+name)
    outputs[path]=result
for path,result in outputs.items():path.write_text(result,encoding='utf-8')
# Small reviewed corrections to the newly added independent files.
p=ROOT/'campus/translations.py';s=p.read_text();s=s.replace("'question', 'explanation'}","'question', 'explanation', 'kind'}");p.write_text(s)
p=ROOT/'campus/assets/i18n.js';s=p.read_text().replace('let answer=EN[s];','let answer=Object.hasOwn(EN,s)?EN[s]:undefined;');p.write_text(s)
p=ROOT/'campus/index.html';s=p.read_text().replace('</noscript>','<p lang="en"><a href="reading.html">Open the English reading guide without JavaScript.</a></p></noscript>');p.write_text(s)
print('Applied hash-verified editorial source changes:',len(outputs))
