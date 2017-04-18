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
    if 1200 <= time <= 1259 and not isPM: #convert time between 12:00am-12:59am into military time
        time -= 1200        
    if isPM and 100 <= time <= 1159:
        time += 1200
    
    return str(time)

def string_to_date(timestamp):
    """ converts messenger timestamp string into its integer representation 

        Keyword Arguments:

        string -- input must be as follows: {DayofWeek, MonthandDay, Year at Time EDT}
    """
    #initialize dictionary to correspond Month with integer
    months = dict()
    m = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for i in range(len(m)):
        months[m[i]] = i+1

    #format Messenger timestamp to remove irrelevant information
    stored = timestamp.split(" ")[1:]
    stored[0] = str(months[stored[0]])
    stored[1] = re.sub(",", "", stored[1])
    processed = [stored[2], lead_zeros(stored[0], 2), lead_zeros(stored[1], 2), lead_zeros(miliTime(stored[4]), 4)]

    #devise integer out of resulting timestamp string
    timestamp_int = int("".join(processed))
    
    return timestamp_int

def format_date(timestamp):
    timestamp = str(timestamp)
    timearray = [timestamp[4:6], timestamp[6:8], timestamp[:4], timestamp[8:]]
    timestring = ":".join(timearray)
    return timestring
        
