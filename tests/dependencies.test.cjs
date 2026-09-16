// Bounded offline compatibility checks, resolving actual installed lockfile paths.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {createRequire} = require('node:module');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '..');
const lock = JSON.parse(fs.readFileSync(path.join(root, 'package-lock.json'), 'utf8'));
function installed(name) {
  const suffix = `node_modules/${name}`;
  const paths = Object.keys(lock.packages).filter(p => p === suffix || p.endsWith('/' + suffix))
    .sort((a,b) => a.split('/').length - b.split('/').length || a.localeCompare(b));
  for (const rel of paths) {
    const dir = path.resolve(root, rel);
    if (!dir.startsWith(root + path.sep)) continue;
    const manifest = path.join(dir, 'package.json');
    if (!fs.existsSync(manifest)) continue;
    const pkg = JSON.parse(fs.readFileSync(manifest, 'utf8'));
    if (pkg.name !== name) continue;
    const resolver = createRequire(manifest);
    return {pkg, entry: resolver.resolve(name)};
  }
  throw new Error(`Required compatibility target is not installed: ${name}`);
}
const pkg = name => installed(name).pkg;
const load = name => require(installed(name).entry);
function atLeast(actual, minimum) {
  assert.match(actual, /^\d+\.\d+\.\d+$/, 'Expected a stable semantic version');
  const a=actual.split('.').map(Number), b=minimum.split('.').map(Number);
  for (let i=0;i<3;i++) if(a[i]!==b[i]) return a[i]>b[i];
  return true;
}
test('Next and ESLint configuration remain aligned', () => {
  assert.equal(pkg('next').version,pkg('eslint-config-next').version);
  assert.ok(atLeast(pkg('next').version,'16.3.5'));
});
test('React and React DOM remain aligned', () => {
  assert.equal(pkg('react').version,pkg('react-dom').version);
  assert.ok(atLeast(pkg('react').version,'19.2.8'));
});
test('minimatch handles ordinary paths and alternatives', () => {
  const module=load('minimatch'), m=typeof module==='function'?module:module.minimatch;
  assert.equal(m('notes/course.md','**/*.md'),true);
  assert.equal(m('notes/course.txt','**/*.md'),false);
  assert.equal(m('notes/a.md','notes/{a,b}.md'),true);
});
test('picomatch preserves bounded matches', () => {
  const matches=load('picomatch')('notes/*.md');
  assert.equal(matches('notes/course.md'),true);assert.equal(matches('other/course.md'),false);
});
test('brace expansion is compatible', () => {
  const module=load('brace-expansion'), expand=typeof module==='function'?module:module.default;
  assert.deepEqual(expand('module{1,2}'),['module1','module2']);
});
test('flatted round-trips a small circular object', () => {
  const f=load('flatted'), value={title:'curso'};value.self=value;
  const restored=f.parse(f.stringify(value));assert.equal(restored.self,restored);assert.equal(restored.title,'curso');
});
test('js-yaml preserves ordinary configuration', () => {
  assert.deepEqual(load('js-yaml').load('course: fundamentos\nhours: 480\n'),{course:'fundamentos',hours:480});
});
test('nanoid produces ordinary identifiers', () => {
  const {nanoid}=load('nanoid'), values=new Set(Array.from({length:20},()=>nanoid(21)));
  assert.equal(values.size,20);for(const id of values)assert.equal(id.length,21);
});
test('browserslist resolves a fixed browser query', () => {
  assert.deepEqual(load('browserslist')('chrome 120'),['chrome 120']);
});
test('baseline mapping exposes version data', () => {
  const mapping=load('baseline-browser-mapping');assert.equal(typeof mapping.getAllVersions,'function');assert.ok(mapping.getAllVersions());
});
test('humanfs reads JSON using its installed location', async () => {
  const {hfs}=await import(pathToFileURL(installed('@humanfs/node').entry).href);
  const config=await hfs.json(path.join(root,'package.json'));
  assert.deepEqual(config.dependencies,JSON.parse(fs.readFileSync(path.join(root,'package.json'),'utf8')).dependencies);
});
test('sharp processes an in-memory 8x8 image', async () => {
  const sharp=load('sharp');assert.ok(atLeast(pkg('sharp').version,'0.35.4'));
  const output=await sharp({create:{width:8,height:8,channels:3,background:{r:255,g:255,b:255}}}).png().toBuffer();
  const metadata=await sharp(output).metadata();assert.equal(metadata.width,8);assert.equal(metadata.height,8);
});
