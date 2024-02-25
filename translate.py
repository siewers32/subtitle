from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator
from modules import subtitle as s

output = "output.srt"
empty = open(output,"w")
empty.close()

w = open(output, "a")
input_file = "input.srt"
f = open("input.srt", "r")
t = ""
to_translate = f.readlines()

x = 0
chunk = 300
start = 0
end = chunk
while x <= len(to_translate):
    t = "".join(to_translate[start:end])
    translated = GoogleTranslator(source='english', target='dutch').translate(t)
    # translated = MyMemoryTranslator(source="en-GB", target="nl-NL").translate(t')

    print(translated)
    w.write(f"{translated}\n")
    start = end + 1 
    end = end + chunk
    x = x + chunk

