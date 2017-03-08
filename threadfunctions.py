#!/usr/bin/python3

def getUniqueUsers(chat):
    users = [user.string for user in chat.find_all("span", class_ = "user")]
    return list(set(users))

def displayUsers():
    for i in range(len(all_unique_users)):
       print("thread[%d]:----" % i)
       
       for u in all_unique_users[i]:
          if "facebook.com" in u:
             print("UNKNOWN...")
          else:
             print(u)
             
       print("\n")
    return 0

