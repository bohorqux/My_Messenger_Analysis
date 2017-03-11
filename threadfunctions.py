#!/usr/bin/python3
from stringformatting import *
from bs4 import BeautifulSoup

def initThreads(messenger_html_doc):
    """ devises soup object out of specified messenger file """
    print("Opening file: %s..." % messenger_html_doc)
    fileIn = open(messenger_html_doc, "r")
    print("File opened!")
    feed = fileIn.read()
    fileIn.close()
    print("File closed!")
    print("Converting %s to soup object..." % messenger_html_doc)
    soup = BeautifulSoup(feed, 'lxml')
    threads = soup.find_all("div", class_ = "thread")

    print("Threads parsed successfully!\n************************\n")
    return threads

###################################### DATA RETRIEVAL FUNCTIONS #################################################

def getUniqueUsers(chat):
    """ return distinct list of users that exist in a single thread/chat """
    users = [user.string for user in chat.find_all("span", class_ = "user")]
    return list(set(users))

def getPostingFreq(chat, user):
    """ returns number of times user has posted in a chat """
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    return len([u for u in users if u == user])

def getTotalPosts(chat):
    """ returns number of posts in chat """
    return len([p.string for p in chat.find_all("p")])

def getStringMatches(chat, string):
    """ returns number of times string is found in a chat """
    posts = [p.string for p in chat.find_all("p")]
    counter = 0
    for p in posts:
        if p == None:
            continue
        elif string in p:
            counter += 1
    return counter

##################################### DATA RETRIEVAL FUNCTIONS ####################################################

################################# THREAD/CHAT VISUAL FUNCTIONS ####################################################

def displayStringMatches(chat, string):
    """ prints frequency of string found in chat """
    matches = getStringMatches(chat, string)
    print("\n####################\nFound %d instances of phrase - %s - in this thread...\n####################" % (matches, string))
    
def displayPostingFreq(chat):
    """ prints frequency of all user posts in chat """
    unique_users = getUniqueUsers(chat)
    print("\n*************** POSTING DATA ***************")
    for u in unique_users:
        frequency = getPostingFreq(chat, u)
        print("%s: %d posts" % (u, frequency))

    print("\nTotal post amount: %d" % getTotalPosts(chat))
    print("*************** POSTING DATA ***************\n")
    return 0

def displayUsers(chat):
    """ prints users involved in a chat """
    print("\n--------------- USERS ---------------")
    unique_users = getUniqueUsers(chat)
    for u in range(len(unique_users)):
        if "facebook.com" in unique_users[u]:
            print(unique_users[u], "  ...Possibly: %s" % unique_users[u-1])
        else:
            print(unique_users[u])

    print("----------------- USERS ---------------\n")
    displayPostingFreq(chat)
    
    return 0
    
def displayAllUsers(threads):
    """ displays all users involved in each thread """
    for i in range(len(threads)):
       print("thread[%d]:----" % i)
       displayUsers(threads[i])

       print("\n")
    return 0

def displaySpecified(threads, user):
    """ prints the users in a chat if a specified user is found """
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
    """ prints the conversation stored in chat """
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    users.reverse()
    posts = [p.string for p in chat.find_all("p")]
    posts.reverse()
    timestamps = [format_date(string_to_date(t.string)) for t in chat.find_all("span", class_ = "meta")]
    timestamps.reverse()

    for i in range(len(users)):
        print("%s: %s\n\t%s\n" % (users[i], timestamps[i], posts[i]))
    return 0

########################## THREAD/CHAT VISUAL FUNCTIONS ####################################################


###################################### MAIN ################################################################
def main():
    threads = initThreads("messages.htm")
    displayAllUsers(threads)
    #displaySpecified(threads, "Pedro Pereira")
    #displayStringMatches(threads[125], "yo")
    #displayChat(threads[80])
    #displayPostingFreq(threads[125])
    return 0
###################################### MAIN #################################################################

main()

