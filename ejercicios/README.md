# Tres pequeños cambios, tres resultados

Puedes hacerlo desde el navegador o desde tu ordenador. Para editar y ejecutar Actions necesitas **tu propia copia**, creada con **Use this template** si está habilitado, o con **Fork** si quieres conservar el vínculo con el proyecto original. Clonar permite descargar y trabajar localmente; no te da permisos para subir cambios al repositorio de Arturo.

## 1. Cambia un dato y calcula

1. Abre `datos/mediciones.csv`.
2. Cambia el primer valor de **24** a **30** y guarda el cambio con un commit.
3. En **Actions → 01 - Analizar datos**, abre la ejecución que se ha iniciado.
4. Mira el resumen de la ejecución: los números aparecen allí directamente. Puedes descargar también **analisis** desde su enlace o desde **Artifacts**.
5. El promedio debe pasar de **25** a **26**, el mínimo sigue en **23** y el máximo pasa a **30**.

En local: `python scripts/analizar.py`. El archivo CSV utiliza punto para los decimales; sus datos son ficticios.

## 2. Mira el cambio en un gráfico

El mismo commit del CSV inicia **02 - Crear grafico**. Descarga **grafico** desde esa ejecución y abre `grafico.png`.

Ahora modifica el título o el color en `scripts/graficar.py`. Al guardar el cambio, el gráfico se vuelve a producir. No hace falta redibujarlo manualmente.

En local: `python scripts/graficar.py`.

## 3. Del Markdown al PDF

1. Abre `ejemplos/informe.md`: cambia el título, escribe tu nombre y añade una explicación.
2. Guarda el cambio. En **Actions → 03 - Crear PDF**, verás «Tu PDF está listo» con el número de páginas; descarga **documento-pdf** para abrir `informe.pdf`.
3. Sube otra foto a `imagenes/actividad-atlas.jpg`, conservando ese nombre, y guarda el cambio. **Aunque no cambies el Markdown, se generará un nuevo PDF.**
4. Si prefieres otro nombre, modifica también la ruta de la imagen en el Markdown. Es relativa a `ejemplos/informe.md`: por ejemplo, `../imagenes/mi-foto.png`.

En local: `python scripts/crear_pdf.py`.

El ejemplo admite títulos con `#`, `##` y `###`, párrafos, listas con `-`, **negrita**, *cursiva*, enlaces y una imagen por línea. Usa PNG o JPG. El convertidor es deliberadamente pequeño; no admite tablas, HTML ni bloques de código. Puedes ampliarlo después o sustituirlo por otra herramienta conservando el mismo flujo.

## Repetir sin cambiar archivos

En **Actions**, selecciona cualquiera de los tres ejercicios, pulsa **Run workflow** y elige la rama. La opción aparece cuando el flujo existe en la rama predeterminada. Si acabas de hacer un fork, entra primero en Actions y habilita los flujos de tu copia si GitHub lo solicita.

Los resultados se descargan desde la ejecución: no se añaden automáticamente al historial de Git. Cada ejecución corresponde a un commit, de modo que puedes identificar qué versión de los archivos produjo el resultado. Los artefactos se conservan durante 14 días.

## Tu primer prototipo

Elige una pregunta de tu tesis, clase o comunidad. Sustituye los datos, adapta el script y explica la fuente y las unidades en `NOTAS.md`. Documenta qué concluyes y qué no puedes concluir. Puedes pedir ayuda a un modelo de lenguaje para entender o modificar el código, y comprobar tú cada cambio ejecutándolo.

## English

The same repository contains all three exercises. Fork it to edit and run Actions in your own account; clone it for local work. Change the first CSV value from 24 to 30: the mean should change from 25 to 26. Download the analysis and chart from their workflow runs. Edit `ejemplos/informe.md` or replace `imagenes/actividad-atlas.jpg`: the PDF workflow rebuilds the document on either change. Run each workflow manually with **Run workflow**, or use the three Python commands above locally.

El PDF incluye fuentes Unicode locales: `Propuesta → simulación`, `CO₂`, letras griegas y subíndices se conservan. Si una fuente no incluye un carácter, el script indica cuál y en qué línea, en lugar de sustituirlo silenciosamente.
