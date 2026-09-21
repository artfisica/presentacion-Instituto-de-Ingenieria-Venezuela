# Actualizar tu repositorio y preparar la versión citable

Esta entrega es una actualización del repositorio que ya publicaste. No ejecutes
otra vez `git init` ni añadas de nuevo el remoto. El asistente no ha escrito en
GitHub, activado opciones, conectado Zenodo ni creado etiquetas.

## 1. Aplicar el ZIP en tu clon existente

Guarda el ZIP actualizado en `~/Downloads/presentacion-Instituto-de-Ingenieria-Venezuela.zip`.
Los comandos siguientes usan la ruta del clon de las instrucciones anteriores:

```bash
cd ~/Downloads
unzip presentacion-Instituto-de-Ingenieria-Venezuela.zip -d charla-actualizacion
cd ~/Downloads/charla-instituto/presentacion-Instituto-de-Ingenieria-Venezuela
git status --short
git pull --ff-only
ditto ~/Downloads/charla-actualizacion/presentacion-Instituto-de-Ingenieria-Venezuela .
rm -f -- fuentes/DejaVuSansMono-Bold.ttf
rm -f -- fuentes/DejaVuSansMono-Oblique.ttf
rm -f -- fuentes/DejaVuSansMono-BoldOblique.ttf
```

`ditto` no elimina archivos: los tres `rm` retiran únicamente variantes Mono que ya no se usan. Si descargaste el parche pequeño, sigue [PARCHE-FUENTES.md](PARCHE-FUENTES.md). Si el navegador añade `__1_` al nombre del ZIP, renómbralo antes al nombre de los comandos.

Si tienes cambios propios sin guardar, revísalos antes de copiar archivos sobre
ellos. Si tu clon está en otra carpeta, cambia únicamente ese `cd`. El ZIP no
contiene `.git`, por lo que conserva tu historial y tu remoto.

Después, desde la raíz del clon y con tu entorno Python activado:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python web/build.py
python web/validate.py
git diff --stat
git add -A
git diff --cached --stat
git commit -m "Improve reuse, Unicode PDFs, run summaries and mobile reading"
git push
```

Los resultados generados en `resultados/` siguen ignorados. Las salidas de
referencia en `ejemplos/salida-esperada/` sí se añaden al repositorio.

## 2. Marcar el repositorio como plantilla

En tu repositorio: **Settings → General → Template repository**.

Los asistentes podrán elegir **Use this template → Create a new repository**.
La plantilla copia los archivos sin conservar el historial compartido de un
fork. Mantén **Fork** como alternativa para quienes quieran seguir tus cambios.
Las políticas de Actions de cada cuenta u organización siguen aplicándose.

[Documentación oficial de plantillas](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).

## 3. Descripción y descubrimiento

En la página principal del repositorio, abre el engranaje de **About** y establece:

- **Description:** Ejercicios de Python y GitHub Actions para investigar, enseñar y publicar resultados reproducibles. Materiales ES/EN.
- **Website:** https://artfisica.github.io/presentacion-Instituto-de-Ingenieria-Venezuela/
- **Topics:** `open-science`, `reproducibility`, `github-actions`, `education`, `venezuela`, `python`.

Estas opciones no pueden aplicarse desde un ZIP; las configuras tú.

## 4. Conectar Zenodo y publicar v1.0

1. Revisa `LICENSE`, `THIRD_PARTY.md` y `CITATION.cff`. Los materiales de terceros
   conservan sus créditos y no pasan a ser propiedad de Arturo.
2. En tu cuenta de **Zenodo**, conecta tu cuenta de GitHub si aún no está vinculada.
   Desde el menú del perfil, abre **GitHub**, pulsa **Sync now**, busca este
   repositorio y activa su integración. Esta es tu conexión con Zenodo, no una
   autorización para que el asistente acceda a GitHub.
3. Añade a `CITATION.cff` `version: "1.0"` y `date-released: AAAA-MM-DD` usando la
   fecha real de publicación. Guarda y sube ese cambio:

```bash
git add CITATION.cff
git commit -m "Prepare citation metadata for v1.0"
git push
git tag -a v1.0 -m "First citable release of the teaching materials"
git push origin v1.0
```

4. En GitHub, abre **Releases → Draft a new release**, selecciona la etiqueta
   **v1.0**, describe el contenido y pulsa **Publish release**. Una etiqueta por
   sí sola no sustituye la publicación de una release para este flujo.
5. Espera a que Zenodo archive la release. Abre el registro y verifica autoría,
   título y licencias. Copia el **DOI real** de la versión al campo `doi` de
   `CITATION.cff` en la rama principal y añade el enlace al README. No muevas ni
   sobrescribas la etiqueta `v1.0`: el archivo publicado conserva esa versión.

No hay DOI ni release creados por esta entrega. La metadata del paquete no
declara una fecha de publicación o una versión archivada que todavía no existe.

Fuentes: [habilitar un repositorio en Zenodo](https://help.zenodo.org/docs/github/enable-repository/),
[CITATION.cff](https://help.zenodo.org/docs/github/describe-software/citation-file/) y
[archivar una release](https://help.zenodo.org/docs/github/archive-software/github-upload/).

## 5. Comprobar la experiencia del asistente

Después del push, entra en cada ejecución de Actions. Los tres ejercicios
incluyen un resumen visible y un enlace al artefacto. El gráfico y el análisis
deben mostrar el promedio inicial 25; el PDF debe indicar su número de páginas.
En el móvil, comprueba los cuatro enlaces de navegación y el modo oscuro del
sistema. La sección «Qué vas a producir en diez minutos» muestra ejemplos reales.

La configuración y los scripts están preparados y probados localmente. La
ejecución de esta actualización en GitHub y la revisión visual en tu teléfono
quedan pendientes de tu push.
