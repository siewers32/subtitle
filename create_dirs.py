import os

def get_videos(files):
    videos = []
    for file in files:
        file_extension = os.path.splitext(file)[1]
        if file_extension in ['.mp4', '.mkv']:
            videos.append(file)
    return videos

def get_dirs(folder_path, files):
    for f in files:
        fpath = os.path.join(folder_path, f)
        dirs = filter()
        

# def get_subs(files):
#     subs = []
#     for file in files:
#         file_extension = os.path.splitext(file)[1]
#         if file_extension in ['.srt']:
#             subs.append(file)
#     return subs

def create_dirs(folder_path, videos):
    for v in videos:
        file_extension = os.path.splitext(v)[1]
        name = os.path.splitext(v)[0]
        dir_path = os.path.join(folder_path, name)
        print(dir_path)
        os.mkdir(dir_path)        

def move_into_folders(folder_path, files):
    items = []
    for f in files:
        items.append(os.path.join(folder_path,f))
    dirs = filter(os.path.isdir, items)
    # print(list(dirs))
    for d in dirs:
        name = os.path.basename(d)
        if os.path.isfile(f"{d}.mkv"):
            os.rename(f"{d}.mkv", f"{d}/{name}.mkv")
        if os.path.isfile(f"{d}.EN.srt"):
            os.rename(f"{d}.EN.srt", f"{d}/{name}.EN.srt")
        if os.path.isfile(f"{d}.NL.srt"):
            os.rename(f"{d}.NL.srt", f"{d}/{name}.NL.srt")
       
    # for v in videos:
    #     org_file_path = os.path.join(folder_path, file_name)
    #     new_file_path = os.path.join(dir_path, file_name)

    # files = os.listdir(folder_path)
    # videos = get_videos
    # subs = filter(get_subs, files)
    # c = 0
    # for file_name in videos:
    #     file_extension = os.path.splitext(file_name)[1]
    #     name = os.path.splitext(file_name)[0]
    #     dir_path = os.path.join(folder_path, name)
    #     org_file_path = os.path.join(folder_path, file_name)
    #     new_file_path = os.path.join(dir_path, file_name)
    #     os.mkdir(dir_path)
    #     os.rename(org_file_path, new_file_path)
    
    # for file_name in subs:
    #     file_extension = os.path.splitext(file_name)[1]
    #     name = os.path.splitext(file_name)[0] 
    #     srt_file_path = os.path.join(dir_path, file_name)
    #     print(dir_path)
    #     os.rename(org_file_path, new_file_path)
        # file_path = os.path.join(folder_path, file_name)
        # out_path = os.path.join(folder_path, file_name.replace("EN","NL"))

# create_dirs('input')
folder_path = 'input'
files = os.listdir(folder_path)
# print(get_videos(files))
# print(get_subs(files))
# create_dirs(folder_path, get_videos(files))
move_into_folders(folder_path, files)