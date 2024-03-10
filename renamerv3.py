import os
import calendar

def getMonthLetter(m):
    for a in range(1,13):
        if calendar.month_name[a] == m:
            return chr(96 + a)

def rename_files(folder_path, map, special):
    files = os.listdir(folder_path)
    counter = 0
    for file_name in files:
        counter = counter + 1
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        name = name.replace("- ", "")
        print(name)
        try:  
            if special:
                # s = name.split(" ")[2]
                s = "Guitarist"
                new_filename = f"Special.{year}.{chr(96 + counter)}.{s}.pdf" 
                print(new_filename)
            else: 
                parts = name.split(" ")
                a = getMonthLetter(parts[3])
                new_filename = f"{a}.{parts[3]}.{year}.pdf"
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
year = "X"
special = False
rename_files(folder_path, year, special)

