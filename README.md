# Run tests
En la raiz del proyecto correr el comando:
python -m unittest discover tests  

# Instalar la libreria
Para instalar la libreria hacer un pip install . dentro de la raiz del proyecto

# Publicar la libreria en PypPi
Para que otros puedan instalar tu librería, puedes publicarla en el Python Package Index (PyPI). Esto es lo que hace que se pueda instalar con pip install mylibrary.
Primero, asegúrate de tener instalado twine y setuptools:
pip install twine setuptools

Luego, crea un archivo dist con:
python setup.py sdist bdist_wheel

Finalmente, sube tu librería:
twine upload dist/*