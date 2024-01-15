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

def convert(r, w, td, f):
    lines = r.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if line in ['\n', '\r\n']:
            w.write(lines[i])
            # Eerste regel is regelnummer
            i = i + 1
            if(i+1 < len(lines)):
                try:
                    fnr = int(lines[i].strip(" "))
                    print(fnr)
                    i = i + 1
                    timestamps = lines[i].split(" --> ") 
                    if fnr >= f:
                        # do the math...
                        begin = diff(timestamps[0],td)
                        end = diff(timestamps[1].strip('\n'),td)
                        print(begin[:-3], end[:-3])
                        w.write(f"{begin[:-3]} --> {end[:-3]}")
                    else:
                        w.write(f"{timestamps[0]} --> {timestamps[1]}")

                except ValueError:
                   pass       
        else:
            w.write(lines[i])

f = 980 # fragmentnummer
td = timedelta(hours=0, minutes=0, seconds=5) # timediff
r = open("test.txt", "r") # subtitle file
w = open("new.txt", "w") # new file
convert(r,w,td,f)

