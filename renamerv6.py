import os
import calendar

def convert_number_to_letters(n):
    txt = []
    number = int(n.strip(" "))
    letters = addzero(number)
    for i in letters:
        txt.append(chr(int(i) + 97))
    return "".join(txt)



def addzero(a):
    if a < 100:
        return f"0{str(a)}"
    else:
        return str(a)

def rename_files(folder_path, map):
    files = os.listdir(folder_path)
    counter = 97
    txt = [] 
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        # try:
        if file_extension in ['.pdf', '.cbr', '.txt']:                   
            letters = convert_number_to_letters(name[8:11])
            print(letters)

            # month = calendar.month_name[nr]
            # a = 96 + nr
            new_filename = file_name.replace(name[8:11], letters + " ")
            new_file_path = os.path.join(folder_path, new_filename)
            old_file_path = os.path.join(folder_path, file_name)        
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {file_name} to {new_filename}")
        # except ValueError as v:
            # print("File skipped")
        # except:
            # print("Something went wrong")
# 

# Vervang 'folder_path' met het pad naar de map waarin je de bestanden wilt hernoemen
folder_path = 'input'
year = "LXVII"
rename_files(folder_path, year)

