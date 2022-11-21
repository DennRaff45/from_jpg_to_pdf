from PIL import Image
import os
import sys

image_folder = input("name of folder: ")
output_folder = input('name of new folder: ')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.pdf')

# print(image_folder, output_folder)
