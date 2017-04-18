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

def getStringMatchesByUser(chat, string, user):
    """ returns number of times string is said by user in chat """
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    posts = [p.string for p in chat.find_all("p")]
    
    for i in range(len(posts)):
        if posts[i] == None:
            continue
        elif string in posts[i] and users[i] == user:
            counter += 1
    return counter

def getStringMatchPercentage(chat, string):
    """ returns percentage of chat that consists of string """
    return getStringMatches(chat, string)/getTotalPosts(chat)

def getUserPercentage(chat, user):
    """ returns percentage of chat that consists of user """
    return getPostingFreq(chat, user)/getTotalPosts(chat)

def getAllUserPercentage(chat):
    """ returns dictionary that corresponds user with posting percentage """
    percentages = dict()
    users = getUniqueUsers(chat)
    for u in users:
        percentages[u] = getUserPercentage(chat, u)

    return percentages

def getUserStringPercentage(chat, string, user):
    """ returns percentage of string outputted by a user in a chat """
    return getStringMatchesByUser(chat, string, user)/getPostringFreq(chat, user)

def getTotalWords(chat):
    """ returns total amount of words in chat """
    posts = [p.string for p in chat.find_all("p")]
    words = [len(pstring.split(" ")) for pstring in posts if pstring != None]
    return sum(words)

def getAverageMessageLength(chat):
    """ returns average number of words in a chat """
    posts = [p.string for p in chat.find_all("p")]
    avg =  len(posts)/getTotalWords(chat)
    avg_n = avg * 100
    return avg_n
    
    
##################################### DATA RETRIEVAL FUNCTIONS ####################################################

##################################### MIDDLEWARE     FUNCTIONS ####################################################
def getPosts(chat):
    """ returns list of all posts in a chat """
    return [p.string for p in chat.find_all("p") if p.string != None]

def mostCommonPosts(chat):
    """ returns tuple list of most common posts/messages that exists in a chat """
    posts = [p.string for p in chat.find_all("p") if p.string != None]
    return createFrequencyList(posts)

def createFrequencyList(aList):
    """ helper function that returns a tuple list (element, frequency) in aList """
    frequencies = dict() #initialize dictionary to capture frequency of posts

    #count up all occurences of each element
    for element in aList:
        if element not in frequencies:
            frequencies[element] = 1
        else:
            frequencies[element] += 1

    #collect frequency values, terminate program if the chat contains truly distinct posts
    scores = [frequencies[key] for key in frequencies if frequencies[key] != 1]
    
    if len(scores) == 0:
        print("No distinct frequencies found...terminating")
        return 0

    #create tuple list of dictionary keys and values
    elementScores = [(key, frequencies[key]) for key in frequencies if frequencies[key] in scores]
    sortedScores = sorted(elementScores, key= lambda t:t[1])

    return sortedScores

def collectWords(chat):
    """ returns a list of all words in a chat """
    posts = [p.string for p in chat.find_all('p') if p.string != None]
    wordies = list()
    
    #probably a really inefficient way to get all the words
    for sentence in posts:
        for words in sentence.split(" "):
            wordies.append(words)
    return wordies
            
def mostCommonWords(chat):
    """ returns tuple list of most common words that exist in a chat """
    words = collectWords(chat)
    return createFrequencyList(words)

def debugTimeStamp(chat, user, istart, iend):
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    timestamps = [t.string for t in chat.find_all("span", class_ = "meta")]
    users.reverse()
    timestamps.reverse()
    toDate = [string_to_date(t) for t in timestamps]
    formatted = [format_date(t) for t in toDate]

    for i in (istart, iend, 1):
        print("original timestamp:\t%s" % timestamps[i])
        print("string_to_date timestamp:\t%s" % toDate[i])
        print("formatted timestamp:\t%s" % formatted[i])
        print()
        
def getUserTimestamps(chat, user):
    """ returns tuple list of specified user with their timestamps """
    users = [u.string for u in chat.find_all("span", class_ = "user")]
    timestamps = [format_date(string_to_date(t.string)) for t in chat.find_all("span", class_ = "meta")]
    users.reverse()
    timestamps.reverse()
    cross = [(users[i], timestamps[i]) for i in range(len(timestamps)) if users[i] == user]
    return cross
################################# MIDDLEWARE         FUNCTIONS ####################################################

################################# THREAD/CHAT VISUAL FUNCTIONS ####################################################

def displayStringMatches(chat, string):
    """ prints frequency of string found in chat """
    matches = getStringMatches(chat, string)
    print("\n####################\nFound %d instances of phrase - %s - in this thread...\n####################" % (matches, string))
    
def displayPostingFreq(chat):
    """ prints frequency of all user posts in chat """
    unique_users = getUniqueUsers(chat)
    for u in unique_users:
        frequency = getPostingFreq(chat, u)
        print("%s: %d posts" % (u, frequency))

    print("\nTotal post amount: %d\n" % getTotalPosts(chat))
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

def displayChatData(chat):
    """ prints a bunch of data about a chat """
    print("--------------- U S E R S ---------------")
    displayUsers(chat)
    print("--------------- U S E R S ---------------")
    print("\n*************** D A T A ***************")
    displayPostingFreq(chat)
    print("Total posts in chat: %d" % getTotalPosts(chat))
    print("Total words in chat: %d" % getTotalWords(chat))
    print("AverageMessageLength: %.3f" % getAverageMessageLength(chat))

    userfreq = getAllUserPercentage(chat)
    print("\n%%%%%%%%%%%%%%% F R E Q %%%%%%%%%%%%%%%")
    for u in userfreq:
        print("%s percentage:\t%.2f" % (u, userfreq[u]*100))
    print("%%%%%%%%%%%%%%% F R E Q %%%%%%%%%%%%%%%")
    print("\n*************** D A T A ***************")

def displayFrequencyList(aList, titlestring, columnstring):
    """ prints out the frequency """

    print("^^^^^^^^^^^^^^^^^^^^ %s ^^^^^^^^^^^^^^^^^^^^^^^^^" % titlestring)
    print("\n%s:\t\tScore:\n--------------------\n" % columnstring)

    for (x,y) in aList:
        print("%s\t\t%d" % (x, y))
        
########################## THREAD/CHAT VISUAL FUNCTIONS ####################################################


###################################### MAIN ################################################################
def main():
    threads = initThreads("messages.htm")
    displayChatData(threads[313])
    return 0

###################################### MAIN #################################################################

#main()

