import os
from modules import subtitle as s

def walk_folder(folder_path):
    files = os.listdir(folder_path)
    c = 0
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        if file_extension == ".srt":
            org_path = os.path.join(folder_path, file_name)
            replace_path = os.path.join(folder_path, file_name.replace("EN", "XX"))
            out_path = os.path.join(folder_path, file_name.replace("XX", "NL"))
            # to_replace(org_path, replace_path)
            try:
                s.do_translate('english', 'dutch', replace_path, out_path)
            except: 
                print(f"no go with {org_path}")

def to_replace(input, output):
    w = open(output, "wt")
    
    to_replace = [
        '<font size="36">',
        '</font>',
        '<c.green>',
        '<c.cyan>',
        '<c.yellow>',
        '<c.color008000>',
        '<font face="Cosmos Light" size="68">',
        '<i>',
        '</i>',
       '<font face="Monotype Corsiva" color=#D900D9">'
    ]
    for f in open(input, "r"):    
        new_line = f
        for r in to_replace:
            new_line = new_line.replace(r,"")
        w.write(new_line)
        # new_lines.append(new_line)         

folder_path = 'input'
# walk_folder(folder_path)
to_replace("input.srt", "output.srt")