from modules import subtitle as s
from datetime import datetime, timedelta
import sys 

input_file = "input.srt"
output_file = "output.srt"

def write_out(output_file, sub_dict):
    try:
        w = open(output_file, "w")
        for d in sub_dict:
            w.write(f"{d['fnr']}\n{d['start']} --> {d['end']}\n{d['tekst']}\n\n")
    except Exception as e:
        print(e)

def dictlist(input_file):
    r = open(input_file, "r") # subtitle file
    lines = r.readlines()
    return s.create_dictionaries(lines)

def checktime(t1):
    try:
        t = datetime.strptime(t1, "%H:%M:%S")
    except Exception as e:
        print(e)
        print("Geef een geldige tijd op!")
        sys.exit(1)
    return t1 + ",000"

def checkint(i, default, err):
    if i == "":
        return default
    else:
        try:
            return int(i)
        except ValueError as e:
            print("Voer een geldig getal in")
            return err

    
# new_sub_dict = s.adjust_time_abs(1, 5000, dictlist, timediff)


keuze = input("Kies de methode om een subtitle aan te passen s=(stretch/shrink) a=(adjust) ")
cs = -1
ce = -1
sec = 0
dictlist = dictlist(input_file)
if keuze == "s":
    ut1 = input("geef de originele tijd op (H:M:S): ")
    ct1 = checktime(ut1)
    ut2 = input("geef de gewenste tijd op (H:M:S): ")
    ct2 = checktime(ut2)
    while cs <= 0:
        us = input("geef het startfragment op (1): ")
        cs = checkint(us, 1, -1)

    while ce <= cs:
        ue = input("geef het eindfragment op (0 = tot laatste): ")
        ce = checkint(ue, 0, -1)
        if ce == 0:
            ce = len(dictlist)
        elif ce <= cs:
            print(f"geef 0 op voor alle of een getal groter dan het startfragment")
 
    perc = s.calc_time_perc(ct1, ct2)
    new_sub_dict = s.adjust_time_rel(cs, ce, dictlist, perc)
    write_out(output_file, new_sub_dict)

elif keuze == "a":
    while cs <= 0:
        us = input("geef het startfragment op (1): ")
        cs = checkint(us, 1, -1)
    while ce < cs:
        ue = input("geef het eindfragment op (0): ")
        ce = checkint(ue, 0, -1)
        if ce == 0:
            ce = len(dictlist)
            print(f"eindfragment = {ce}")
        elif ce == -1:
            print(f"geef 0 op voor alle of een getal groter dan het startfragment")
    while sec == 0:
        ue = input("geef het verschil in seconden op: ")
        sec = checkint(ue, 0, 0)
        print(f"abs_function: {cs}, {ce},{sec}")
    write_out(output_file, s.adjust_time_abs(cs, ce, dictlist, timedelta(hours=0, minutes=0, seconds=sec)))









