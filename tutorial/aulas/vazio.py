from PIL import Image
import os

dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, 'data/1.png')

img1 = Image.open(file_path)
img1.convert(mode='L').save(dir_path + '/data/1_gray.png')
