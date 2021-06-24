# Recipe-OCR-Scan
El objetivo de este repositorio es transcribir una serie recetas contenidas en imágenes y crear un recetario editable.

Para este propósito se creó un script que imprime en la terminal el texto contenido en todas las imágenes dentro de un directorio

## Configurar entorno virtual

### Instalación con Miniconda (recomendado):

Es recomendable usar un gestor de paquete como anaconda o miniconda para descargar los programas en un entorno virtual. Instalar el programa [tesseract](https://anaconda.org/conda-forge/tesseract) y la librería de Python [pytesseract](https://anaconda.org/conda-forge/pytesseract).


```$conda install -c conda-forge tesseract```

```$conda install -c conda-forge pytesseract```

### Instalar de manera global (no recomendado)

```$sudo apt-get install tesseract-ocr```

```$sudo apt-get install tesseract-ocr-spa```

```$pip install pytesseract```

### Listar lenguajes disponibles:

```tesseract --list-langs```

Usar `where tesseract` (Windows) o `which tesseract` (GNU/Linux) para determinar ubicacion del programa.