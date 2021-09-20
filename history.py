import json
'''

user = {"username":"Baal",
        "password":"Thunder321!"
        }

'''

def loginRecordAppend(user):
    if loginRecordQuery((user.keys())[0], (user.values())[0]) == False:
        with open('loginHistory.json', 'a', encoding='utf-8') as f:
            json.dump(user, f, ensure_ascii=False, indent=4)

        print("Login History updated.\n")

def loginRecordQuery(name, pssd):
    users = {}
    with open('loginHistory.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
        if (name in users) and (user[name] == users[name]):
            return True
        else:
            return False

def makeDict(name, pssd):
 
            
    user = {
            "username":name,
            "password":pssd
            }
    return user
