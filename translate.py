
from modules import subtitle as s


# def do_translate(from_lang, to_lang, from_file, to_file):

#     empty = open(to_file,"w")
#     empty.close()

#     w = open(to_file, "a")
#     f = open(from_file, "r")
#     t = ""
#     to_translate = f.readlines()
#     x = 0
#     chunk = 200
#     start = 0
#     end = chunk
#     while x <= len(to_translate):
#         # input("continue... y")
#         t = "".join(to_translate[start:end])
#         translated = GoogleTranslator(source=from_lang, target=to_lang).translate(t)
#         # translated = MyMemoryTranslator(source="en-GB", target="nl-NL").translate(t')

#         print(translated)
#         w.write(f"{translated}\n")
#         start = end + 1 
#         end = end + chunk
#         x = x + chunk

s.do_translate('english', 'dutch', 'input.srt', 'output.srt')