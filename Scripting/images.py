import os
from PIL import Image, ImageFilter


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
pichachu_path = script_dir + '/Pokemon/pickachu.png'
astro_path = script_dir + '/Pokemon/astro.jpg'

img = Image.open(pichachu_path)
astro_img = Image.open(astro_path)

grey_img = img.convert('L')

img = img.convert('RGB')
blur_img = img.filter(ImageFilter.BLUR)
smooth_img = img.filter(ImageFilter.SMOOTH)
sharp_img = img.filter(ImageFilter.SHARPEN)
resize_img = img.resize((300,300))
rotated_img = img.rotate(90)

grey_img.save("grey.png","png")
blur_img.save("blur.png","png")
smooth_img.save("smooth.png","png")
rotated_img.save("rotate.png","png")
resize_img.save("resize.png","png")

box = (100, 100, 200, 200)
crop_img = resize_img.crop(box)
crop_img.save("crop.png","png")

print(astro_img.size)

astro_img.thumbnail((400,200))
astro_img.save('thumbnail.jpg')

# rotated_img.show()