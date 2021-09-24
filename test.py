import login_cli


file = open('accounts.txt', 'w')


#Week1
def test_signup():
    #Test Password - 8 <= length <= 12, 1 digit, 1 nonalpha character
    assert login_cli.ifPasswordValid('Password1!') == True
    assert login_cli.ifPasswordValid('sDk123!') == False
    assert login_cli.ifPasswordValid('passcodE45123*') == False
    assert login_cli.ifPasswordValid('Password123') == False
    #Test Account Creation
    assert login_cli.signup('username1', 'Password1!') == 'Account created!'
    assert login_cli.signup('username2', 'Password1!') == 'Account created!'
    #Test Unique Username
    assert login_cli.ifNameValid('username1') == False
    assert login_cli.ifNameValid('username2') == False
    assert login_cli.signup('username1', 'Password1!') == 'Username already exists'
    #Max Users
    login_cli.signup('username3', 'Password1!')
    login_cli.signup('username4', 'Password1!')
    login_cli.signup('username5', 'Password1!')
    assert login_cli.signup('username6', 'Password1!') == 'Too many users'
    assert login_cli.signup('username7', 'Password1!') == 'Too many users'

#Week1
def test_login():
    file = open('accounts.txt', 'w')
    login_cli.signup('username2', 'password')
    assert login_cli.login('username2', 'password') == 'You are logged in!'
    assert login_cli.login('username2', 'password123') == 'Invalid credentials'
#Week1
def test_ifNameValid():
    login_cli.signup('username2', 'password')
    assert login_cli.ifNameValid("username2") == False
    assert login_cli.ifNameValid("Bill") == True
#Week1
def test_ifPasswordValid():
    
    assert login_cli.ifPasswordValid("CCcccc123!") == True
    assert login_cli.ifPasswordValid("cc") == False
    assert login_cli.ifPasswordValid("Cccccccc") == False
    assert login_cli.ifPasswordValid("2cccccccc") == False
    assert login_cli.ifPasswordValid("c!ccccccc") == False
    assert login_cli.ifPasswordValid("2Cccccccc") == False
    assert login_cli.ifPasswordValid("2!ccccccc") == False
    assert login_cli.ifPasswordValid("@Cccccccc") == False
    assert login_cli.ifPasswordValid("2ccccccccdsfsdfdsf") == False







#Week1
## history.py is removed from this project for now.
##def test_makeDict():
##    assert history.makeDict("admin", "1234567") == {"username":"admin", "password":"1234567"}
##    assert history.makeDict("admin12", "123fdr") == {"username":"admin12", "password":"123fdr"}
##
##def test_loginRecordQuery():
##    login_cli.signup("admin", "password")
##    assert history.loginRecordQuery("admin", "password") == True
##    assert history.loginRecordQuery("fsdf", "312fre") == False
##    assert history.loginRecordQuery("", "") == False
##
##
##def test_loginRecordAppend():
##    user1 = history.makeDict("admin1", "1234567")
##    user2 = history.makeDict("admin2", "312fre")
##    assert history.loginRecordAppend(user1) == "Login History updated.\n"
##    assert history.loginRecordAppend(user2) == "Login History updated.\n"
##    assert history.loginRecordAppend(user1) == None
##    assert history.loginRecordAppend(user2) == None


file.close()


