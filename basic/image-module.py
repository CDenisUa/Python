import cairosvg
from PIL import Image
import webbrowser
import os

svg_path = os.path.abspath("data/download.svg")

# webbrowser.open(f'file://{svg_path}')

image = Image.open('data/download.png')
image.show()