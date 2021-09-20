import json
'''

users = {"username":"Baal",
        "password":"Thunder321!"
        }

'''

def loginRecordAppend(user):
    
    if loginRecordQuery(list(user.keys())[0], list(user.values())[0]) == False:
        with open('loginHistory.json', "r") as f:
            users = json.load(f)
            users.update(user)
        with open('loginHistory.json', "w") as f:
            json.dump(users, f)
            print("Login History updated.\n")

def loginRecordQuery(name, pssd):
    
    with open('loginHistory.json') as f:
        users = json.load(f)
        if (name in users) and (pssd == users[name]):
            return True
        else:
            return False

def makeDict(name, pssd):
 
            
    user = {
            "username":name,
            "password":pssd
            }
    return user
