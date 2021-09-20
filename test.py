import login_cli


file = open('accounts.txt', 'w')

def test_createAccount():
    assert login_cli.signup('username1', 'password') == "Account created!"
    #assert login_cli.signup('username1', 'password') == 'Username already exists'
    #assert login_cli.signup('username2', 'password') == "Account created!"
    #assert login_cli.signup('username3', 'password') == "Account created!"
    #assert login_cli.signup('username4', 'password') == "Account created!"
    #assert login_cli.signup('username5', 'password') == "Account created!"

def test_uniqueUsername():
    assert login_cli.signup('username1', 'password') == 'Username already exists'

def test_maxAccoutns():
    assert login_cli.signup('username2', 'password')
    assert login_cli.signup('username3', 'password')
    assert login_cli.signup('username4', 'password')
    assert login_cli.signup('username5', 'password')
    assert login_cli.signup('username6', 'password') == 'Too many users'

#print(login_cli.signup('username2', 'password'))
#print(login_cli.login('username2', 'password'))

def test_login():
    file = open('accounts.txt', 'w')
    login_cli.signup('username2', 'password')
    assert login_cli.login('username2', 'password') == 'You are logged in!'
    assert login_cli.login('username2', 'password123') == 'Invalid credentials'

def test_ifNameValid():
    login_cli.signup('username2', 'password')
    assert login_cli.ifNameValid("username2") == False
    assert login_cli.ifNameValid("Bill") == True

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
