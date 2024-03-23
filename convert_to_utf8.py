import os    
from chardet import detect

# get file encoding type
def get_encoding_type(file):
    f = open(file, 'rb')
    rawdata = f.read()
    f.close()
    return detect(rawdata)['encoding']

# add try: except block for reliability
def encode_multiple(input_path, output_path):
    files = os.listdir(input_path)
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        name = os.path.splitext(file_name)[0]
        if file_extension == ".srt":
            try:
                file_path = os.path.join(input_path, file_name)
                out_path = os.path.join(output_path, file_name) 
                print(file_path) 
                from_codec = get_encoding_type(file_path) 
                print(from_codec)                      
                f = open(file_path, 'r', encoding=from_codec)
                w = open(out_path, 'w', encoding='utf-8')
                text = f.read() # for small files, for big use chunks
                w.write(text)
                # os.remove(srcfile) # remove old encoding file
                # os.rename(trgfile, srcfile) # rename new encoding
            except UnicodeDecodeError:
                print('Decode Error')
            except UnicodeEncodeError:
                print('Encode Error')


encode_multiple("input", "output")