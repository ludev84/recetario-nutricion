# Image-OCR-Scan

Este script usa el programa tesseract y la librería pytesseract para extraer el texto de una imagen e imprimirlo en la consola.

## Instalar por anaconda (recomendado):

Es recomendable usar un gestor de paquete como anaconda o miniconda para descargar los programas en un entorno virtual.

* https://anaconda.org/conda-forge/tesseract

* https://anaconda.org/conda-forge/pytesseract

## Instalar de manera global (no recomendado)

* sudo apt-get install tesseract-ocr.

* sudo apt-get install tesseract-ocr-spa

* pip install pytesseract

## Listar lenguajes disponibles:
tesseract --list-langs

Usar where tesseract (Windows) o where tesseract (GNU/Linux) para determinar ubicacion del programa