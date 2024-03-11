# import os
# from shutil import copytree, ignore_patterns
# import logging


# def check_type(file_name):
#     file_extension = os.path.splitext(file_name)[1]
#     name = os.path.splitext(file_name)[0]
#     if file_extension in [".txt", ".srt", ".mkv", ".mp4"] or os.path.isdir(file_name):
#         # print(file_name)
#         return False
#     else:
#         return True

# def log(path, names):
#     # f = open("log.txt", "a")
#     a = filter(check_type, names)
#     print(list(a))
#     # print(names)
#     return list(filter(check_type, names))
    
# source = os.path.join('input', "")
# destination = os.path.join('output', "test")

# try:
#     copytree(source, destination, ignore=ignore_patterns('')), dirs_exist_ok=True)
# except FileExistsError as e:
#     print(e)

# # copytree(source, destination, ignore=ignore_patterns('*.pyc', '*.srt'))



import os
import shutil


def copytree_with_ignore(src, dst):
    # Create the destination directory if it doesn't exist
    # os.makedirs(dst, exist_ok=True)

    # Use shutil.copytree with the custom ignore function
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except FileExistsError as e:
        print(e)

if __name__ == "__main__":
    source_directory = "input"
    destination_directory = "output"

    copytree_with_ignore(source_directory, destination_directory)


