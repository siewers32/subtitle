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

def counter(c):
    return c + 1

def convert(r, w, td, f):
    lines = r.readlines()
    #for i in range(0, len(lines)):
    i = -1
    while i < (len(lines)-2):
        i = i + 1
        line = lines[i]
        if line in ['\n', '\r\n'] or i == 0:
            # Eerste regel is regelnummer
            if i != 0:
                w.write("\n")
                i = i + 1
            if(i+1 < len(lines)):
                try:
                    fnr = int(lines[i].strip(" "))
                    print(fnr)
                    w.write(str(fnr) + "\n")
                    i = i + 1
                    timestamps = lines[i].split(" --> ") 
                    if fnr >= f:
                        # do the math...
                        begin = diff(timestamps[0],td)
                        end = diff(timestamps[1].strip('\n'),td)
                        print(begin[:-3], end[:-3])
                        w.write(f"{begin[:-3]} --> {end[:-3]}")
                        w.write("\n")
                    else:
                        w.write(f"{timestamps[0]} --> {timestamps[1]}")
                except ValueError:
                   pass       
        else:
            pass
            w.write(lines[i])


f = 433 # fragmentnummer
td = timedelta(hours=0, minutes=0, seconds=4) # timediff
r = open("subtitle.srt", "r") # subtitle file
w = open("S01_E1__Care_and_protection.NL.srt", "w") # new file
convert(r,w,td,f)

