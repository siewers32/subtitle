from datetime import datetime, timedelta 
import time
def strtotime(s):
    dt = datetime.strptime(s, '%H:%M:%S,%f').time()

def diff(t, td):
    # oorspronkelijke tijd
    # hours, minutes, seconds optellen bij oorspronkelijke tijd
    t = datetime.strptime(t, '%H:%M:%S,%f')
    # print(t + td).strftime("%H:%M:%S,%f")
    # print((t + td).strftime("%H:%M:%S,%f"))
    return (t + td).strftime("%H:%M:%S,%f")

def skiplines(n):
    if n > 0:
        return n - 1
    else:
        return 0

def addtime(timetekst, timediff):
    timestamps = timetekst.split(" --> ") 
    begin = diff(timestamps[0],timediff)
    end = diff(timestamps[1].strip('\n'),timediff)
    # w.write(f"{begin[:-3]} --> {end[:-3]}\n") # nieuwe timestamp
    return [begin[:-3], end[:-3]]

def get_framenumber(f, l):
    fnr = 0
    try:
        fnr = int(f.strip(" ")) + l
    except ValueError as e:
        print(e)
    except e:
        print(e)
    return str(fnr)
   



def adjust_frame(frametekst, framediff):
    for i in range(0, len(frametekst)):
        # eerste regel
        frame = f"{get_framenumber(lines[i], framediff)}"
        # tweede regel
        newtime = addtime(frametekst[i+1], td)
        #new_sub = f"{new_sub}{newtime[0]} --> {newtime[1]}\n"
        return f"{frame}\n{newtime}\n{get_translation(i)}"


def get_translation(frametekst, start):
    translation = ""
    for i in range(start, len(frametekst)):
        translation = f"{translation}{frametekst[i]}"
    return translation




def convert(lines, td, f, l):
    skip = 0
    new_sub = ""
    for i in range(0, len(lines)):
        skip = skiplines(skip)
        if lines[i] in ['\n', '\r\n'] or i == 0:
            if i == 0: # eerste regel fragmentnummer
                new_sub = f"{get_framenumber(lines[i], l)}\n"
                i = i + 1
                timestamps = lines[i].split(" --> ") 
                newtime = addtime(timestamps, td)
                new_sub = f"{new_sub}{newtime[0]} --> {newtime[1]}\n"
                get_translation(i)
            else:
                new_sub = f"new_sub\n"  # lege regel toevoegen
            # lege regel voorafgaand aan fragment
            skip = 2 # twee regels voor fragmentnummer en timestamps
            i = i + 1 # naar volgende regel
            try:
                # framenummer
                new_sub = f"{new_sub}{str(fnr + l)}\n"
                # next line
                #timestamps
                timestamps = lines[i].split(" --> ") 
                if fnr >= f:
                    # do the math...
                    newtime = addtime(timestamps, td)
                    new_sub = f"{new_sub}{newtime[0]} --> {newtime[1]}\n"
                else:
                    new_sub = f"{new_sub}{timestamps[0]} --> {timestamps[1]}"
            except StopIteration as e:
                print(e)
            except ValueError as e:
                print(e)
            except Exception as e: # work on python 3.x
                print(e)

        else:
            # w.write(lines[i]) # overige regels
            new_sub = new_sub + lines[i];
    return new_sub

def get_fragment(start, tekst):
    for i in range(start, len(tekst)):
        if tekst[i] in ['\n', '\r\n']:
            return tekst[start:i - start]

def get_fragment_linenumbers(lines):
    fs = [0]
    fragments = []
    for i in range(0, len(lines)):
        if lines[i] in ["\n","\r\n"]:
            fs.append(i+1)
    for x in range(0, len(fs)):
        try:
            fragments.append([fs[x], fs[x+1]])
        except IndexError as e:
            fragments.append([fs[x], len(lines)])
            pass
        except Exception as e:
            print(e)
    return fragments




# 1799
# 01:42:56,103 --> 01:43:00,165

# f = 1 # fragmentnummer
# l = 0 # regelnummer
td = timedelta(hours=0, minutes=0, seconds=14) # timediff

r = open("test.txt", "r") # subtitle file
lines = r.readlines()
# print(lines)

# i = 0
# while i < len(lines):
#         nol = get_number_of_lines_for_frame(i,lines)

#         if lines[i] in ['\n', '\r\n']:
#             print(get_framenumber(lines[i+1], 0))
#         elif i == 0:
#             print(get_framenumber(lines[i], 0))

# print(get_fragment(0,lines))
# print(get_fragment_start(lines))

# fragment_starts = get_fragment_start(lines)
# for i in range(0, len(fragment_starts)):
#     if len(fragment_starts) > i+1:
#         start = fragment_starts[i] + 1
#         end = fragment_starts[i+1]
#         get_fragment()
   
# for i in get_fragment_start(lines):
#     print(get_fragment(i, lines))

def create_dictionaries(lines):
    fd = {"fnr": 0, "start": "00:00:00,000", "end": "00:00:00,000", "tekst": ""}
    for i in get_fragment_linenumbers(lines):
        frame = lines[i[0]:i[1]]
        print(frame)
        timetekst = frame[1]
        time = addtime(timetekst, td)
        # for x in lines[i[0]:i[1]]:
        fd["fnr"] = int(frame[0].strip("\n"))
        fd["start"] = time[0]
        fd["end"] = time[1]
        fd["tekst"] = ''.join(frame[2:]).strip("\n\n")
        print(fd)

# convert(r,td,f, l)
# w = open("bla.srt", "w") # new file
# w.write(convert(lines,td,f, l))



create_dictionaries(lines)