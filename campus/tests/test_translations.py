"""Bilingual coverage, deterministic IDs and protected code parity."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import build
import translations

class TranslationTests(unittest.TestCase):
    def test_html_translates_prose_not_commands(self):
        s='<h2 id="M01-x">Hola</h2><p>Texto <code>echo hola</code></p><pre><code>rm ejemplo</code></pre>'
        result=translations.transform_html(s,lambda x:'EN:'+x)
        self.assertIn('EN:Hola',result)
        self.assertIn('<code>echo hola</code>',result)
        self.assertIn('<code>rm ejemplo</code>',result)
        self.assertIn('id="M01-x"',result)
    def test_source_digest_changes_when_text_changes(self):
        self.assertNotEqual(translations.key('Hola'),translations.key('Hola.'))
    def test_missing_translation_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'en.json';p.write_text(json.dumps({'entries':{}}))
            with self.assertRaises(ValueError):translations.english({'modules':[],'title':'Texto no registrado'},p)
    def test_stale_translation_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'en.json';p.write_text(json.dumps({'entries':{translations.key('Texto nuevo'):{'source':'Old','target':'English'}}}))
            with self.assertRaises(ValueError):translations.english({'modules':[],'title':'Texto nuevo'},p)
    def test_translated_markup_cannot_introduce_html(self):
        x=translations.transform_html('<p>Texto</p>',lambda _: '<script>bad</script>')
        self.assertNotIn('<script>',x);self.assertIn('&lt;script&gt;',x)
    def test_entities_and_whitespace_are_preserved(self):
        x=translations.transform_html('<p> Hola &amp; mundo </p>',lambda v:{'Hola':'Hello','mundo':'world'}[v])
        self.assertEqual(x,'<p> Hello &amp; world </p>')
    def test_full_catalogue_has_english_translation(self):
        es=build.collect();en=translations.english(es)
        self.assertEqual(en['language'],'en');self.assertEqual(len(en['modules']),32)
        self.assertEqual(len(en['resources']),len(es['resources']))
        self.assertEqual(en['hours'],480)
        self.assertGreater(en['translation']['segments'],2000)
    def test_source_code_links_ids_and_quiz_answers_identical(self):
        es=build.collect();en=translations.english(es)
        def parity(a,b,field=''):
            if isinstance(a,dict):
                for k,v in a.items():parity(v,b[k],k)
            elif isinstance(a,list):
                self.assertEqual(len(a),len(b))
                for x,y in zip(a,b):parity(x,y,field)
            elif field in ['id','source','correct','hours','theoryHours','practiceHours','prerequisites']:
                self.assertEqual(a,b)
            elif field=='html':
                self.assertEqual(re.findall(r'<(?:pre|code)\b.*?</(?:pre|code)>',a,re.S),re.findall(r'<(?:pre|code)\b.*?</(?:pre|code)>',b,re.S))
                self.assertEqual(re.findall(r'(?:id|href)="([^"]+)"',a),re.findall(r'(?:id|href)="([^"]+)"',b))
        parity(es,en)
    def test_readers_have_correct_languages(self):
        es=build.collect();en=translations.english(es)
        self.assertIn('lang="en"',build.reading_page(en,'en'))
        self.assertIn('lang="es"',build.reading_page(es,'es'))
        self.assertIn('Self-assessment',build.reading_page(en,'en'))
    def test_all_reviewed_quizzes_are_explicit_overrides(self):
        o=json.loads((translations.LOCALES/'en-overrides.json').read_text())
        for m in build.collect()['modules']:
            for source in [m['title'],m['quiz']['question'],m['quiz']['explanation'],*m['quiz']['options']]:
                self.assertIn(source,o)
    def test_independent_editorial_assets(self):
        page=(build.HERE/'index.html').read_text()
        self.assertNotIn('<img',page)
        self.assertIn('editorial.css',page)
        self.assertIn('ES / EN',page)
    def test_provenance_covers_new_translation_inputs(self):
        self.assertTrue((translations.LOCALES/'en-content.json').is_file())

if __name__=='__main__':unittest.main(verbosity=2)
