#!/usr/bin/env python3
"""Generate the two HTML editions using only Python's standard library."""
from pathlib import Path
from html import escape
from content.site import ES, EN, LINKS

ROOT = Path(__file__).resolve().parent
BASE = 'https://artfisica.github.io/presentacion-Instituto-de-Ingenieria-Venezuela/'

def paragraphs(items):
    return ''.join(f'<p>{p}</p>' for p in items)

def project(p, c):
    links = ''.join(f'<a href="{escape(LINKS[key], quote=True)}">{escape(label)} <span aria-hidden="true">↗</span></a>' for label, key in p['links'])
    if p.get('image'):
        visual = f'<img src="assets/{p["image"]}" alt="{escape(p["alt"], quote=True)}" class="{p.get("class", "")}" loading="lazy" width="1200" height="600">'
    else:
        title, bottom, kicker = p['tile']
        visual = f'<div class="type-tile {p.get("tone", "")}" aria-hidden="true"><div class="tile-kicker">{kicker}</div><div class="tile-title">{title}</div><div class="tile-bottom">{bottom}</div></div>'
    badge = f'<span class="project-type">{p["badge"]}</span>' if p.get('badge') else ''
    credit = f'<p class="credit">{p["credit"]}</p>' if p.get('credit') else ''
    primary = LINKS[p['links'][0][1]]
    return f'''<article class="project" id="project-{p['id']}">
      <a class="figure-link" href="{primary}" aria-label="{escape(p['links'][0][0], quote=True)}"><div class="project-visual">{visual}{badge}</div></a>
      <div class="project-body"><div class="eyebrow">{p['category']}</div><h3>{p['title']}</h3><p>{p['text']}</p>
      <details><summary>{c['details']}</summary><p>{p['detail']}</p></details>
      <div class="project-links">{links}</div>{credit}</div>
    </article>'''

