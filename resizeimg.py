from PIL import Image
import os

folder_path = 'input'
output = 'output'

files = os.listdir(folder_path)

for image in files:
    file_extension = os.path.splitext(image)[1]
    fname = os.path.splitext(image)[0] 
    print(fname)  
    if file_extension == ".jpg":
        file_path = os.path.join(folder_path, image)
        new_file_path = os.path.join(output, fname)
        im = Image.open(file_path)
        im.thumbnail((4000, 5000))
        print(new_file_path)
        im.save(f"{new_file_path}v2.jpg")
        print(im.size) # Output: (400, 350)