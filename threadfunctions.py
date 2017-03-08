#!/usr/bin/python3
from stringformatting import *
from bs4 import BeautifulSoup

def initThreads(messenger_html_doc):
    """ devises soup object out of specified messenger file """
    print("Opening file: %s" % messenger_html_doc)
    fileIn = open(messenger_html_doc, "r")
    feed = fileIn.read()
    fileIn.close()
    print("Converting %s to soup object" % messenger_html_doc)
    soup = BeautifulSoup(feed, 'lxml')
    threads = soup.find_all("div", class_ = "thread")

    print("Threads parsed successfully!")
    return threads

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
       displayUsers(threads[i])

       print("\n")
    return 0


##################################################################################
def main():
    threads = initThreads("messages.htm")
    displayAllUsers(threads)
    return 0

main()

