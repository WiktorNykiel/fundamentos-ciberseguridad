#!/usr/bin/env python3
"""Build a standalone static resource directory using Python stdlib only."""
from __future__ import annotations
from pathlib import Path
import html,json,shutil,re
from urllib.parse import urlsplit
from validate import validate,load,ROOT
E=lambda x:html.escape(str(x),quote=True)
CSP="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'"
def inline(text:str)->str:
    """Small safe Markdown subset; no arbitrary HTML or executable links."""
    result=[];last=0
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',text):
        result.append(E(text[last:m.start()]));label,url=m.groups();u=urlsplit(url)
        safe=(u.scheme=='https' and bool(u.hostname) and not u.username and not u.password) or (not u.scheme and not u.netloc and not url.startswith('/'))
        if safe:
            url=re.sub(r'\.md(?=$|[#?])','.html',url)
            result.append('<a href="'+E(url)+'" rel="noreferrer noopener">'+E(label)+'</a>')
        else:result.append(E(label))
        last=m.end()
    result.append(E(text[last:]));out=''.join(result)
    out=re.sub(r'`([^`]+)`',r'<code>\1</code>',out)
    return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',out)

def markdown(text:str)->str:
    lines=text.splitlines();out=[];i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('```'):
            block=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):block.append(lines[i]);i+=1
            out.append('<pre><code>'+E('\n'.join(block))+'</code></pre>')
        elif line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',c) for c in cells):rows.append(cells)
                i+=1
            if rows:
                out.append('<div class="table-scroll"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in rows[1:])+'</tbody></table></div>')
            continue
        elif re.match(r'^#{1,6} ',line):
            level=len(line.split(' ',1)[0]);out.append(f'<h{level}>'+inline(line[level+1:])+f'</h{level}>')
        elif line.startswith(('- ','* ')):
            rows=[]
            while i<len(lines) and lines[i].startswith(('- ','* ')):rows.append('<li>'+inline(lines[i][2:])+'</li>');i+=1
            out.append('<ul>'+''.join(rows)+'</ul>');continue
        elif line.strip():out.append('<p>'+inline(line)+'</p>')
        i+=1
    return ''.join(out)

def build(root:Path=ROOT)->dict:
    report=validate(root);sources,certs=load(root);out=root/'site'
    if out.is_symlink():raise ValueError('Symlink output is not allowed')
    if out.exists():
        if any(p.is_symlink() for p in out.rglob('*')):raise ValueError('Symlink output member is not allowed')
        shutil.rmtree(out)
    out.mkdir()
    for name in ('theme.css','catalog.js'):shutil.copyfile(root/'tools'/name,out/name)
    categories=list(dict.fromkeys(s['category'] for s in sources['sources']))
    cards=''.join(f'<article data-source="{E(s["id"])}" data-category="{E(s["category"])}"><div><span class="pill">{E(s["category"])}</span></div><h3><a href="{E(s["url"])}" rel="noreferrer noopener">{E(s["title"])}</a></h3><p>{E(s["annotation"])}</p><p class="small">{E(s["jurisdiction"])} · {E(s["language"])} · {E(s["id"])}<br>Consulta {E(s["reviewed_at"])} · {E(s["review_status"])}</p></article>' for s in sources['sources'])
    # Include the Markdown source documents inside the standalone site, not links to its parent.
    docs=out/'docs';docs.mkdir(exist_ok=True)
    for p in root.glob('*.md'):shutil.copyfile(p,docs/p.name)
    shutil.copytree(root/'plantillas',docs/'plantillas',dirs_exist_ok=True)
    shutil.copytree(root/'data',docs/'data',dirs_exist_ok=True)
    for p in docs.rglob('*.md'):
        text=p.read_text('utf-8');title=text.splitlines()[0].lstrip('# ')
        back='../'*(len(p.relative_to(out).parts)-1)
        document='<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>'+E(title)+' · SmartKEA</title><link rel="stylesheet" href="'+back+'theme.css"></head><body><a class="skip" href="#main">Saltar al contenido</a><header class="top"><a class="brand" href="'+back+'index.html">SmartKEA / Awesome DPD</a><a href="'+E(p.name)+'" download>Descargar Markdown</a></header><main id="main" class="doc">'+markdown(text)+'</main><footer>Material educativo independiente · Solo datos ficticios · No es asesoramiento ni certificación.</footer></body></html>'
        p.with_suffix('.html').write_text(document,'utf-8')
    page='''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="description" content="Fuentes oficiales, rutas de estudio y criterios de certificación para DPD y privacidad. SmartKEA."><title>Awesome DPD · SmartKEA</title><link rel="stylesheet" href="theme.css"><script defer src="catalog.js"></script></head><body><a class="skip" href="#main">Saltar al contenido</a><header class="top"><a class="brand" href="index.html">SmartKEA <span class="small">/ Awesome DPD</span></a><div class="row"><a href="docs/README.html">Documentación</a><button id="print" type="button">Imprimir</button></div></header><main id="main"><section class="hero"><div><span class="tag">Privacidad · España / Unión Europea</span><h1>De la norma<br>a la evidencia.</h1><p>Un punto de entrada para aprender, contrastar y decidir. Fuentes primarias comentadas, criterios de certificación y trabajo práctico para DPD, legal, negocio y tecnología.</p><p class="small">Edición inicial · Revisión 18 septiembre 2026 · Español</p></div><aside class="panel"><div class="stats"><div><div class="stat">32</div><small>fuentes</small></div><div><div class="stat">13</div><small>credenciales</small></div><div><div class="stat">8</div><small>casos</small></div></div><div class="notice">Autoestudio, no certificación. Este proyecto no es un curso reconocido ni está avalado por las entidades enlazadas.</div><p class="small">Sin cuentas, telemetría o descarga automática de fuentes. Los enlaces externos se abren al elegirlos.</p></aside></section><section class="grid"><article><span class="tag">01 · Orientarse</span><h2>Una ruta, no una lista infinita</h2><p>Dos entradas —derecho y tecnología— y seis etapas para la función DPD.</p><a href="docs/ITINERARIO.html">Ver itinerario DPD</a></article><article><span class="tag">02 · Demostrar</span><h2>Casos y plantillas</h2><p>Construye un RAT, razona una EIPD y documenta una decisión. Siempre con datos ficticios.</p><a href="docs/CASOS.html">Ocho casos con criterios</a><a href="docs/plantillas/README.html">Ocho plantillas de aprendizaje</a></article><article><span class="tag">03 · Especializarse</span><h2>Elegir una credencial</h2><p>Objetivo, requisitos y límites antes de comprar un examen. Distingue formación, examen y certificación.</p><a href="docs/CERTIFICACIONES.html">Comparar opciones</a><a href="docs/90-DIAS.html">Primeros 90 días</a></article></section><section class="section"><h2>La biblioteca de fuentes</h2><p>Filtra por tema o busca un concepto. La anotación explica para qué sirve cada recurso; no sustituye el documento oficial.</p><div class="filters"><label>Buscar<input id="q" type="search" maxlength="160" placeholder="EIPD, brecha, experiencia, IA…"></label><label>Tema<select id="category"><option value="all">Todos los temas</option>'''+''.join(f'<option value="{E(c)}">{E(c)}</option>' for c in categories)+'''</select></label><button id="reset" type="button">Limpiar</button></div><p class="small" id="count" role="status" aria-live="polite"></p><p class="empty" id="empty" hidden>No hay coincidencias. Prueba otro término o limpia los filtros.</p><div class="grid">'''+cards+'''</div></section><section class="notice"><strong>Vigencia y derechos.</strong> Consulta editorial de páginas oficiales, no monitorización continua ni auditoría de todas sus descargas. Público no significa licencia abierta: la elección de licencia queda pendiente del titular. Las marcas y documentos externos conservan sus derechos.</section></main><footer>SmartKEA · Formación independiente · Solo datos sintéticos · <a href="docs/SECURITY.html">Seguridad</a> · <a href="docs/AVISO-LICENCIA.html">Licencias</a> · <a href="docs/CONTRIBUTING.html">Contribuir</a></footer></body></html>'''
    (out/'index.html').write_text(page,'utf-8')
    (out/'_headers').write_text('/*\n  Content-Security-Policy: '+CSP+'\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n','utf-8')
    return report
if __name__=='__main__':print(json.dumps(build(),ensure_ascii=False,indent=2))
