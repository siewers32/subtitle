from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()
# imagelist is the list with all image filenames
folder_path = 'input'

files = os.listdir(folder_path)

for image in files:
    file_extension = os.path.splitext(image)[1]
    if file_extension == ".jpg":
        file_path = os.path.join(folder_path, image)
        im = Image.open(file_path)
        verh = im.size[0] / im.size[1]
        print(im.size[0], im.size[1])
        w = round(im.size[0] / 10)
        h = round(im.size[1] / 10)
        pdf.add_page(orientation = 'P', format = (w,h))
        print(w,h)        
        pdf.image(file_path,0,0,w,h)
pdf.output("output/wallpaper_buildings.pdf")


