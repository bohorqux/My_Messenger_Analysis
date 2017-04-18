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

def timestampsCounter(start, end, outFile, timearray, val):
    ss = start
    es = end
    counter = 0
    timeindice = 0
    
    while ss != es:
        
        if ss == timearray[timeindice]:
            #if timeindice >= 130:
                #input("MATCH FOUND")
                #input("***finding next timestamp:\t%s***" % timearray[timeindice+1])
            t = "".join(ss.split(":"))
            timeindice += 1
            print("***finding next timestamp:\t%s***" % timearray[timeindice])
            #outFile.write("%d\t%d\n" % (counter, val))

        elif int(ss[13:]) == 60:
            ss = incrementHour(ss)
            ss = ss[:13] + "00"
            
        elif int(ss[11:13]) == 25:
            ss = incrementDay(ss)
            ss = ss[:11] + "0000"

        elif int(ss[3:5]) == 32:
            ss = incrementMonth(ss)
            ss = ss[:3] + "01" + ss[5:]

        elif int(ss[:2]) == 13:
            ss = incrementYear(ss)
            ss = "01" + ss[2:]


        else:
            ss = incrementMinute(ss)
            #outFile.write("%d\n" % counter)

        counter += 1
        print(ss)

    print("time indice = %d\tarray length = %d\n" % (timeindice, len(timearray)))
        
    
def main():
    threads = initThreads("messages.htm")
    chat = threads[313]
    debug = [t.string for t in chat.find_all("span", class_ = "meta")]
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    users.reverse()
    debug.reverse()
    cross = [(users[i], debug[i]) for i in range(len(debug)) if users[i] == "Xavier Bohorquez"]
    cross = [x[1] for x in cross]
    [print(cross[i]) for i in range(130, 150)]
    print()
    
    xavi_stamps = [timestamp[1] for timestamp in getUserTimestamps(chat, "Xavier Bohorquez")]
    [print(xavi_stamps[i]) for i in range(130, 150)]

    timestampsCounter(xavi_stamps[0], xavi_stamps[-1], 10, xavi_stamps, 1)

main()

    
