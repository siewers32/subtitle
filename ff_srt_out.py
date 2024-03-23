import os
import ffmpeg
import sys

def ff_files(folder_path):
    files = os.listdir(folder_path)
    c = 0
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        file_path = os.path.join(folder_path, file_name)
        out_path = os.path.join(folder_path, f"{name}.EN.srt")
        try:
            if file_extension in [".mkv", ".mp4"]:
                stream = ffmpeg.input(file_path)
                stream = ffmpeg.output(stream, out_path)
                ffmpeg.run(stream)
        except ffmpeg.Error as e:
            print(e.stderr, file=sys.stderr)
            sys.exit(1)
        # c = c + 1
        # try:
        #     # new_filename = file_name.replace(" 720p WEB-DL H264 BONE", "")
        #     new_filename = f"{name}.mp4"
        #     old_file_path = os.path.join(folder_path, file_name)
        #     new_file_path = os.path.join(folder_path, new_filename)     
        #     os.rename(old_file_path, new_file_path)
        #     print(f"Renamed {file_name} to {new_filename}")
        # except:
        #     print("no file")

# Vervang 'folder_path' met het pad naar de map waarin je de bestanden wilt hernoemen
folder_path = 'input'
ff_files(folder_path)