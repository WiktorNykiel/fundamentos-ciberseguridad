import json,sys,tempfile,unittest,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
from validate import validate
from render import build,markdown,inline
class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'dpd'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('site','__pycache__'))
    def mutate(self,fn,file='sources.json'):
        p=self.root/'data'/file;d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
    def test_valid_catalogue(self):self.assertEqual(validate(self.root)['sources'],32)
    def test_duplicate_source_rejected(self):
        self.mutate(lambda d:d['sources'].append(d['sources'][0]))
        with self.assertRaises(ValueError):validate(self.root)
    def test_unsafe_url_rejected(self):
        self.mutate(lambda d:d['sources'][0].update(url='javascript:alert(1)'))
        with self.assertRaises(ValueError):validate(self.root)
    def test_credentials_in_url_rejected(self):
        self.mutate(lambda d:d['sources'][0].update(url='https://user:password@example.com/'))
        with self.assertRaises(ValueError):validate(self.root)
    def test_unknown_source_rejected(self):
        self.mutate(lambda d:d['certifications'][0].update(source='MISSING'),'certifications.json')
        with self.assertRaises(ValueError):validate(self.root)
    def test_mandatory_certification_rejected(self):
        self.mutate(lambda d:d['certifications'][0].update(mandatory=True),'certifications.json')
        with self.assertRaises(ValueError):validate(self.root)
    def test_broken_local_link_rejected(self):
        (self.root/'BAD.md').write_text('[bad](missing.md)')
        with self.assertRaises(ValueError):validate(self.root)
    def test_symlink_rejected(self):
        (self.root/'link.md').symlink_to(self.root/'README.md')
        with self.assertRaises(ValueError):validate(self.root)
    def test_no_executable_markdown(self):
        self.assertNotIn('<script>',markdown('<script>alert(1)</script>'))
        self.assertNotIn('href=',inline('[bad](javascript:evil)'))
    def test_site_has_rendered_documents(self):
        build(self.root);p=self.root/'site/docs/CASOS.html'
        self.assertTrue(p.is_file());self.assertIn('theme.css',p.read_text())
        self.assertNotIn('href="docs/CASOS.md"',(self.root/'site/index.html').read_text())
        self.assertTrue((self.root/'site/docs/plantillas/README.html').is_file())
    def test_deterministic_site(self):
        build(self.root);a=(self.root/'site/index.html').read_bytes();build(self.root)
        self.assertEqual(a,(self.root/'site/index.html').read_bytes())
if __name__=='__main__':unittest.main()
