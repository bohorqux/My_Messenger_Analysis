#!/usr/bin/python3
import re

def lead_zeros(string, num_zeros):
    """ pads zero(s) to front of specified string """
    return "0" * (num_zeros - len(string)) + string

def miliTime(time):
    """ converts meridian time string into military time string """
    
    time = re.sub(":", "", time)
    isPM = False
    if "pm" in time:
        isPM = True

    time = int(time[:-2]) #removing am/pm discretion to perform essential mathematical operations
    if 1159 < time < 1259 and not isPM:
        time -= 1200        
    if isPM:
        time += 1200
    
    return str(time)

def string_to_date(timestamp):
    """ converts messenger timestamp string into its integer representation 

        Keyword Arguments:

        string -- input must be as follows: {DayofWeek, MonthandDay, Year at Time EDT}
    """
    #initialize dictionary to correspond Month with integer
    months = dict()
    m = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
    for i in range(len(m)):
        months[m[i]] = i

    #format Messenger timestamp to remove irrelevant information
    stored = timestamp.split(" ")[1:]
    stored[0] = str(months[stored[0]])
    stored[1] = re.sub(",", "", stored[1])
    processed = [stored[2], lead_zeros(stored[0], 2), lead_zeros(stored[1], 2), lead_zeros(miliTime(stored[4]), 4)]

    #devise integer out of resulting timestamp string
    timestamp_int = int("".join(processed))
    
    return timestamp_int


        
