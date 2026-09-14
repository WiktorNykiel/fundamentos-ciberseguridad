// Bounded compatibility checks; no exploitation or external network calls.
const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');
const pkg = name => JSON.parse(fs.readFileSync(path.join(process.cwd(), 'node_modules', name, 'package.json'), 'utf8'));
// Accept newer stable releases instead of blocking legitimate future dependency PRs.
function atLeast(actual, minimum) {
  assert.match(actual, /^\d+\.\d+\.\d+$/, 'Expected a stable semantic version');
  const a = actual.split('.').map(Number);
  const b = minimum.split('.').map(Number);
  for (let i = 0; i < 3; i++) {
    if (a[i] !== b[i]) return a[i] > b[i];
  }
  return true;
}
test('Next and ESLint configuration stay aligned on a reviewed stable release', () => {
  assert.equal(pkg('next').version, pkg('eslint-config-next').version);
  assert.ok(atLeast(pkg('next').version, '16.3.5'));
});
test('React and React DOM stay aligned on a patched stable release', () => {
  assert.equal(pkg('react').version, pkg('react-dom').version);
  assert.ok(atLeast(pkg('react').version, '19.2.8'));
});
test('minimatch handles ordinary paths and alternatives', () => {
  const m = require('minimatch');
  assert.equal(m('notes/course.md', '**/*.md'), true);
  assert.equal(m('notes/course.txt', '**/*.md'), false);
  assert.equal(m('notes/a.md', 'notes/{a,b}.md'), true);
});
test('picomatch preserves positive and negative ordinary matches', () => {
  const matches = require('picomatch')('notes/*.md');
  assert.equal(matches('notes/course.md'), true);
  assert.equal(matches('other/course.md'), false);
});
test('brace expansion is compatible on bounded expressions', () => {
  assert.deepEqual(require('brace-expansion')('module{1,2}'), ['module1','module2']);
});
test('flatted round-trips a small circular object', () => {
  const f = require('flatted'); const value = {title:'curso'}; value.self=value;
  const restored = f.parse(f.stringify(value));
  assert.equal(restored.self, restored); assert.equal(restored.title, 'curso');
});
test('js-yaml preserves a bounded ordinary configuration', () => {
  const yaml = require('js-yaml');
  assert.deepEqual(yaml.load('course: fundamentos\nhours: 480\n'), {course:'fundamentos', hours:480});
});
test('nanoid produces identifiers with the requested ordinary length', () => {
  const {nanoid} = require('nanoid'); const values = new Set(Array.from({length:20},()=>nanoid(21)));
  assert.equal(values.size,20); for(const id of values)assert.equal(id.length,21);
});
test('browserslist resolves a fixed supported browser query', () => {
  assert.deepEqual(require('browserslist')('chrome 120'), ['chrome 120']);
});
test('baseline mapping exposes version data', () => {
  const mapping=require('baseline-browser-mapping');
  assert.equal(typeof mapping.getAllVersions, 'function');
  assert.ok(mapping.getAllVersions());
});
test('humanfs reads bounded JSON with runtime dependencies', async () => {
  const {hfs} = await import('@humanfs/node');
  const config = await hfs.json('package.json');
  const expected = JSON.parse(fs.readFileSync('package.json', 'utf8'));
  assert.deepEqual(config.dependencies, expected.dependencies);
});
test('sharp processes an in-memory 8x8 image', async () => {
  const sharp=require('sharp');
  assert.ok(atLeast(pkg('sharp').version, '0.35.4'));
  const output=await sharp({create:{width:8,height:8,channels:3,background:{r:255,g:255,b:255}}}).png().toBuffer();
  const metadata=await sharp(output).metadata();
  assert.equal(metadata.width,8); assert.equal(metadata.height,8);
});
