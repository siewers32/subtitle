import os
import calendar

def counter(a):
    if a < 10:
        return f"0{str(a)}"
    else:
        return str(a)
    
def rename_files(folder_path, year):
    files = os.listdir(folder_path)
    c = 0
    for file_name in files:
        c = c + 1
        # file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        try:
            new_file = file_name.replace("2018", "XVIII")
            # new_file = new_file.replace(" 25FPS", ".EN")
            # new_filename = f"{name}.mp4"
            # new_filename = f"Luck {new_filename}"
            # parts = new_filename.split(".")
            # new_parts = []
            # for part in parts:
            #     if part != "Issue" and not part.isnumeric():
            #         new_parts.append(part)
            # new_filename = ".".join(new_parts)



            # # new_filename = f"{parts[2]}.{parts[1]}.df.pdf"
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file)     
            # os.rename(old_file_path, new_file_path)
            print(f"Renamed {file_name} to {new_file}")
        except:
            print("no file")

# Vervang 'folder_path' met het pad naar de map waarin je de bestanden wilt hernoemen
folder_path = 'input'
year = "NineteenSeventy"
rename_files(folder_path, year)


