'''
	Introduccion:
	Este programa usa el programa tesseract y la librería pytesseract
	para extraer el texto de una imagen y copiarlo en el portapapeles
	e imprimirlo en la consola.

	Instalacion de entorno virtual
- Usar gestor de paquete Anaconda o Miniconda para descargar pytesseract
	
- Instalar por anaconda:
	https://anaconda.org/conda-forge/tesseract
	https://anaconda.org/jim-hart/pytesseract (Version con todos los idiomas)

- Instalacion por apt-get (No utilizado en este script):
	$sudo apt-get install tesseract-ocr
	$sudo apt-get install tesseract-ocr-spa

- Listar lenguajes disponibles:
    tesseract --list-langs

- Usar where tesseract (Windows) o where tesseract (GNU/Linux)
  para determinar ubicacion del programa
'''


import pyperclip
from PIL import Image
import pytesseract

# Ubicacion del programa tesseract
pytesseract.pytesseract.tesseract_cmd = r'/home/luis/miniconda3/envs/tesseract/bin/tesseract'

receta = 'lentejas.png'

pyperclip.copy(pytesseract.image_to_string(Image.open(receta), lang='spa'))
print(pyperclip.paste())
