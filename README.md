# De los datos abiertos al conocimiento compartido

**Computación, automatización e inteligencia artificial para investigar y aprender.**

Charla en línea de Arturo Rodolfo Sánchez Pineda para el Instituto de Ingeniería, Venezuela.

**Este mismo repositorio es tu punto de partida.** Puedes clonarlo, ejecutar los ejemplos y adaptarlos a tu tesis, clase o proyecto. Si puedes y quieres, llega a la charla con tu cuenta de GitHub creada.

[Presentación en español](https://artfisica.github.io/presentacion-Instituto-de-Ingenieria-Venezuela/) · [English](https://artfisica.github.io/presentacion-Instituto-de-Ingenieria-Venezuela/en.html) · [Guía de ejercicios](ejercicios/README.md)

## Qué vas a aprender

- Organizar datos, código, notas e imágenes para que otra persona pueda comprender y repetir tu trabajo.
- Usar Git y GitHub para conservar versiones, explicar cambios y colaborar.
- Convertir tareas repetidas en scripts: analizar datos, dibujar un gráfico y preparar un informe.
- Automatizar esas tareas para obtener nuevos resultados cuando cambien los archivos.
- Utilizar modelos de lenguaje para entender y adaptar código, manteniendo la revisión de los resultados en tus manos.

## Carpetas para empezar

| Carpeta | Qué encontrarás |
|---|---|
| `datos/` | Un CSV pequeño con datos ficticios. |
| `ejemplos/` | Un informe Markdown que puedes editar. |
| `imagenes/` | La imagen utilizada en ese informe. |
| `scripts/` | Tres programas Python: análisis, gráfico y PDF. |
| `ejercicios/` | Pasos guiados y notas para tu propio proyecto. |
| `resultados/` | Los archivos generados al ejecutar los programas. |
| `web/` | La página bilingüe de la presentación. |

Las automatizaciones están en `.github/workflows/`. Puedes empezar editando los ejemplos sin cambiar su configuración.

## Ejercicios

| Cambias… | Se ejecuta… | Obtienes… |
|---|---|---|
| `datos/mediciones.csv` | **01 - Analizar datos** | Resumen JSON e informe HTML. |
| El mismo CSV o el script del gráfico | **02 - Crear grafico** | Una imagen PNG. |
| `ejemplos/informe.md` o una imagen en `imagenes/` | **03 - Crear PDF** | Un PDF actualizado con texto e imágenes. |

También puedes ejecutar cualquiera desde **Actions → nombre del ejercicio → Run workflow**. Descarga su resultado desde **Artifacts**, dentro de la ejecución terminada. Se conserva durante 14 días. Estas tres acciones generan archivos descargables y no crean commits.

**[Empieza por la guía de los tres ejercicios](ejercicios/README.md).** El primer cambio consiste en sustituir un 24 por un 30 y comprobar que el promedio cambia de 25 a 26.

## Desde el navegador

Haz **Fork** de este repositorio para tener tu copia. Entra en **Actions** y habilita sus flujos si GitHub te lo pide. Edita un dato o el Markdown y guarda el cambio: los ejercicios correspondientes se ejecutan automáticamente.

No necesitas instalar Python para esta vía. Una cuenta de GitHub te permite tener tu copia; revisa las condiciones y cuotas de los servicios que utilices. La publicación de la web está separada de los tres ejercicios y solo se activa en el repositorio de Arturo.

## Desde tu ordenador

Necesitas Git y Python 3.10 o posterior. Las acciones utilizan Python 3.12.

```bash
git clone https://github.com/artfisica/presentacion-Instituto-de-Ingenieria-Venezuela.git
cd presentacion-Instituto-de-Ingenieria-Venezuela
python3 scripts/analizar.py
```

Este primer análisis utiliza solo Python, sin paquetes adicionales. Para el gráfico y el PDF:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/graficar.py
python scripts/crear_pdf.py
```

Abre los archivos de `resultados/`. En Windows puedes crear el entorno con `py -3 -m venv .venv` y activarlo en PowerShell con `.venv/Scripts/Activate.ps1`.

Clonar descarga el material y permite trabajar localmente. Para subir tus cambios a GitHub, utiliza tu propio fork como repositorio remoto. También puedes abrir un Codespace de tu copia y utilizar los mismos comandos en su terminal, dentro de las cuotas de tu cuenta.

## Del ejemplo a tu investigación

Sustituye los datos, formula una pregunta, adapta el script y documenta tus fuentes, unidades y decisiones en `ejercicios/NOTAS.md`. Si utilizas un modelo de lenguaje, pídele una explicación del cambio y verifica el resultado. Una automatización repetible facilita la revisión; la interpretación científica sigue siendo tu responsabilidad.

## Para Arturo

[PUBLICAR.md](PUBLICAR.md) contiene los comandos exactos para subir este paquete al repositorio existente y activar GitHub Pages. La página se puede revisar localmente abriendo `web/index.html`. El anuncio ampliado está en `telegram-es.md`.

Las versiones extensas están en `web/content/long-version-es.md` y `web/content/long-version-en.md`. Créditos y referencias en [SOURCES.md](SOURCES.md). Para editar la web, cambia `web/content/site.py` y ejecuta `python3 web/build.py`.

## English quick start

This same repository contains the presentation and three practical exercises: analyse a CSV, create a PNG chart and build a PDF from Markdown and local images. Clone for local use, or fork to edit and run Actions in your own account. Start with `python3 scripts/analizar.py`; install `requirements.txt` in a virtual environment for the chart and PDF. Instructions in [ejercicios/README.md](ejercicios/README.md) include an English summary. Changing the Markdown **or an image** triggers a new PDF build. Download outputs from the completed workflow's **Artifacts** section. The teaching workflows never push commits or publish a website.
