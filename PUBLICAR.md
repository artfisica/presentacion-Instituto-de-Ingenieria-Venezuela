# Primera publicación - instrucciones originales

**El repositorio ya está publicado. Para esta entrega utiliza [ACTUALIZAR.md](ACTUALIZAR.md), sin repetir `git init` ni configurar otra vez el remoto.**

El destino es tu repositorio existente:

<https://github.com/artfisica/presentacion-Instituto-de-Ingenieria-Venezuela>

No se ha realizado ningún push ni cambio en GitHub. Tú ejecutas los pasos siguientes. Se asume que el repositorio sigue vacío, como en tu captura y según tu confirmación de que no has subido nada.

## 1. Descargar y descomprimir en tu Mac

Guarda el ZIP actualizado en **Descargas**, con el nombre exacto `presentacion-Instituto-de-Ingenieria-Venezuela.zip`. Utiliza esta versión, que incluye los ejercicios en la raíz del mismo repositorio.

```bash
cd ~/Downloads
unzip presentacion-Instituto-de-Ingenieria-Venezuela.zip -d charla-instituto
cd charla-instituto/presentacion-Instituto-de-Ingenieria-Venezuela
open web/index.html
```

Si el navegador añadió `(1)` al nombre descargado, renómbralo antes al nombre indicado. `charla-instituto` es una carpeta nueva para esta entrega, de modo que no se mezcle con el paquete anterior.

## 2. Activar Pages

Abre <https://github.com/artfisica/presentacion-Instituto-de-Ingenieria-Venezuela/settings/pages>.

En **Build and deployment → Source**, elige **GitHub Actions**.

## 3. Hacer el primer push

Desde la misma carpeta en la terminal:

```bash
git init -b main
git add .
git status --short
git commit -m "Add bilingual presentation and three practical exercises"
git remote add origin https://github.com/artfisica/presentacion-Instituto-de-Ingenieria-Venezuela.git
git push -u origin main
```

Se sube **el contenido descomprimido**, no el ZIP como un único archivo. La carpeta `.github` viene incluida en el ZIP y `git add .` también la añade.

Si Git indica que el remoto ya tiene commits, no uses `--force`: trabaja sobre un clon de ese repositorio y copia allí el contenido del paquete. Esta entrega está preparada para el caso vacío confirmado.

## 4. Verificar los cuatro flujos

En <https://github.com/artfisica/presentacion-Instituto-de-Ingenieria-Venezuela/actions> aparecerán:

1. **01 - Analizar datos**: descarga `analisis`.
2. **02 - Crear grafico**: descarga `grafico`.
3. **03 - Crear PDF**: descarga `documento-pdf`.
4. **Publish static website to GitHub Pages**: publica la presentación bilingüe.

Los tres primeros son los ejercicios. El cuarto mantiene la página de la charla. Abre cada ejecución terminada para acceder a sus **Artifacts**. Si activaste Pages después del push, vuelve a ejecutar el flujo de publicación con **Run workflow**.

La web estará en:

<https://artfisica.github.io/presentacion-Instituto-de-Ingenieria-Venezuela/>

En inglés:

<https://artfisica.github.io/presentacion-Instituto-de-Ingenieria-Venezuela/en.html>

Los enlaces estarán activos cuando tu publicación termine correctamente. Compruébalos antes de compartirlos. Los flujos se han preparado y sus scripts se han probado localmente; la ejecución en tu cuenta de GitHub queda pendiente de tu primer push.

## 5. Compartir con los asistentes

Para leer la presentación, comparte la URL de Pages. Para los ejercicios, comparte el repositorio anterior. Pueden hacer **Fork** para editar y ejecutar Actions en su cuenta, o clonar para trabajar localmente:

```bash
git clone https://github.com/artfisica/presentacion-Instituto-de-Ingenieria-Venezuela.git
cd presentacion-Instituto-de-Ingenieria-Venezuela
python3 scripts/analizar.py
```

No necesitan otro repositorio de ejercicios. La página enlaza a la sección **Ejercicios** de este mismo repositorio.

## Actualizar más adelante

```bash
python3 web/build.py
python3 web/validate.py
git add .
git commit -m "Update presentation and exercises"
git push
```

Para el PDF, basta con cambiar `ejemplos/informe.md` o una imagen en `imagenes/`, crear el commit y hacer push. La acción lo regenera y lo ofrece para descargar; no escribe resultados en el repositorio.

Documentación oficial: [descarga de artefactos](https://docs.github.com/en/actions/managing-workflow-runs/downloading-workflow-artifacts) y [GitHub Pages con Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
