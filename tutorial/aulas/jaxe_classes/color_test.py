from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os



dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, 'data/1.jpg')
with Image.open(file_path) as img:
    width, height = img.size
    pixels = img.load()

    for px in range(int(width/2)):
        for py in range(height):
            r, g, b = img.getpixel((px, py))
            red = r
            blue = 50
            green = 0
            pixels[px, py] = (red, green, blue)
    
    img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    pixels = img.load()

    for px in range(int(width/2)):
        for py in range(height):
            r, g, b = img.getpixel((px, py))
            red = r - 50
            blue = b
            green = g - 50
            pixels[px, py] = (red, green, blue) 
    
    img = img.transpose(method=Image.FLIP_LEFT_RIGHT)

    draw = ImageDraw.Draw(img)
    file_path = os.path.join(dir_path, 'data/arial.ttf')
    draw.text((100, 100), 'eae meu consagrado', fill=(255, 255, 255), font=ImageFont.truetype(file_path, 100))

    img = img.filter(ImageFilter.GaussianBlur(radius=5))

    img.show() 
    img.close()
