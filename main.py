from datetime import datetime, timedelta 
import time

def diff(t, td):
    t = datetime.strptime(t, '%H:%M:%S,%f')
    return (t + td).strftime("%H:%M:%S,%f")

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

def create_dictionaries(lines):
    # fd = {"fnr": 0, "start": "00:00:00,000", "end": "00:00:00,000", "tekst": ""}
    framelist = []
    for i in get_fragment_linenumbers(lines):
        fd = {}
        frame = lines[i[0]:i[1]]
        # t = addtime(frame[1], timediff)
        print(frame)
        t = frame[1].split(" --> ") 
        fd["fnr"] = int(frame[0].strip("\n"))
        fd["start"] = t[0].strip("\n")
        fd["end"] = t[1].strip("\n")
        fd["tekst"] = ''.join(frame[2:]).strip("\n\n")
        framelist.append(fd)
    return framelist

def adjust_time_abs(startframe, endframe, dictlist, timediff):
    for f in dictlist:
        if f["fnr"] >= startframe and f["fnr"] <= endframe:
            # print(f["start"])
            f["start"] = diff(f["start"], timediff)[:-3]
            f["end"] = diff(f["end"], timediff)[:-3]
        print(f)
    return dictlist

def adjust_time_rel(startframe, endframe, dictlist, perc):
    for i, f in enumerate(dictlist):
        if f["fnr"] > startframe and f["fnr"] <= endframe:
            # print(f["start"])
            f["start"] = time_with_perc(perc, f["start"], perc)[:-3]
            f["end"] = time_with_perc(perc, f["end"], perc)[:-3]
            print(f)
    return dictlist


def time_with_perc(perc, hmsf, i):
    t0 = datetime.strptime("00:00:00,000", "%H:%M:%S,%f")
    t1 = datetime.strptime(hmsf, '%H:%M:%S,%f')
    delta = t1 - t0
    secs = delta.total_seconds()
    total = (secs * perc)/100
    s0 = timedelta(milliseconds=int(round((total * 1000),0)))
    d = s0 + t0
    return datetime.strftime(d, "%H:%M:%S,%f")


# def time_in_seconds(hms):
#     t0 = datetime.strptime("00:00:00,000", "%H:%M:%S,%f")
#     t1 = datetime.strptime(hms, '%H:%M:%S,%f')
#     delta = t1 - t0
#     return delta.total_seconds()  

def calc_time_perc(ts1, ts2):
    # convert time string to datetime
    t0 = datetime.strptime("00:00:00,000", "%H:%M:%S,%f")
    t1 = datetime.strptime(ts1, "%H:%M:%S,%f")
    t2 = datetime.strptime(ts2, "%H:%M:%S,%f")
    delta1 = t1 - t0
    orig_secs = delta1.total_seconds()
    delta2 = t2 - t0
    new_secs = delta2.total_seconds()
    perc = (new_secs / orig_secs) * 100
    return (perc)

# def get_time_percentage(hms, sec2):
#     sec1 = time_in_seconds(hms)
#     return int(sec1)/int(sec2)





# convert(r,td,f, l)
# w = open("bla.srt", "w") # new file
# w.write(convert(lines,td,f, l))
# for i in dictlist:
#     print(i) 
# print(adjust_time_abs(2, 3, dictlist, timedelta(hours=2, minutes=0, seconds=11)))

# print(time_in_seconds('00:03:33'))
# print(calc_time_difference('01:00:55','01:01:53'))
# print(adjust_time_rel(1, 5, dictlist, "00:01:04,951", "00:02:00,00"))

r = open("subtitle.srt", "r") # subtitle file

lines = r.readlines()
dictlist = create_dictionaries(lines)


# adjust_time_rel(1, 5000, dictlist, perc)
# adjust_time_abs(1, 5000, dictlist, timediff)

timediff = timedelta(hours=0, minutes=0, seconds=2) # timediff
# new_sub_dict = adjust_time_abs(90, 5000, dictlist, timediff)
perc = calc_time_perc("01:13:54,830", "01:14:00,055")
new_sub_dict = adjust_time_rel(0, 974, dictlist, perc)


# 971
# 01:13:51,464 --> 01:13:54,830
# Yeah, I guess they are, it's a shame.




w = open("blab.srt", "w")
for d in new_sub_dict:
    w.write(f"{d['fnr']}\n{d['start']} --> {d['end']}\n{d['tekst']}\n\n")
   
