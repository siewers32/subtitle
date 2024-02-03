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

def convert(r, td, f, l):
    skiplines = 0
    new_sub = ""
    lines = r.readlines()
    for i in range(0, len(lines)):
        if skiplines > 0 :
            #pass
            skiplines = skiplines-1
        else :
            skiplines = 0
            line = lines[i]
            if line in ['\n', '\r\n']:
                skiplines = 2
                # Eerste regel is regelnummer
                # w.write(line) # lege regel
                new_sub = new_sub + line
                i = i + 1
                if(i+1 < len(lines)):
                    try:
                        fnr = int(lines[i].strip(" "))
                        w.write(str(fnr + l) + "\n") # nieuw regelnummer
                        i = i + 1
                        timestamps = lines[i].split(" --> ") 
                        if fnr >= f:
                            # do the math...
                            begin = diff(timestamps[0],td)
                            end = diff(timestamps[1].strip('\n'),td)
                            print(begin[:-3], end[:-3])
                            # w.write(f"{begin[:-3]} --> {end[:-3]}\n") # nieuwe timestamp
                            new_sub = f"{new_sub}{begin[:-3]} --> {end[:-3]}\n"
                            print(f"{new_sub}{begin[:-3]} --> {end[:-3]}\n")

                        else:
                            # w.write(f"{timestamps[0]} --> {timestamps[1]}")
                            new_sub = f"{new_sub}{timestamps[0]} --> {timestamps[1]}"

                    except ValueError:
                        pass       
            else:
                # w.write(lines[i]) # overige regels
                new_sub = new_sub + lines[i];
    return new_sub

# 1799
# 01:42:56,103 --> 01:43:00,165

f = 1 # fragmentnummer
l = 0 # regelnummer
td = timedelta(hours=0, minutes=0, seconds=14) # timediff
r = open("subtitle.txt", "r") # subtitle file
# convert(r,td,f, l)
w = open("bla.srt", "w") # new file
w.write(convert(r,td,f, l))


