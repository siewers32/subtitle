import os
import calendar

def rename_files(folder_path, map):
    files = os.listdir(folder_path)
    counter = 97
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        try:    
            nr = int(name.split('-')[1])
            month = calendar.month_name[nr]
            a = 96 + nr
            new_filename = f"{chr(a)}.{month}.{year}.pdf"
            # print(new_filename)
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
year = "MMXII"
rename_files(folder_path, year)

