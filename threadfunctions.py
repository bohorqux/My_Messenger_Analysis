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

    print("Threads parsed successfully!\n************************\n")
    return threads

def getUniqueUsers(chat):
    """ return distinct list of users that exist in a single thread/chat """
    users = [user.string for user in chat.find_all("span", class_ = "user")]
    return list(set(users))

def getPostingFreq(chat, user):
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    return len([u for u in users if u == user])

def displayPostingFreq(chat):
    unique_users = getUniqueUsers(chat)
    for u in unique_users:
        frequency = getPostingFreq(chat, u)
        print("%s: %d total posts" % (u, frequency))
    return 0

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

def displaySpecified(threads, user):
    acc = 0
    for i in range(len(threads)):
        if user in getUniqueUsers(threads[i]):
            print("thread[%d]:---" % i)
            displayUsers(threads[i])
            acc += 1
            print()
            print("*************************************")
            displayPostingFreq(threads[i])
            print("*************************************")
            print()
    print("Involved in %d message(s)...\n" % acc)
    return 0

def displayChat(chat):
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    users.reverse()
    posts = [p.string for p in chat.find_all("p")]
    posts.reverse()
    timestamps = [format_date(string_to_date(t.string)) for t in chat.find_all("span", class_ = "meta")]
    timestamps.reverse()

    for i in range(len(users)):
        print("%s: %s\n\t%s" % (users[i], timestamps[i], posts[i]))
    return 0
    
##################################################################################
def main():
    threads = initThreads("messages.htm")
    #displayAllUsers(threads)
    #displaySpecified(threads, "Keyan Vakil")
    displayChat(threads[229])
    #displayPostingFreq(threads[92])
    return 0

main()

