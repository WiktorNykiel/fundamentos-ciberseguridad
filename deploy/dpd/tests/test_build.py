import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('builder',Path(__file__).resolve().parents[1]/'build_assets.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.src=self.root/'source';self.src.mkdir();self.out=self.root/'public'
        (self.src/'index.html').write_text('<html><head></head><body><a href="doc.html">Doc</a><script src="a.js"></script></body></html>')
        (self.src/'doc.html').write_text('<html><head></head><body><a href="index.html">Inicio</a></body></html>')
        (self.src/'a.js').write_text('console.log("test")')
    def test_mount(self):
        r=b.mount(self.src,self.out);self.assertEqual(r['files'],3);self.assertEqual(r['deploymentVerified'],False)
        self.assertIn('https://smartkea.com/introduccion-dpd/',(self.out/'introduccion-dpd/index.html').read_text())
        self.assertTrue((self.out/'introduccion-dpd/_release.json').exists())
    def test_deterministic(self):
        first=b.mount(self.src,self.out);second=b.mount(self.src,self.out);self.assertEqual(first,second)
    def test_rebuild_changes_hash(self):
        first=b.mount(self.src,self.out);(self.src/'a.js').write_text('changed');self.assertNotEqual(first['treeSha256'],b.mount(self.src,self.out)['treeSha256'])
    def test_root_link_mounted(self):
        (self.src/'doc.html').write_text('<a href="/">Inicio</a>');b.mount(self.src,self.out)
        self.assertIn('/introduccion-dpd/',(self.out/'introduccion-dpd/doc.html').read_text())
    def test_reject_escape(self):
        (self.src/'doc.html').write_text('<a href="../outside.html">Bad</a>')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
    def test_reject_missing(self):
        (self.src/'doc.html').write_text('<a href="missing.html">Bad</a>')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
    def test_reject_script_link(self):
        (self.src/'doc.html').write_text('<a href="javascript:alert(1)">Bad</a>')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
    def test_reject_symlink(self):
        (self.src/'link.js').symlink_to(self.src/'a.js')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
    def test_reject_unmarked_output(self):
        self.out.mkdir();(self.out/'keep.txt').write_text('retain')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
        self.assertEqual((self.out/'keep.txt').read_text(),'retain')
    def test_reject_unexpected_file(self):
        (self.src/'server.py').write_text('not public')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
    def test_skip_host_config(self):
        (self.src/'_headers').write_text('not served');b.mount(self.src,self.out)
        self.assertFalse((self.out/'introduccion-dpd/_headers').exists())
    def test_reject_invalid_commit(self):
        with self.assertRaises(ValueError):b.mount(self.src,self.out,'not-a-sha')
    def test_preserve_old_build_on_failure(self):
        first=b.mount(self.src,self.out);(self.src/'doc.html').write_text('<a href="missing.html">Bad</a>')
        with self.assertRaises(ValueError):b.mount(self.src,self.out)
        old=json.loads((self.out/'introduccion-dpd/_release.json').read_text());self.assertEqual(first,old)
if __name__=='__main__':unittest.main()
