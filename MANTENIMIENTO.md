# Mantenimiento local y publicación

## Comprobar el proyecto

Desde la raíz, con Python 3.10 o posterior:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python web/build.py
python web/validate.py
```

En Windows, activa el entorno con `.venv/Scripts/Activate.ps1`.

## Cambiar la presentación

Edita `web/content/site.py` y ejecuta `python web/build.py`. No edites los HTML
ni las versiones extensas generadas. `EVENT` determina las fechas y horas
visibles y los calendarios de ambas ediciones. `EVENT['link']` es FORMATEC;
`room` y `room_link` permanecen vacíos hasta que la organización confirme la sala.

Revisa `web/index.html` y `web/en.html` en el navegador. La validación automática
comprueba archivos locales; no comprueba que los enlaces externos respondan.

## Cambiar los ejemplos

Los tres scripts escriben en `resultados/`, que está ignorado por Git.
Las referencias de `ejemplos/salida-esperada/` son estáticas: si cambias el ejemplo
base, sigue su README para regenerar PDF, gráfico, JSON y vistas previas.
Documenta la procedencia de cada imagen en `imagenes/README.md` y `THIRD_PARTY.md`.

## Publicar los cambios

Arturo revisa y realiza todas las operaciones en GitHub. El asistente entrega
archivos locales y ZIP; no crea ramas remotas, PR, commits remotos ni despliegues.
Después de revisar el diff, Arturo puede abrir una rama, guardar los cambios
y crear el PR desde su cuenta. Al integrar cambios de `web/` en `main`,
`pages.yml` regenera, valida y publica la web exclusivamente en su repositorio.
Los tres flujos docentes solo producen artefactos descargables durante 14 días.

## Configuración y citación

La configuración de plantilla, About y Zenodo está documentada en las secciones
2–4 de [ACTUALIZAR.md](ACTUALIZAR.md). No declares DOI, versión ni fecha de
release hasta que Arturo publique y compruebe los datos reales.

[PUBLICAR.md](PUBLICAR.md), [PARCHE-FUENTES.md](PARCHE-FUENTES.md) y la sección 1
de ACTUALIZAR describen entregas anteriores; no repitas esas migraciones para
un cambio normal. [fuentes/README.md](fuentes/README.md) conserva el procedimiento
para mantener los subconjuntos de fuentes PDF.
