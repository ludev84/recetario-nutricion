# Recipe-OCR-Scan
El objetivo de este repositorio es transcribir una serie recetas contenidas en imágenes y crear un recetario editable.

Para este propósito se creó un script que imprime en la terminal el texto contenido en todas las imágenes dentro de un directorio

## Configurar entorno virtual

### Instalar por anaconda (recomendado):

Es recomendable usar un gestor de paquete como anaconda o miniconda para descargar los programas en un entorno virtual.

* https://anaconda.org/conda-forge/tesseract

* https://anaconda.org/conda-forge/pytesseract

### Instalar de manera global (no recomendado)

* sudo apt-get install tesseract-ocr.

* sudo apt-get install tesseract-ocr-spa

* pip install pytesseract

### Listar lenguajes disponibles:
tesseract --list-langs

Usar where tesseract (Windows) o where tesseract (GNU/Linux) para determinar ubicacion del programa