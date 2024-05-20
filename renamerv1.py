import os
import calendar

def convert_numbers_to_strings(filename):
    str = []
    for i in filename:
        if i.isnumeric():
            
            str.append(chr(int(i) + 97))
        else:
            str.append(i)
    return("".join(str))


def rename_files(folder_path, map):
    files = os.listdir(folder_path)
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        try:    
            # nr = int(name.split(' - ')[0])
            # month = calendar.month_name[nr]
            # a = 96 + nr
            # new_filename = f"{chr(a)}.{month}.{year}.pdf"
            # print(new_filename)
            new_filename = convert_numbers_to_strings(file_name)
            new_file_path = os.path.join(folder_path, new_filename)
            old_file_path = os.path.join(folder_path, file_name)        
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {file_name} to {new_filename}")
        except ValueError as v:
            print("File skipped")
        except:
            print("Something went wrong")


# Vervang 'folder_path' met het pad naar de map waarin je de bestanden wilt hernoemen
folder_path = 'input'
year = "LXVII"
rename_files(folder_path, year)


