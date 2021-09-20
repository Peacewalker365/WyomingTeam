import login_cli
import history
from UI import UI

file = open('accounts.txt', 'w')



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

def test_savedLogin():
    assert history.loginRecordQuery('username1', 'Password1!') == False

def test_loginAndNavigiation():
    #Starts the UI to manually test the login interface and navigation
    ui = UI()
    ui.loginUI()

