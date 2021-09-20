import json
'''

User = {"username":"Baal",
        "password":"Thunder321!"
        }

'''


def UserDatabaseAppend(User):
    with open('loginHistory.json', 'a', encoding='utf-8') as f:
        json.dump(User, f, ensure_ascii=False, indent=4)

        print("User database updated.\n")
