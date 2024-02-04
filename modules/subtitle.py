from datetime import datetime, timedelta 
import time

# Calculate new time from time and timedelta
# @datetime t
# @timedelta td
def diff(t, td):
    t = datetime.strptime(t, '%H:%M:%S,%f')
    return (t + td).strftime("%H:%M:%S,%f")

# Get start and end of textfragments of a complete .srt-file
# @list lines
# @return list with list-elements consisting of two integers referencing the textfragment-numbers
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

# Create a dictionary from a textfile with subtitles
# @list lines
def create_dictionaries(lines):
    # fd = {"fnr": 0, "start": "00:00:00,000", "end": "00:00:00,000", "tekst": ""}
    framelist = []
    for i in get_fragment_linenumbers(lines):
        fd = {}
        frame = lines[i[0]:i[1]]
        # t = addtime(frame[1], timediff)
        # print(frame)
        t = frame[1].split(" --> ") 
        fd["fnr"] = int(frame[0].strip("\n"))
        fd["start"] = t[0].strip("\n")
        fd["end"] = t[1].strip("\n")
        fd["tekst"] = ''.join(frame[2:]).strip("\n\n")
        framelist.append(fd)
    return framelist

# Adjust all fragments from a certain starting point (fragmentnumber) up to the fragmentnumber of the last textfragment
# @int startframe
# @int endframe
# @list with dictionaries of all textfragments
# return @list with adjusted dictionaries
def adjust_time_abs(startframe, endframe, dictlist, timediff):
    for f in dictlist:
        if f["fnr"] >= startframe and f["fnr"] <= endframe:
            # print(f["start"])
            f["start"] = diff(f["start"], timediff)[:-3]
            f["end"] = diff(f["end"], timediff)[:-3]
        print(f)
    return dictlist

# Stretch or shrink fragments from a certain starting point (fragmentnumber) up to the fragmentnumber of the last textfragment
# @int startframe
# @int endframe
# @list with dictionaries of all textfragments
# @int perc (percentage to adjust time-properties of all fragments)
# return @list with adjusted dictionaries
def adjust_time_rel(startframe, endframe, dictlist, perc):
    if endframe == 0:
        lframe = len(dictlist)
    else:
        lframe = endframe
    for i, f in enumerate(dictlist):
        if f["fnr"] > startframe and f["fnr"] <= lframe:
            # print(f["start"])
            f["start"] = time_with_perc(perc, f["start"])[:-3]
            f["end"] = time_with_perc(perc, f["end"])[:-3]
            print(f)
    return dictlist

# Add up given time and percentage of that time
# @float perc (percentage to stretch or shrink when negative)
# @string hmsf time in "H:M:S,f" format
# return @datetime adjusted time
def time_with_perc(perc, hmsf):
    t0 = datetime.strptime("00:00:00,000", "%H:%M:%S,%f")
    t1 = datetime.strptime(hmsf, '%H:%M:%S,%f')
    delta = t1 - t0
    secs = delta.total_seconds()
    total = (secs * perc)/100
    s0 = timedelta(milliseconds=int(round((total * 1000),0)))
    d = s0 + t0
    return datetime.strftime(d, "%H:%M:%S,%f")

# Figure out the difference as percentage between two timestamps
# @string ts1 original time
# @string ts2 adjusted time
# return @float perc percentage
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