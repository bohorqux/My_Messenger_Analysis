#!/usr/bin/python3

from threadfunctions import *

#  m  m  :  d  d  :  y  y  y  y  :  t  t  t  t
#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14

def incrementMinute(timestamp):
    assert(type(timestamp)) == str
    new_time = timestamp[:-4]
    seconds = int(timestamp[-2:]) + 1
    return new_time + timestamp[-4:-2] + lead_zeros(str(seconds), 2)

def incrementHour(timestamp):
    assert(type(timestamp)) == str
    new_time = timestamp[:-4]
    hour = int(timestamp[-4:-2]) + 1
    return new_time + lead_zeros(str(hour), 2) + timestamp[-2:]
    
def incrementDay(timestamp):
    new_time1 = timestamp[:3]
    new_time2 = timestamp[5:]
    day = int(timestamp[3:5]) + 1
    return new_time1 + lead_zeros(str(day), 2) + new_time2

def incrementMonth(timestamp):
    new_time = timestamp[2:]
    month = int(timestamp[:2]) + 1
    return lead_zeros(str(month), 2) + new_time

def incrementYear(timestamp):
    new_time1 = timestamp[:6]
    new_time2 = timestamp[10:]
    year = int(timestamp[6:10]) + 1
    return new_time1 + lead_zeros(str(year), 4) + new_time2

def incrementTime(timestamp):

    timestamp = incrementMinute(timestamp)
    
    if int(timestamp[13:]) == 60:
        timestamp = incrementHour(timestamp)
        timestamp = timestamp[:13] + "00"
            
    elif int(timestamp[11:13]) == 25:
        timestamp = incrementDay(timestamp)
        timestamp = timestamp[:11] + "0000"

    elif int(timestamp[3:5]) == 32:
        timestamp = incrementMonth(timestamp)
        timestamp = timestamp[:3] + "01" + timestamp[5:]

    elif int(timestamp[:2]) == 13:
        timestamp = incrementYear(timestamp)
        timestamp = "01" + timestamp[2:]

    return timestamp

def timeStampCounter(start, end, outFile, timearray, val):
    counter = 0
    timeindice = 0

    while start != incrementTime(end) and timeindice < len(timearray):
        
        if start == timearray[timeindice]:
            t = "".join(start.split(":"))
            timeindice += 1
            outFile.write("%d\t%d\n" % (counter, val))

        else:
            start = incrementTime(start)
            outFile.write("%d\n" % counter)

        counter += 1
            
    print("time indice = %d\tarray length = %d\n" % (timeindice, len(timearray)))        


def createPlot(filename, chat, user, val):

    timearray = [timestamp[1] for timestamp in getUserTimestamps(chat, user)]
    plot = open(filename, "w")
    timeStampCounter(timearray[0], timearray[-1], plot, timearray, val)
    plot.close()
    
def main():
    threads = initThreads("messages.htm")
    chat = threads[313]
    createPlot("Xlog.dat", chat, "Xavier Bohorquez", 1)
    createPlot("Dlog.dat", chat, "Dan Palacio", 2)
    
main()

    
