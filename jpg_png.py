from PIL import Image
import sys
import os

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir(folder):
    img = Image.open(f'{folder}{file}')
    outfile = os.path.splitext(file)[0]
    img.save(f'{new_folder}{outfile}.png', 'png')
    print('converted!')


img = Image.open('./pokemon/pikachu.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('crop.png', 'png')
