import os
from modules import subtitle as s

def translate_files(folder_path):
    files = os.listdir(folder_path)
    c = 0
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        if file_extension == ".srt":
            file_path = os.path.join(folder_path, file_name)
            out_path = os.path.join(folder_path, file_name.replace("EN","NL"))
            try:
                s.do_translate('english', 'dutch', file_path, out_path)
            except: 
                print("no go")
           
  
folder_path = 'input'
translate_files(folder_path)