#!/usr/bin/env python3
"""Real-browser checks for routes and the independently deployable DPD catalogue."""
from functools import partial
from http.server import ThreadingHTTPServer
import json,os,sys,unittest
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright,expect
HERE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(HERE))
from serve import Handler
KEY='smartkea.learning-paths.v1';CAMPUS_KEY='fundamentos-ciberseguridad:progress:v1'
class RoutesAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(HERE/'dist')))
        Thread(target=cls.server.serve_forever,daemon=True).start()
        cls.base=f'http://127.0.0.1:{cls.server.server_port}/'
        cls.pw=sync_playwright().start();cls.engine=os.environ.get('CAMPUS_BROWSER','chromium')
        if cls.engine not in ('chromium','webkit','firefox'):raise ValueError('Unsupported browser')
        options={'headless':True}
        if os.environ.get('CAMPUS_BROWSER_EXECUTABLE'):options['executable_path']=os.environ['CAMPUS_BROWSER_EXECUTABLE']
        cls.browser=getattr(cls.pw,cls.engine).launch(**options)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.pw.stop();cls.server.shutdown();cls.server.server_close()
    def setUp(self):
        self.context=self.browser.new_context(viewport={'width':1440,'height':1000})
        self.page=self.context.new_page();self.errors=[]
        self.page.on('pageerror',lambda e:self.errors.append(str(e)))
    def tearDown(self):
        try:self.assertEqual(self.errors,[])
        finally:self.context.close()
    def go(self,path='rutas.html'):self.page.goto(self.base+path,wait_until='networkidle')
    def stored(self,key=KEY):return self.page.evaluate('(k)=>localStorage.getItem(k)',key)
    def test_01_routes_and_dpd_filter(self):
        self.go();expect(self.page.locator('[data-route]:visible')).to_have_count(6)
        expect(self.page.locator('[data-phase]')).to_have_count(26)
        self.page.locator('#route-filter').select_option('dpd')
        expect(self.page.locator('[data-route]:visible')).to_have_count(1)
        expect(self.page.locator('[data-phase]:visible')).to_have_count(6)
        expect(self.page.locator('#ruta-dpd')).to_contain_text('128 h')
    def test_02_storage_requires_opt_in(self):
        self.go();self.page.locator('[data-phase]').first.check();self.assertIsNone(self.stored())
        self.page.reload();expect(self.page.locator('[data-phase]').first).not_to_be_checked()
        self.page.locator('[data-phase]').first.check();self.page.locator('#remember-paths').check()
        self.assertEqual(len(json.loads(self.stored())['completed']),1)
        self.page.reload();expect(self.page.locator('[data-phase]').first).to_be_checked()
        self.page.locator('#remember-paths').uncheck();self.assertIsNone(self.stored())
    def test_03_clear_preserves_campus(self):
        self.go();self.page.evaluate('(k)=>localStorage.setItem(k,"synthetic-campus-fixture")',CAMPUS_KEY)
        self.page.locator('[data-phase]').first.check();self.page.locator('#remember-paths').check()
        self.page.once('dialog',lambda d:d.accept());self.page.locator('#clear-paths').click()
        self.assertIsNone(self.stored());self.assertEqual(self.stored(CAMPUS_KEY),'synthetic-campus-fixture')
    def test_04_malformed_storage_is_ignored(self):
        self.go();self.page.evaluate('(k)=>localStorage.setItem(k,JSON.stringify({schema:1,completed:["<script>"]}))',KEY)
        self.page.reload();expect(self.page.locator('#remember-paths')).not_to_be_checked()
        expect(self.page.locator('[data-phase]:checked')).to_have_count(0)
    def test_05_presentation_keyboard(self):
        self.go();self.page.locator('#start-presentation').click()
        expect(self.page.locator('#slide-count')).to_have_text('Ruta 1 de 6')
        self.page.keyboard.press('ArrowRight');expect(self.page.locator('#slide-count')).to_have_text('Ruta 2 de 6')
        self.page.keyboard.press('Escape');expect(self.page.locator('#start-presentation')).to_be_focused()
        expect(self.page.locator('[data-route]:visible')).to_have_count(6)
    def test_06_catalogue_search_and_documents(self):
        self.go('dpd/index.html');expect(self.page.locator('[data-source]:visible')).to_have_count(32)
        self.page.locator('#q').fill('nonexistent-123456');expect(self.page.locator('#empty')).to_be_visible()
        self.page.locator('#reset').click();expect(self.page.locator('[data-source]:visible')).to_have_count(32)
        self.page.locator('a[href="docs/CASOS.html"]').click()
        expect(self.page.locator('h1')).to_contain_text('Casos');self.assertIn('<html',self.page.content())
    def test_07_responsive_and_local_requests(self):
        remote=[];self.page.on('request',lambda req:remote.append(req.url) if not req.url.startswith(self.base) else None)
        out=HERE/'qa/current'/self.engine/'screenshots';out.mkdir(parents=True,exist_ok=True)
        for path in ('rutas.html','dpd/index.html','dpd/docs/CERTIFICACIONES.html'):
            for width in (360,768,1440):
                self.page.set_viewport_size({'width':width,'height':960});self.go(path)
                self.assertTrue(self.page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(path,width))
                if width in (360,1440):self.page.screenshot(path=str(out/f'{path.replace("/","-")}-{width}.png'),full_page=False)
        self.assertEqual(remote,[])
    def test_08_without_javascript(self):
        context=self.browser.new_context(java_script_enabled=False);self.addCleanup(context.close)
        p=context.new_page();p.goto(self.base+'rutas.html');expect(p.locator('[data-route]')).to_have_count(6)
        p.goto(self.base+'dpd/index.html');expect(p.locator('[data-source]')).to_have_count(32)
        p.goto(self.base+'dpd/docs/ITINERARIO.html');expect(p.locator('h1')).to_be_visible()
if __name__=='__main__':unittest.main(verbosity=2)
