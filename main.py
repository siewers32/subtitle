from datetime import datetime, timedelta 
import time
def strtotime(s):
    dt = datetime.strptime(s, '%H:%M:%S,%f').time()

def calcTimeDiff(t, td):
    # oorspronkelijke tijd
    # hours, minutes, seconds optellen bij oorspronkelijke tijd
    t = datetime.strptime(t, '%H:%M:%S,%f')
    # print(t + td).strftime("%H:%M:%S,%f")
    # print((t + td).strftime("%H:%M:%S,%f"))
    return (t + td).strftime("%H:%M:%S,%f")

def counter(c):
    return c + 1

def adjustTime(line, minfragment, fragment):
    try:
        timestamps = line.split(" --> ") 
        if fragment >= minfragment:
            # do the math...
            begin = calcTimeDiff(timestamps[0],td)
            end = calcTimeDiff(timestamps[1].strip('\n'),td)
            return f"{begin[:-3]} --> {end[:-3]}\n"
        else:
            return f"{timestamps[0]} --> {timestamps[1]}\n"
    except ValueError as ve:
        print("something wrong with values in timediff")       


def convert(r, w, td, f):
    lines = r.readlines()
    i = 0
    while i < (len(lines)-2):
        line = lines[i]
        if line in ['\n', '\r\n'] or i == 0:
            # Eerste regel is regelnummer
            if i != 0:
                w.write("\n")
                i = i + 1
                
            fnr = int(lines[i].strip(" "))
            w.write(str(fnr) + "\n")
            i = i + 1
            w.write(adjustTime(lines[i], f, fnr))   
        else:
            pass
            w.write(lines[i])
        i = i + 1


f = 433 # fragmentnummer
td = timedelta(hours=0, minutes=0, seconds=4) # timediff
r = open("subtitle.srt", "r") # subtitle file
w = open("S01_E1__Care_and_protection.NL.srt", "w") # new file
convert(r,w,td,f)

