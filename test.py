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