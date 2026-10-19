# User delivery boundary — mandatory

Arturo's explicit, permanent instruction: agents must NEVER write to, push to,
publish to, or modify his GitHub repositories or their settings. Deliver local
files, a ZIP and instructions. Arturo alone performs GitHub actions.
Do not suggest connecting GitHub to get around this delivery boundary.

# This project

Static bilingual HTML for an online talk at Instituto de Ingeniería, Venezuela.
Spanish: web/index.html. English: web/en.html. Presentation comes before biography.
Edit web/content/site.py and run python3 web/build.py (standard library only).
All imagery and fonts are local. No tracking, external JS or runtime dependencies.
Preserve accurate distinctions: LAGO is a proposal; the Nobel went to Englert
and Higgs; engineering studies at ULA must not become an unsupported second degree.
The talk is confirmed for Wednesday 21 October 2026 at 09:00 America/Caracas
(UTC−4, 13:00 UTC). That data lives only in EVENT in web/content/site.py and
feeds the hero chip, footer, long versions and the .ics files. The connection is the
FORMATEC virtual-rooms page (EVENT['link']); the specific room (EVENT['room'],
EVENT['room_link']) is still pending: never invent it. Never hand-edit
web/index.html or web/en.html;
pages.yml regenerates both from site.py on every deploy.

The root is also the participant repository. Keep datos/, ejemplos/, imagenes/,
scripts/ and ejercicios/ easy to navigate. Three teaching workflows generate
artifacts only; only pages.yml deploys the website, on Arturo's repository.
