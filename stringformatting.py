#!/usr/bin/python3
import re

def lead_zeros(string, amount):
    return "0" * (amount - len(string)) + string

def miliTime(time):
    time = re.sub(":", "", time)
    isPM = False
    
    if "pm" in time:
        isPM = True

    time = int(time[:-2])
    
    if 1159 < time < 1259 and not isPM:
        time -= 1200        
    if isPM:
        time += 1200
    
    return str(time)

def string_to_date(string):
    months = dict()
    m = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
    for i in range(len(m)):
        months[m[i]] = i
        
    stored = string.split(" ")[1:]
    stored[0] = str(months[stored[0]])
    stored[1] = re.sub(",", "", stored[1])
    processed = [stored[2], lead_zeros(stored[0], 2), lead_zeros(stored[1], 2), lead_zeros(miliTime(stored[4]), 4)]
    timestamp = int("".join(processed))
    
    return timestamp


        
