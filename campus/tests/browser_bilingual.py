"""Bilingual/device acceptance plus the full existing regression suite."""
import json
import re
import os
import unittest
import browser as base
from browser_extra import ExtendedBrowserTests

class BilingualBrowserTests(ExtendedBrowserTests):
    def english(self,route='#/curso'):
        self.page.goto(self.base+'/?lang=en'+route)
        self.page.wait_for_function('document.documentElement.lang === "en" && document.querySelector("#navigation .nav-main")')
        self.page.wait_for_timeout(100)
    def test_38_switch_language_preserves_work(self):
        self.goto('#/modulo/M05');self.page.locator('#read-check').check();self.page.locator('#notes').fill('nota privada no traducir')
        self.page.locator('#language-select').select_option('en')
        self.page.get_by_role('link',name='Theory',exact=True).wait_for()
        self.assertEqual(self.page.locator('html').get_attribute('lang'),'en')
        self.assertTrue(self.page.locator('#read-check').is_checked())
        self.assertEqual(self.page.locator('#notes').input_value(),'nota privada no traducir')
        self.page.locator('#language-select').select_option('es')
        self.page.get_by_role('link',name='Teoría',exact=True).wait_for()
        self.assertTrue(self.page.locator('#read-check').is_checked())
    def test_39_all_english_module_titles_and_theory(self):
        data=json.loads((base.HERE/'dist/course.en.json').read_text())
        for m in data['modules']:
            self.english('#/modulo/'+m['id'])
            self.assertEqual(self.page.locator('.module-hero h1').inner_text(),m['title'])
            self.assertGreater(len(self.page.locator('#theory').inner_text()),500)
            self.assertTrue(self.page.get_by_role('link',name='Self-assessment',exact=True).is_visible())
    def test_40_english_quiz_and_wizard(self):
        self.english('#/modulo/M05/revision');q=self.data['modules'][4]['quiz']
        self.page.locator(f'input[value="{q["correct"]}"]').check();self.page.get_by_role('button',name='Check answer',exact=True).click()
        self.assertIn('Correct answer',self.page.locator('#quiz-feedback').inner_text())
        self.english('#/modulo/M05/practica/L05A')
        for _ in range(5):self.page.locator('[data-action=step-done]').click()
        self.page.get_by_role('button',name='Complete lab',exact=True).click()
        self.assertTrue(self.state()['labs']['L05A']['done'])
    def test_41_device_link_excludes_notes_and_queries(self):
        self.goto('#/modulo/M05');self.page.locator('#notes').fill('PRIVATE NOT SHARED');self.page.locator('#read-check').check()
        self.goto('#/dispositivos');self.page.locator('[data-device=create]').click()
        url=self.page.locator('#handoff-url').input_value()
        self.assertLess(len(url),2048);self.assertIn('#/transfer/',url);self.assertNotIn('PRIVATE',url)
        self.assertEqual(self.page.locator('a[href^="mailto:"]').count(),1)
    def test_42_import_preview_and_additive_merge(self):
        self.goto('#/modulo/M05');self.page.locator('#read-check').check();self.goto('#/dispositivos');self.page.locator('[data-device=create]').click();url=self.page.locator('#handoff-url').input_value()
        receiver=self.browser.new_context(viewport={'width':744,'height':1133});p=receiver.new_page()
        try:
            p.goto(self.base+'/#/modulo/M01');p.locator('#notes').fill('receiving note');p.locator('#read-check').check()
            p.goto(url);p.locator('[data-device=accept]').wait_for()
            self.assertNotIn('#/transfer/',p.url)
            self.assertFalse(p.evaluate('(k)=>JSON.parse(localStorage.getItem(k)).modules.M05.read',base.KEY))
            p.locator('[data-device=accept]').click();p.locator('#read-check').wait_for()
            state=p.evaluate('(k)=>JSON.parse(localStorage.getItem(k))',base.KEY)
            self.assertTrue(state['modules']['M05']['read']);self.assertTrue(state['modules']['M01']['read']);self.assertEqual(state['modules']['M01']['notes'],'receiving note')
        finally:receiver.close()
    def test_43_invalid_link_does_not_overwrite_progress(self):
        self.goto('#/modulo/M01');self.page.locator('#read-check').check()
        self.goto('#/transfer/not-valid')
        self.assertIn('no válido',self.page.locator('#main').inner_text())
        self.assertTrue(self.state()['modules']['M01']['read'])
    def test_44_share_requires_click_and_sends_no_notes(self):
        self.goto('#/modulo/M05');self.page.locator('#notes').fill('PRIVATE')
        self.goto('#/dispositivos');self.page.evaluate("navigator.share=async data=>{window.shared=data}")
        self.page.locator('[data-device=create]').click();self.assertIsNone(self.page.evaluate('window.shared'))
        self.page.locator('[data-device=share]').click();value=self.page.evaluate('window.shared')
        self.assertEqual(set(value),{'title','url'});self.assertNotIn('PRIVATE',json.dumps(value))
    def test_45_phone_tablet_desktop_layouts_both_languages(self):
        for lang in ['es','en']:
            for width,height in [(320,568),(375,812),(390,844),(744,1133),(768,1024),(820,1180),(1024,768),(1366,900)]:
                self.page.set_viewport_size({'width':width,'height':height})
                self.page.goto(self.base+f'/?lang={lang}#/temario');self.page.locator('#outline-query').wait_for()
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width+1,(lang,width))
                self.assertGreaterEqual(self.page.locator('#language-select').bounding_box()['height'],43)
                self.page.locator('#outline-block').select_option('linux');self.assertEqual(self.page.locator('[data-outline-row]:visible').count(),8)
                if width in (390,744,820):self.page.screenshot(path=str(base.HERE/f'qa/screenshots/bilingual-{lang}-{width}-{os.environ.get("BROWSER_ENGINE","chromium")}.png'),full_page=True)
    def test_46_english_reader(self):
        self.page.goto(self.base+'/reading.html')
        self.assertEqual(self.page.locator('html').get_attribute('lang'),'en')
        self.assertEqual(self.page.locator('article[id^="M"]').count(),32)
        self.assertEqual(self.page.locator('section[id^="L"]').count(),96)
    def test_47_english_presentation(self):
        self.english('#/modulo/M05');self.page.get_by_role('button',name='Presentation mode ▷').click()
        self.assertIn('SLIDE',self.page.locator('#slide-counter').inner_text())
        self.page.keyboard.press('ArrowRight');self.assertIn('2 /',self.page.locator('#slide-counter').inner_text())
        self.page.screenshot(path=str(base.HERE/'qa/screenshots/bilingual-presentation.png'))
    def test_48_english_reference_search(self):
        self.english('#/temario');self.page.locator('#global-search').fill('permissions')
        self.page.get_by_role('heading',name='Search results.').wait_for()
        self.assertGreater(self.page.locator('.search-result').count(),0)
    def test_49_english_download_names_do_not_change_commands(self):
        data=json.loads((base.HERE/'dist/course.en.json').read_text())
        self.english('#/modulo/M05')
        expected=re.findall(r'<code[^>]*>(.*?)</code>',data['modules'][4]['html'],re.S)
        self.assertGreater(len(expected),0)
        self.assertEqual(self.page.locator('#theory code').count(),len(expected))
    def test_50_independent_editorial_theme(self):
        self.assertEqual(self.page.locator('.topbar img').count(),0)
        colour=self.page.evaluate('getComputedStyle(document.documentElement).getPropertyValue("--brand").trim()')
        self.assertEqual(colour,'#b5122d')

if __name__=='__main__':unittest.main(verbosity=2)
