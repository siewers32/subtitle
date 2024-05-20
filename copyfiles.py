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


