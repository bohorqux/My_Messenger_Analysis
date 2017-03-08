#!/usr/bin/python3
from stringformatting import *
from bs4 import BeautifulSoup

def getUniqueUsers(chat):
    """ return distinct list of users that exist in a single thread/chat """
    users = [user.string for user in chat.find_all("span", class_ = "user")]
    return list(set(users))

def displayUsers(chat):
    unique_users = getUniqueUsers(chat)
    for u in unique_users:
        if "facebook.com" in u:
            print("UNKNOWN...")
        else:
            print(u)
    return 0
    
def displayAllUsers(threads):
    """ displays all users involved in each thread """
    for i in range(len(threads)):
       print("thread[%d]:----" % i)
       displayUsers(thread[i])

       print("\n")
    return 0

