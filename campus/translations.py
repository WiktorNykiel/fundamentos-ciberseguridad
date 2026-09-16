"""Versioned editorial translations. Code, identifiers and links are never translated."""
from __future__ import annotations
import copy
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re

LOCALES = Path(__file__).parent / 'locales'
TEXT_KEYS = {'title', 'description', 'environment', 'tasks', 'evidence', 'success', 'recovery', 'question', 'explanation', 'kind'}
PROTECTED = {'pre', 'code', 'script', 'style', 'kbd', 'samp'}

def key(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def useful(text: str) -> bool:
    return bool(re.search(r'[a-zA-ZáéíóúüñÁÉÍÓÚÑ]', text)) and not re.fullmatch(r'[A-Z][0-9]{2}[A-Z]?', text.strip())

class TextHTML(HTMLParser):
    def __init__(self, convert):
        super().__init__(convert_charrefs=False)
        self.convert = convert
        self.protected = 0
        self.output = []
    def handle_starttag(self, tag, attrs):
        self.output.append(self.get_starttag_text())
        if tag in PROTECTED: self.protected += 1
    def handle_startendtag(self, tag, attrs): self.output.append(self.get_starttag_text())
    def handle_endtag(self, tag):
        self.output.append('</' + tag + '>')
        if tag in PROTECTED: self.protected = max(0, self.protected - 1)
    def handle_data(self, data):
        if self.protected or not useful(data.strip()):
            self.output.append(data)
        else:
            start = data[:len(data)-len(data.lstrip())]
            end = data[len(data.rstrip()):]
            self.output.append(start + html.escape(self.convert(data.strip()), quote=False) + end)
    def handle_entityref(self, name): self.output.append('&'+name+';')
    def handle_charref(self, name): self.output.append('&#'+name+';')
    def handle_comment(self, data): self.output.append('<!--'+data+'-->')
    def handle_decl(self, decl): self.output.append('<!'+decl+'>')

def transform_html(value: str, convert) -> str:
    parser = TextHTML(convert)
    parser.feed(value)
    parser.close()
    return ''.join(parser.output)

def transform(value, convert, field=''):
    if isinstance(value, dict): return {k: transform(v, convert, k) for k,v in value.items()}
    if isinstance(value, list): return [transform(v, convert, field) for v in value]
    if isinstance(value, str):
        if field == 'html': return transform_html(value, convert)
        if field in TEXT_KEYS or field == 'options':
            return convert(value) if useful(value) else value
    return value

def extract(data) -> dict[str,str]:
    found = {}
    def capture(text):
        found[key(text)] = text
        return text
    transform(data, capture)
    return found

def english(data, mapping_path: Path | None = None):
    payload = json.loads((mapping_path or LOCALES/'en-content.json').read_text('utf-8'))
    entries = payload['entries']
    overrides_path = LOCALES/'en-overrides.json'
    overrides = json.loads(overrides_path.read_text('utf-8')) if overrides_path.exists() else {}
    used = set()
    def convert(text):
        ident = key(text)
        if text in overrides:
            used.add(ident)
            return overrides[text]
        item = entries.get(ident)
        if not item or item.get('source') != text or not isinstance(item.get('target'),str) or not item['target'].strip():
            raise ValueError('Missing/stale English translation: '+text[:100])
        used.add(ident)
        return item['target']
    result = transform(copy.deepcopy(data), convert)
    result['language'] = 'en'
    result['translation'] = {'method':'machine-assisted, with editorial overrides','segments':len(used),'sourceLanguage':'es','model':payload.get('model'),'review':'Structure and protected code verified; independent English technical proofreading remains recommended.'}
    for m in result['modules']:
        m['search'] = re.sub('<[^>]+>', ' ', m['html'])
    return result

if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('output',type=Path);a=p.parse_args()
    from build import collect
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(extract(collect()),ensure_ascii=False),encoding='utf-8')