def render(c):
    lang=c['lang']
    nav=''.join(f'<a href="#{anchor}">{label}</a>' for anchor,label in zip(['charla','proyectos','recursos','arturo'],c['nav']))
    language_parts=[]
    for filename, code, label in [('index.html','es','ES'), ('en.html','en','EN')]:
        selected = 'selected' if lang == code else ''
        current = 'aria-current="page"' if lang == code else ''
        language_parts.append(f'<a href="{filename}" lang="{code}" hreflang="{code}" class="{selected}" {current}>{label}</a>')
    language=''.join(language_parts)
    cards=''.join(project(p,c) for p in c['projects'])
    steps=''.join(f'<div class="method-step"><span>0{i}</span><h3>{title}</h3><p>{body}</p></div>' for i,(title,body) in enumerate(c['steps'],1))
    resources=''.join(f'<article class="resource"><h3>{title}</h3><p>{body}</p><a href="{LINKS[key]}">{label} ↗</a></article>' for title,body,label,key in c['resources'])
    canonical=BASE+('' if lang=='es' else 'en.html')
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c['title']} — Arturo Sánchez Pineda</title><meta name="description" content="{escape(c['description'],quote=True)}">
<meta name="author" content="Arturo Sánchez Pineda"><meta name="theme-color" content="#102434">
<meta property="og:image" content="{BASE}assets/atlas-venezuela.webp"><meta property="og:image:alt" content="{escape(c['photo_alt'],quote=True)}"><meta property="og:type" content="website"><meta property="og:title" content="{c['title']}"><meta property="og:description" content="{escape(c['description'],quote=True)}"><meta property="og:locale" content="{'es_VE' if lang=='es' else 'en_US'}"><meta property="og:url" content="{canonical}">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="es" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en.html"><link rel="alternate" hreflang="x-default" href="{BASE}">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="stylesheet" href="assets/style.css">
<link rel="preload" href="assets/fonts/ibm-plex-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
</head><body>
<a class="skip" href="#main">{c['skip']}</a>
<header class="topbar"><nav class="wrap nav" aria-label="{'Principal' if lang=='es' else 'Main'}"><a class="brand" href="index.html"><span aria-hidden="true">[ a / s ]</span> Arturo Sánchez Pineda</a><div class="navlinks"><div class="navsections">{nav}</div><div class="language" aria-label="{'Idioma' if lang=='es' else 'Language'}">{language}</div></div></nav></header>
<main id="main">
<section class="hero wrap" aria-labelledby="hero-title"><div class="eyebrow">{c['event']}</div><h1 id="hero-title">{c['hero']}</h1><p class="event-chip">{'Fecha y enlace: por confirmar' if lang == 'es' else 'Date and meeting link: to be confirmed'}</p>
<div class="hero-bottom"><div><p class="subtitle">{c['subtitle']}</p><div class="actions"><a class="button" href="#proyectos">{c['cta']} <span aria-hidden="true">↘</span></a><a class="button secondary" href="#charla">{c['read']}</a></div></div><p class="speaker"><strong>Arturo Sánchez Pineda</strong>{c['role']}<br>CERN / ATLAS · INAIT · Creative Commons</p></div>
<aside class="takeaway"><div><h2>{c['takeaway_title']}</h2><p>{c['takeaway_text']}</p></div><a class="button" href="{LINKS['repo']}#ejercicios">{c['takeaway_cta']} ↓</a></aside>
<figure><div class="hero-image"><img src="assets/atlas-venezuela.webp" width="1600" height="799" alt="{escape(c['photo_alt'],quote=True)}" fetchpriority="high"><span class="image-label">{c['photo_label']}</span></div><figcaption class="caption">{c['photo_caption']} <a href="{LINKS['theses']}">{'Fuente' if lang=='es' else 'Source'} ↗</a></figcaption></figure></section>
<section class="section wrap" id="charla"><div class="section-head"><div class="eyebrow">{c['intro_label']}</div><h2>{c['intro_title']}</h2></div><div class="intro-grid"><aside class="side-note">{c['intro_note']}</aside><div class="prose">{paragraphs(c['intro'])}<blockquote class="callout">{c['quote']}</blockquote></div></div></section>
<section class="section wrap" id="resultados"><div class="section-head"><div class="eyebrow">{'Tu primer resultado' if lang=='es' else 'Your first result'}</div><div><h2>{'Qué vas a producir<br>en diez minutos' if lang=='es' else 'What you can make<br>in ten minutes'}</h2><p>{'Datos de ejemplo: seis valores, promedio 25, mínimo 23 y máximo 27. Cambia un 24 por un 30 y comprueba que el promedio pasa a 26.' if lang=='es' else 'Example data: six values, mean 25, minimum 23 and maximum 27. Change a 24 to a 30 and check that the mean becomes 26.'}</p></div></div>
<div class="output-grid"><figure><a href="{LINKS['repo']}/blob/main/ejemplos/salida-esperada/grafico.png"><img src="assets/ejemplo-grafico.webp" width="1000" height="556" loading="lazy" alt="{'Gráfico de barras con los seis valores del CSV de ejemplo.' if lang=='es' else 'Bar chart showing the six sample CSV values.'}"></a><figcaption>{'Un gráfico reproducible desde tu CSV.' if lang=='es' else 'A reproducible chart from your CSV.'}</figcaption></figure>
<figure><a href="{LINKS['repo']}/blob/main/ejemplos/salida-esperada/informe.pdf"><img src="assets/ejemplo-pdf.webp" width="600" height="849" loading="lazy" alt="{'Vista previa del PDF generado desde Markdown y una fotografía con crédito ATLAS/CERN.' if lang=='es' else 'Preview of the PDF generated from Markdown and an ATLAS/CERN-credited photograph.'}"></a><figcaption>{'Tu texto e imagen, convertidos en PDF.' if lang=='es' else 'Your text and image, turned into a PDF.'}</figcaption></figure></div><p class="output-links"><a href="{LINKS['repo']}/tree/main/ejemplos/salida-esperada">{'Abrir los resultados completos' if lang=='es' else 'Open the complete example outputs'} ↗</a> · <a href="{LINKS['repo']}/blob/main/ejercicios/README.md">{'Hacer los ejercicios' if lang=='es' else 'Try the exercises'} ↗</a></p></section>
<section class="section wrap" id="proyectos"><div class="section-head"><div class="eyebrow">{c['projects_label']}</div><div><h2>{c['projects_title']}</h2><p>{c['projects_intro']}</p></div></div><div class="project-grid">{cards}</div></section>
<section class="section method" id="metodo"><div class="wrap"><div class="section-head"><div class="eyebrow">{c['method_label']}</div><div><h2>{c['method_title']}</h2><p>{c['method_intro']}</p></div></div><div class="method-steps">{steps}</div><div class="prose">{paragraphs(c['method_body'])}</div></div></section>
<section class="section wrap" id="recursos"><div class="section-head"><div class="eyebrow">{c['resources_label']}</div><div><h2>{c['resources_title']}</h2><p>{c['resources_intro']}</p></div></div><div class="intro-grid"><aside class="side-note">Git · GitHub · Jupyter<br>Codespaces · Actions<br>{'Modelos de lenguaje' if lang=='es' else 'Language models'}</aside><div class="prose">{paragraphs(c['resources_body'])}</div></div><div class="resource-list">{resources}</div><p class="end-note">{c['closing']}</p></section>
<section class="section bio" id="arturo"><div class="wrap"><div class="section-head"><div class="eyebrow">{c['bio_label']}</div><h2>{c['bio_title']}</h2></div><div class="bio-grid"><aside class="bio-aside"><p class="name">Arturo<br>Sánchez Pineda</p><p class="bio-summary">{c['bio_summary']}</p><div class="profile-links"><a href="{LINKS['linkedin']}">LinkedIn ↗</a><a href="{LINKS['orcid']}">ORCID ↗</a><a href="{LINKS['profile']}">ATLAS ↗</a></div></aside><div class="prose">{paragraphs(c['bio'])}</div></div></div></section>
</main>
<footer class="wrap"><div class="footer"><div><strong>{c['footer']}</strong><br>Arturo Sánchez Pineda · Instituto de Ingeniería, Venezuela<small>{c['footer_note']}</small></div><a href="{LINKS['repo']}">{c['repo_label']} ↗</a></div><details class="credits"><summary>{c['credits_title']}</summary><p>{c['credits']}</p></details></footer>
</body></html>'''

def export_text(c):
    """Provide the complete long version as editable Markdown too."""
    import re
    def plain(s):
        s=re.sub(r'<a href="([^"]+)">(.*?)</a>',r'[\2](\1)',s)
        s=s.replace('<strong>','**').replace('</strong>','**').replace('<br>',' ')
        return re.sub('<[^>]+>','',s)
    sections=[f'# {c["title"]}',c['event'],f'**{c["takeaway_title"]}**',c['takeaway_text'], '\n\n'.join(map(plain,c['intro']))]
    for p in c['projects']:
        sections += [f'## {p["title"]}',p['text'],p['detail'],' · '.join(f'[{label}]({LINKS[key]})' for label,key in p['links'])]
    sections += [f'## {plain(c["method_title"])}','\n\n'.join(map(plain,c['method_body'])),f'## {plain(c["resources_title"])}','\n\n'.join(map(plain,c['resources_body'])),c['closing'], '## Arturo Sánchez Pineda','\n\n'.join(map(plain,c['bio']))]
    return '\n\n'.join(sections)+'\n'

if __name__ == '__main__':
    for c in (ES,EN):
        (ROOT/c['filename']).write_text(render(c),encoding='utf-8')
        (ROOT/'content'/f'long-version-{c["lang"]}.md').write_text(export_text(c),encoding='utf-8')
    print('Generated index.html, en.html and both long-form Markdown editions.')
