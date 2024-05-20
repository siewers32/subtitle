import os

def replace_in_files(folder_path):
    files = os.listdir(folder_path)
    c = 0
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        if file_extension in [".srt"]:
            file_path = os.path.join(folder_path, file_name)
            out_path = os.path.join(folder_path, file_name.replace("EN","XX"))

            w = open(out_path,"w")
            to_replace = [
                '<font size="36">',
                '</font>',
                '<c.green>',
                '<c.cyan>',
                '<c.yellow>',
                '<c.color008000>',
                '<font color="#808080">',
                '<font color="#ffff00">',
                '<font face="sans-serif" size="35">',
                '<i>',
                '</i>'
            ]

            for f in open(file_path, "r"):
                new_line = f
                for r in to_replace:
                    new_line = new_line.replace(r,"")
                w.write(new_line)
                # new_lines.append(new_line)

replace_in_files("input") 

