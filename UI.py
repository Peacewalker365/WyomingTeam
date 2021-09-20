from re import search
from login_cli import login
from login_cli import getUsers
from login_cli import signup
from login_cli import ifPasswordValid
from login_cli import ifNameValid
##from history import loginRecordQuery
##from history import loginRecordAppend
##from history import  makeDict


class UI:
    def __init__(self):
        self.loggedIn = False

    def loginUI(self):
        print("\n\n\n*******************************\n")
        print("1. Sign in\n")
        print("2. Sign up\n")
        print("3. Quit\n")
        print("\n*******************************\n\n\n")
        inpt = input("Go to: ")
        if inpt == "1":
            if self.loggedIn == True:
                return self.mainUI()
            username_inpt = input("username: ")
            password_inpt = input("password: ")
##            if loginRecordQuery(username_inpt, password_inpt) == True:
##                return self.mainUI()
            if login(username_inpt, password_inpt) == 'You are logged in!':
                #user = makeDict(username_inpt, password_inpt)
                #loginRecordAppend(user)
                print("You are logged in!")
                return self.mainUI()
            else:
                print("Invalid credentials")
                return self.loginUI()
                         
        elif inpt == "2":
            username_inpt = input("username: ")
            password_inpt = input("password: ")
            if ifNameValid(username_inpt) == False:
                return self.loginUI()
            if ifPasswordValid(password_inpt) == False:
                return self.loginUI()
            loginRes = signup(username_inpt, password_inpt)
            if loginRes == "Account created!":
                
                print("Account created!")
                return self.mainUI()
            else:
                print(loginRes)
                return self.loginUI()
                    
        elif inpt == "3":
            return
        else:
            print("Invalid entry, please try again.\n")
            return self.loginUI()


        
    def mainUI(self):
        self.loggedIn = True
        print("\n\n\n*******************************\n")
        print("1. Search a job\n")
        print("2. Find someone\n")
        print("3. Learn a new skill\n")
        print("4. Log out\n")
        print("\n*******************************\n\n\n")

        inpt = input("Go to: ")
        if inpt == "1":
            print("Under construction\n")
            return self.mainUI()
        elif inpt == "2":
            print("Under construction\n")
            return self.mainUI()
        elif inpt == "3":
            return self.skillUI()
        elif inpt == "4":
            return self.loginUI()
        else:
            print("Invalid entry, please try again.\n")
            return self.mainUI()


    def skillUI(self):
        print("\n*******************************\n")
        print("1. Programming\n")
        print("2. Theory of Composition\n")
        print("3. Sky Dive\n")
        print("4. Short Swing Trading\n")
        print("5. Time Management\n")
        print("6. I'm perfect enough\n")
        print("\n*******************************\n")
        
        inpt = input("\nGo to: ")
        x = search("^[1-5]$", inpt)

        if x != None:
            print("Under construction\n")
            return self.skillUI()
        elif inpt == "6":
            return self.mainUI()
        else:
            print("Invalid entry, please try again.\n")
            return self.skillUI()
            
        
    
