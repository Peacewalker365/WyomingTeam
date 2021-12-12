from random import randrange as rand
from typing import List
import inquirer as menu
import re
import utils

# TODO: remove global vars.
config = None
logged_in_user = ""  # global variable for current login.
logged_in_user_membership = ""
current_email = ""


def print_welcome_screen() -> dict:
    """Print welcome selections for the user."""
    return menu.prompt([menu.List(
        'welcome_target',
        message='Welcome! Where would you like to go?',
        choices=['Connect to friends', 'Skip', 'Quit'],
        carousel=True
    )])


def print_connect_screen() -> dict:
    """Print connect screen selections for the user."""
    return menu.prompt([menu.List(
        'connect_target',
        message='[CONNECT] Where would you like to go from here?',
        choices=['Log in', 'Sign up to join friends', 'Go back'],
        carousel=True
    )])
#
#Changes to be done
#
def print_main_screen() -> dict:
    """Print main screen selections to the user."""
    return menu.prompt([menu.List(
        'main_target',
        message='[HOME] Where would you like to go next?',
        choices=[
            'Search for a job',
            'Message center',
            'Find someone',
            'Learn a new skill',
            'Friends',
            'Profile',
            'Useful Links',
            'InCollege Important Links',
            'InCollege Learning',
            'Log out'
        ],
        carousel=True
    )])


def print_message_screen() -> dict:
    """Print message selections for the user."""
    return menu.prompt([menu.List(
        'message_target',
        message='Welcome! Where would you like to go?',
        choices=[
            'Send',
            'Inbox',
            'Available recipients',
            'Go back'
        ],
        carousel=True
    )])


def print_inbox_screen():
    user = config['current_login']
    choices = []
    inbox = config['accounts'][user]['inbox']
    for email in inbox:
        choices += list(str(key) + ': ' + str(value) for key, value in email.items())
    choices.reverse()
    choices.append('Go back')
    return menu.prompt([menu.List(
        'inbox_target',
        message='Which message do you want to view?',
        choices=choices,
        carousel=True
    )])


def print_recipient_screen():
    user = config['current_login']
    membership = config['current_login_membership']
    if membership == 'pro':
        choices = [*(config['accounts'].keys())]
    else:
        choices = [*(config['accounts'][user]['friends'])]
    choices.append('Go back')
    return menu.prompt([menu.List(
        'recipient_target',
        message='Which recipient do you want to choose?',
        choices=choices,
        carousel=True
    )])


def print_inbox_operation_screen(email: str) -> dict:
    """Print message selections for the user."""
    return menu.prompt([menu.List(
        'inbox_operation_target',
        message=email,
        choices=[
            'Reply',
            'Delete',
            'Go back'
        ],
        carousel=True
    )])


def print_recipient_operation_screen(recipient: str) -> dict:
    """Print message selections for the user."""
    return menu.prompt([menu.List(
        'recipient_operation_target',
        message='Who do you want to reach?',
        choices=[
            f'Send a message to {recipient}',
            'Go back'
        ],
        carousel=True
    )])

def print_login_screen() -> dict:
    """Print login screen selections to the user."""
    if logged_in_user == '':
        print('-----\n🎓 Here is one of the success stories by one of the users 🎓')
        story = config['stories'][rand(len(config['stories']))]
        print(f'"{story}"')
        print('🎓 Join us to get a job, find some friends, and some more! 🎓\n-----\n')
    return menu.prompt([menu.List(
        'login_target',
        message='[LOGIN] What would you like to do?',
        choices=[
            'Sign in',
            'Sign up',
            'Search for a job',
            'Watch a video',
            'Useful Links',
            'InCollege Important Links',
            'Training',
            'Go back'
        ],
        carousel=True
    )])

def print_ulinks_screen() -> dict:
    return menu.prompt([menu.List(
        'ulinks_target',
        message='[LINKS] Which useful link would you like to browse?',
        choices=[
            'General',
            'Browse InCollege',
            'Business Solutions',
            'Directories',
            'Go back'
        ],
        carousel=True
    )])


def print_general_screen() -> dict:
    return menu.prompt([menu.List(
        'general_target',
        message='[LINKS] Which general link would you like to choose?',
        choices=[
            'Sign up',
            'Help Center',
            'About',
            'Press',
            'Blog',
            'Careers',
            'Developers',
            'Go back'
        ],
        carousel=True
    )])


def print_ilinks_screen() -> dict:
    return menu.prompt([menu.List(
        'ilinks_target',
        message='[LINKS] Which InCollege  link would you like to browse?',
        choices=[
            'Copyright Notice',
            'About',
            'Accessibility',
            'User Agreement',
            'Privacy Policy',
            'Cookie Policy',
            'Copyright Policy',
            'Brand Policy',
            'Guest Controls',
            'Languages',
            'Go back'
        ],
        carousel=True
    )])


def print_privacy_screen() -> dict:
    return menu.prompt([menu.List(
        'privacy_target',
        message='[PRIVACY] Which privacy option would you like to choose?',
        choices=[
            'Guest Control',
            'Go back'
        ],
        carousel=True
    )])


def print_guest_screen() -> dict:
    return menu.prompt([menu.Checkbox(
        'guest_target',
        message='[PRIVACY] Which guest control would you like to toggle?',
        choices=[
            'InCollege Email',
            'SMS',
            'Targeted Advertising features'
        ]
    )])


def print_language_screen() -> dict:
    return menu.prompt([menu.List(
        'language_target',
        message='[LANG] Which language would you like to choose?',
        choices=[
            'English',
            'Spanish'
        ],
        carousel=True
    )])


def print_skill_screen() -> dict:
    return menu.prompt([menu.List(
        'skill_target',
        message='[SKILLS] What would you like to learn?',
        choices=[
            'Programming in C#',
            'Theory of composition',
            'Sky dive',
            'Short swing trading',
            'Time management',
            'I am perfect enough',
            'Go back'
        ],
        carousel=True
    )])


def print_job_screen() -> dict:
    config.notification_center(
            config['current_login'],
            job_notify=False,
            profile_alert=False,
            unread_msg=False,
            job_posted=False,
            job_deleted=False,
            new_user=False,
            job_num=True
    )
    return menu.prompt([menu.List(
        'job_target',
        message='[JOBS] What would you like to do?',
        choices=['Internships', 'Go back'],
        carousel=True
    )])


def print_internship_screen() -> dict:
    return menu.prompt([menu.List(
        'internship_target',
        message='[INTERNSHIPS] What would you like?',
        choices=[
            'Post a job',
            'Apply for a job',
            'Show my applications',
            'Show my postings',
            'Show my saved jobs',
            'Go back'
        ],
        carousel=True
    )])


def print_profile_screen() -> dict:
    return menu.prompt([menu.List(
        'profile_target',
        message='[PROFILE] What would you like to do?',
        choices=[
            'View profile',
            'Edit profile title',
            'Edit profile major',
            'Edit profile university',
            'Edit profile about',
            'Edit profile experience',
            'Edit profile education',
            'Go Back'
        ],
        carousel=True
    )])


def print_friend_screen() -> dict:
    return menu.prompt([menu.List(
        'friend_target',
        message='Friend screen',
        choices=[
            'Show my Network',
            'Search for Someone',
            'View Friend Requests',
            'Go Back'
        ],
        carousel=True
    )])


def print_job_list_screen():
    # Get current login to not display already applied jobs.
    user = config['accounts'][config['current_login']]
    return menu.prompt([menu.List(
        'posting_target',
        message='Choose a job that you want to learn more about',
        # Get list of proper jobs and make them menu choices.
        choices=config.get_list_jobs(user) + ['Go Back'],
        carousel=True
    )])


def print_postings_list_screen():
    user = config['accounts'][config['current_login']]
    return menu.prompt([menu.List(
        'my_posting_target',
        message='Choose your posting for more information',
        choices=config.get_list_jobs(user, my_posts=True) + ['Go Back'],
        carousel=True
    )])


def print_application_list_screen():
    user = config['accounts'][config['current_login']]
    return menu.prompt([menu.List(
        'my_application_target',
        message='Choose your application',
        choices=config.get_list_jobs(user, my_apps=True) + ['Go Back'],
        carousel=True
    )])


def print_saved_list_screen():
    user = config['accounts'][config['current_login']]
    return menu.prompt([menu.List(
        'saved_list_target',
        message='Choose from your saved posts',
        choices=config.get_list_jobs(user, saved=True) + ['Go Back'],
        carousel=True
    )])


def print_unsave_posting_screen(job_id: str):
    return menu.prompt([menu.List(
        'unsave_posting_target',
        message='What would you like to do with your posting',
        choices=['Delete this saved posting: ' + job_id, 'Go Back'],
        carousel=True
    )])


def print_delete_posting_screen(job_id: str):
    return menu.prompt([menu.List(
        'delete_posting_target',
        message='What would you like to do with your posting',
        choices=['Delete this posting: ' + job_id, 'Go Back'],
        carousel=True
    )])


def print_application_screen(job_id: str):
    return menu.prompt([menu.List(
        'application_target',
        message='What would you like to do',
        choices=[
            'Apply for this job: ' + job_id,
            'Save this job: ' + job_id,
            'Go Back'
        ],
        carousel=True
    )])


def print_withdrawal_screen(job_id: str):
    return menu.prompt([menu.List(
        'withdraw_target',
        message='What would you like to do',
        choices=['Withdraw from this job: ' + job_id, 'Go Back'],
        carousel=True
    )])


def print_friend_list_screen(key) -> dict:
    user = config['accounts'][config['current_login']]
    choices = []
    # Friend list handling.
    if key == 'friends':
        accounts = user[key]
        if len(accounts) == 0:
            choices.append('No Connections')
        else:
            for account in accounts:
                choices.append(f'View profile of {account}')
                choices.append(f'Disconnect from {account}')
    # Pending requests handling.
    elif key == 'friend_requests':
        requests = user[key]
        if len(requests) == 0:
            choices.append('No Requests')
        else:
            for account in requests:
                choices.append(f'Accept friend request of {account}')
                choices.append(f'Decline friend request of {account}')
    # Friend search handling
    else:
        inputs = menu.prompt([
            menu.Text('key', 'Search by: lastname, university, or major'),
            menu.Text('value', 'Enter search parameter')
        ])
        key, value = inputs['key'], inputs['value']
        print(f'{key}   {value}')
        results = config.search_student(key, value)
        if len(results) == 0:
            choices.append('No results')
        else:
            for account in results:
                choices.append(f'Request to connect with {account}')
    choices.append('Go Back')
    return menu.prompt([menu.List(
        'friend_list_target',
        message='to be changed',
        choices=choices,
        carousel=True
    )])


def ask_for_login() -> dict:
    return menu.prompt([
        menu.Text('login_username', 'Enter your username'),
        menu.Text('login_password', 'Enter your password')
    ])


def ask_for_signup():
    return menu.prompt([
        menu.Text('signup_username', 'Enter your new username'),
        menu.Text('signup_password', 'Enter your new password (strong)'),
        menu.Text('signup_firstname', 'Enter your first name'),
        menu.Text('signup_lastname', 'Enter your last name'),
        menu.Text('signup_membership', 'Enter pro to subscribe to $10/mo plan')
    ])


def ask_for_fullname() -> dict:
    return menu.prompt([
        menu.Text('friend_first', 'Enter your friend\'s first name'),
        menu.Text('friend_last', 'Enter your friend\'s last name')
    ])


def ask_for_email() -> dict:
    return menu.prompt([
        menu.Text('email_recipient', 'Enter the recipient\'s username'),
        menu.Text('email_message', 'Enter the message')
    ])


def ask_job_application() -> dict:
    return menu.prompt([
        menu.Text('grad_date', 'Enter your graduation date (MM/DD/YYYY)'),
        menu.Text('start_date', 'Enter your expected start date (MM/DD/YYYY)'),
        menu.Text('app_text', 'Why you are a good fit')
    ])


def ask_job_posting() -> dict:
    return menu.prompt([
        menu.Text('job_title', 'Enter job title'),
        menu.Text('job_description', 'Enter job description'),
        menu.Text('job_employer', 'Enter company name'),
        menu.Text('job_location', 'Enter location (city, state)'),
        menu.Text('job_salary', 'Enter salary (format: $/month)')
    ])


def edit_profile(selection) -> None:
    """Edit selection of the profile that was chosen by the user."""
    login = config['current_login']
    profile = config['accounts'][login]['profile']
    if selection != 'education' and selection != 'experience':
        inp = menu.prompt([menu.Text('edit', f'Enter a new {selection}')])
        edit = inp['edit']
        if selection == 'major' or selection == 'university':
            edit = edit.title()
        profile[selection] = edit
        config.save_profile(login, profile)
    elif selection == 'experience':
        if len(profile[selection]) < 3:
            inp = menu.prompt([
                menu.Text('title', 'Enter title for experience'),
                menu.Text('employer', 'Enter employer'),
                menu.Text('date_started', 'Enter date started'),
                menu.Text('date_ended', 'Enter date ended'),
                menu.Text('location', 'Enter the location'),
                menu.Text('description', 'Enter a description')
            ])
            profile[selection].append(inp)
            config.save_profile(login, profile)
        else:
            print('Maximum Experiences')
    elif selection == 'education':
        inp = menu.prompt([
            menu.Text('name', 'Enter the school name'),
            menu.Text('degree', 'Enter your degree'),
            menu.Text('years', 'Enter your years attended')
        ])
        profile[selection].append(inp)
        config.save_profile(login, profile)


def edit_friends_list(
        current_user: str,
        current_friends: list,
        friend_username: str,
        friend_friends: list
) -> None:
    """Saves appropriate lists of friends of respective usernames."""
    current_friends.remove(friend_username)
    config.save_friends(current_user, current_friends)
    # Perform the same for friend.
    friend_friends.remove(current_user)
    config.save_friends(friend_username, friend_friends)

def print_training_screen():
 return menu.prompt([menu.List(
        'training_target',
        message='Training',
        choices=[
            'Training and Education',
            'IT Help Desk',
            'Business Analysis and Strategy',
            'Security',
            'Go Back'
        ]
    )])
def print_training_education_screen():
    return menu.prompt([menu.List(
        'training_education_target',
        message='Training and Education',
        choices=[
            '1 option - to be changed',
            '2 option - to be changed',
            '3 option - to be changed',
            '4 option - to be changed',
            'Go Back'
        ]
    )])

def print_business_screen():
    return menu.prompt([menu.List(
        'business_target',
        message='Trending Courses',
        choices=[
            'How to use In College Learning',
            'Train the trainer',
            'Gamification of Learning',
            "Not seeing what you're looking for? Sign in to see all 7,609 results",
            'Go Back'
        ]
    )])

def print_courses_screen():
    courses = config['courses']
    choices2 = []
    username = config.config['current_login']
    for course in courses:
        if course in config.config['accounts'][username]['courses']:
            course = course + '- Completed'
        choices2.append(course)

    choices2.append('Go Back')
    return menu.prompt([menu.List(
        'course_target',
        message='Choose a course',
        choices = choices2
    )])

def print_taken_course_screen():
    return menu.prompt([menu.List(
        'taken_target',
        message='You have already taken this course, do you want to take it again?',
        choices=['Yes',
                 'No'
        ]
    )])
def user_loop(new_config: utils.InCollegeConfig) -> None:
    """Main driver for the user interaction."""
    print('-#- 🎓 WELCOME TO THE IN COLLEGE CLI! 🎓 -#-\n')
    global config  # TODO: needs a fix, remove globals.
    config = new_config
    # TODO: Remove these initial assignments.
    inputs = None
    logged_in_user = config['current_login']
    logged_in_user_membership = config['current_login_membership']
    current_email = None

    while True:
        # config = utils.InCollegeConfig()
        config.process_all_APIs()
        # Welcome screen when inputs are empty.
        if inputs is None:
            # Print out first menu options.
            inputs = print_welcome_screen()
        # Selection from welcome screen.
        if 'welcome_target' in inputs:
            if inputs['welcome_target'] == 'Connect to friends':
                info = ask_for_fullname().values()
                print()
                if config.full_name_exists(*info):
                    # Print connect screen if user exists.
                    inputs = print_connect_screen()
                else:
                    # Go back to welcome screen if user is not found.
                    inputs = print_welcome_screen()
            elif inputs['welcome_target'] == 'Skip':
                # Print login screen when user selects 'skip' on welcome.
                inputs = print_login_screen()
            else:
                break
        # Selection from connect screen.
        if 'connect_target' in inputs:
            if inputs['connect_target'] == 'Log in':
                # If there login field is not empty, i.e., user is logged in.
                if config['current_login'] != '':
                    print('🔑 You were already logged in.')
                    inputs = print_main_screen()
                else:
                    info = ask_for_login().values();
                    print()
                    if config.login_valid(*info):
                        # Save login and print main screen if login correct.
                        inputs = print_main_screen()
                    else:
                        # Print connect screen if login is not correct.
                        inputs = print_connect_screen()
            elif inputs['connect_target'] == 'Sign up to join friends':
                info = ask_for_signup().values()
                print()
                if config.create_user(*info):
                    inputs = print_main_screen()
                else:  # Error was detected.
                    inputs = print_connect_screen()
            else:
                inputs = print_welcome_screen()
        if 'my_application_target' in inputs:
            if inputs['my_application_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['my_application_target'].split()[0]
                config.display_job(job_id)
                inputs = print_withdrawal_screen(job_id)
        if 'withdraw_target' in inputs:
            if inputs['withdraw_target'] != 'Go Back':
                user = config['current_login']
                job_id = inputs['withdraw_target'].split()[-1]
                config.withdraw_application(user, job_id)
            inputs = print_application_list_screen()
        if 'application_target' in inputs:
            if inputs['application_target'] != 'Go Back':
                user = config['current_login']
                # Grab the job id listed in the string from choices.
                job_id = inputs['application_target'].split()[-1]
                # Apply for a job by adding it to the list of user apps.
                if inputs['application_target'].split()[0] == 'Apply':
                    info = ask_job_application().values();
                    print()
                    config.submit_application(user, job_id, *info)
                else:
                    config.save_application(user, job_id)
            # Go back in any case.
            inputs = print_job_list_screen()
        if 'posting_target' in inputs:
            if inputs['posting_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['posting_target'].split()[0]
                config.display_job(job_id)
                inputs = print_application_screen(job_id)
        if 'delete_posting_target' in inputs:
            if inputs['delete_posting_target'] != 'Go Back':
                user = config['current_login']
                job_id = inputs['delete_posting_target'].split()[-1]
                config.delete_posting(job_id)
            inputs = print_postings_list_screen()
        if 'my_posting_target' in inputs:
            if inputs['my_posting_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['my_posting_target'].split()[0]
                config.display_job(job_id)
                inputs = print_delete_posting_screen(job_id)
        if 'unsave_posting_target' in inputs:
            if inputs['unsave_posting_target'] != 'Go Back':
                user = config['current_login']
                job_id = inputs['unsave_posting_target'].split()[-1]
                config.unsave_posting(job_id)
            inputs = print_saved_list_screen()
        if 'saved_list_target' in inputs:
            if inputs['saved_list_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['saved_list_target'].split()[0]
                config.display_job(job_id)
                inputs = print_unsave_posting_screen(job_id)
        if 'internship_target' in inputs:
            if inputs['internship_target'] == 'Post a job':
                info = ask_job_posting().values();
                print()
                config.create_posting(config['current_login'], *info)
                inputs = print_internship_screen()
            elif inputs['internship_target'] == 'Apply for a job':
                inputs = print_job_list_screen()
            elif inputs['internship_target'] == 'Show my applications':
                inputs = print_application_list_screen()
            elif inputs['internship_target'] == 'Show my postings':
                inputs = print_postings_list_screen()
            elif inputs['internship_target'] == 'Show my saved jobs':
                inputs = print_saved_list_screen()
            else:
                inputs = print_job_screen()
        if 'job_target' in inputs:
            if inputs['job_target'] == 'Internships':
                inputs = print_internship_screen()
            else:  # Go back was selected.
                inputs = print_main_screen()
        if 'skill_target' in inputs:
            if inputs['skill_target'] == 'Go back':
                inputs = print_main_screen()
            else:
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_main_screen()
        if 'main_target' in inputs:
            if inputs['main_target'] == 'Search for a job':
                inputs = print_job_screen()
            elif inputs['main_target'] == 'Message center':
                inputs = print_message_screen()
            elif inputs['main_target'] == 'Find someone':
                info = ask_for_fullname().values()
                print()
                config.full_name_exists(*info)
                inputs = print_main_screen()
            elif inputs['main_target'] == 'Learn a new skill':
                inputs = print_skill_screen()
            elif inputs['main_target'] == 'Friends':
                inputs = print_friend_screen()
            elif inputs['main_target'] == 'Profile':
                inputs = print_profile_screen()
            elif inputs['main_target'] == 'Useful Links':
                inputs = print_ulinks_screen()
            elif inputs['main_target'] == 'InCollege Important Links':
                inputs = print_ilinks_screen()
            elif inputs['main_target'] == 'InCollege Learning':
                inputs = print_courses_screen()
            elif inputs['main_target'] == 'Log out':
                config.save_login('')  # reset login "cookie".
                inputs = print_login_screen()
        # Selection from login screen.
        if 'login_target' in inputs:
            if inputs['login_target'] == 'Sign in':
                if config['current_login'] != '':
                    print('🔑 You were already logged in.')
                    inputs = print_main_screen()
                else:
                    info = ask_for_login().values()
                    print()
                    if config.login_valid(*info):
                        inputs = print_main_screen()
                    else:
                        inputs = print_login_screen()
            elif inputs['login_target'] == 'Sign up':
                info = ask_for_signup().values()
                print()
                if config.create_user(*info):
                    inputs = print_main_screen()
                else:  # Error was detected.
                    inputs = print_login_screen()
            elif inputs['login_target'] == 'Go back':  # Reuse code.
                inputs = print_welcome_screen()
            elif inputs['login_target'] == 'Watch a video':
                print('⚠️🚨 Playing video 🎥. Under construction. 🚨⚠️')
                inputs = print_login_screen()
            elif inputs['login_target'] == 'Useful Links':
                inputs = print_ulinks_screen()
            elif inputs['login_target'] == 'InCollege Important Links':
                inputs = print_ilinks_screen()
            elif inputs['login_target'] == 'Search for a job':
                if config['current_login'] != '':
                    inputs = print_job_screen()
                else:
                    print('Please log in first\n')
                    inputs = print_login_screen()
            elif inputs['login_target'] == 'Training': 
                inputs = print_training_screen()
        # Selection from training screen
        if 'training_target' in inputs:
            if inputs['training_target'] == 'Training and Education':
                inputs = print_training_education_screen()
            elif inputs['training_target'] == 'IT Help Desk':
                print('Coming Soon!')
                inputs = print_training_screen()
            elif inputs['training_target'] == 'Business Analysis and Strategy':
                inputs = print_business_screen()
            elif inputs ['training_target'] == 'Security':
                print("Coming Soon!")
                inputs = print_training_screen()
            elif inputs['training_target'] == 'Go Back':
                inputs = print_login_screen()
        #Selection from training and education screen
        if 'training_education_target' in inputs:
            if inputs ['training_education_target'][0] == '1':
                print('Under construction')
                inputs = print_training_education_screen()
            elif inputs['training_education_target'][0] == '2':
                print('Under Construction')
                inputs = print_training_education_screen()
            elif inputs['training_education_target'][0] == '3':
                print('Under Construction')
                inputs = print_training_education_screen()
            elif inputs['training_education_target'][0] == '4':
                print('Under Construction')
                inputs = print_training_education_screen()
            elif inputs['training_education_target'] == 'Go Back':
                inputs = print_training_screen()
        #Selection from business screen
        if 'business_target' in inputs:
            if inputs['business_target'] == 'Go Back':
                inputs = print_training_screen()
            else:
                print('Login to learn more.')
                inputs = print_login_screen()
        #Selection from courses screen
        if 'course_target' in inputs:
            if inputs['course_target'][0] == 'H':
                if inputs['course_target'][-9:] == 'Completed':
                    inputs = print_taken_course_screen()
                else:
                    config.save_course(config.config['current_login'], inputs['course_target'])
                    print('You have now completed this training.')
                    inputs = print_courses_screen()
            elif inputs['course_target'][0] == 'T':
                if inputs['course_target'][-9:] == 'Completed':
                    inputs = print_taken_course_screen()
                else:
                    config.save_course(config.config['current_login'], inputs['course_target'])
                    print('You have now completed this training.')
                    inputs = print_courses_screen()
            elif inputs['course_target'][0:2] == 'Ga':
                if inputs['course_target'][-9:] == 'Completed':
                    inputs = print_taken_course_screen()
                else:
                    config.save_course(config.config['current_login'], inputs['course_target'])
                    print('You have now completed this training.')
                    inputs = print_courses_screen()
            elif inputs['course_target'][0] == 'U':
                if inputs['course_target'][-9:] == 'Completed':
                    inputs = print_taken_course_screen()
                else:
                    config.save_course(config.config['current_login'], inputs['course_target'])
                    print('You have now completed this training.')
                    inputs = print_courses_screen()
            elif inputs['course_target'][0] == 'P':
                if inputs['course_target'][-9:] == 'Completed':
                    inputs = print_taken_course_screen()
                else:
                    config.save_course(config.config['current_login'], inputs['course_target'])
                    print('You have now completed this training.')
                    inputs = print_courses_screen()
            elif inputs['course_target'] == 'Go Back':
                inputs = print_main_screen()
        #selection from course_taken_screen
        if 'taken_target' in inputs:
            if inputs['taken_target'] == 'Yes':
                print('You have now completed this training')
                inputs = print_courses_screen()
            elif inputs['taken_target'] == 'No':
                print('Course Cancelled')
                inputs = print_courses_screen()

     
        # Selection from useful links section.
        if 'ulinks_target' in inputs:
            if inputs['ulinks_target'] == 'General':
                inputs = print_general_screen()
            elif inputs['ulinks_target'] == 'Go back':
                if config['current_login'] != '':
                    inputs = print_main_screen()
                else:
                    inputs = print_login_screen()
            else:
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_ulinks_screen()
        # Selection from home screen.
        if 'general_target' in inputs:
            if inputs['general_target'] == 'Sign up':
                inputs = print_login_screen()
            elif inputs['general_target'] == 'Go back':
                inputs = print_ulinks_screen()
            else:
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_general_screen()
        # Selection from informative links.
        if 'ilinks_target' in inputs:
            if inputs['ilinks_target'] == 'Copyright Notice':
                print('Copyright @ 1980-2021, InCollege Inc. None Rights Reserved.')
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Guest Controls':
                if config['current_login'] != '':
                    inputs = print_guest_screen()
                else:
                    print('Please sign in to see the hidden content')
                    inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Languages':
                if config['current_login'] != '':
                    inputs = print_language_screen()
                else:
                    print('Please sign in to see the hidden content')
                    inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Go back':
                if config['current_login'] != '':
                    inputs = print_main_screen()
                else:
                    inputs = print_login_screen()
            else:
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_ilinks_screen()
        # Selection from privacy screen.
        if 'privacy_target' in inputs:
            if inputs['privacy_target'] == 'Guest Control':
                if config['current_login'] != '':
                    inputs = print_guest_screen()
                else:
                    print('❌ Error. Please sign in to see the hidden content')
                    inputs = print_privacy_screen()
            elif inputs['privacy_target'] == 'Go back':
                inputs = print_ilinks_screen()
        # Selection from guest screen.
        if 'guest_target' in inputs:
            config.save_guest_control(
                config['current_login'],
                inputs['guest_target']
            )
            config.show_guest_control(config['current_login'])
            inputs = print_ilinks_screen()
        # Selection from language screen.
        if 'language_target' in inputs:
            config.save_lang(
                config['current_login'],
                inputs['language_target']
            )
            config.show_lang(config['current_login'])
            inputs = print_ilinks_screen()
        # Selection from editing the profile screen.
        if 'profile_target' in inputs:
            if inputs['profile_target'] == 'View profile':
                config.display_profile(config['current_login'])
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile title':
                edit_profile('title')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile major':
                edit_profile('major')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile university':
                edit_profile('university')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile about':
                edit_profile('about')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile experience':
                edit_profile('experience')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile education':
                edit_profile('education')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Go Back':
                inputs = print_main_screen()
        # Selection from the friend section.
        if 'friend_target' in inputs:
            if inputs['friend_target'] == 'Show my Network':
                inputs = print_friend_list_screen('friends')
            elif inputs['friend_target'] == 'Search for Someone':
                inputs = print_friend_list_screen('search')
            elif inputs['friend_target'] == 'View Friend Requests':
                inputs = print_friend_list_screen('friend_requests')
            elif inputs['friend_target'] == 'Go Back':
                inputs = print_main_screen()
        # Selection from the friend list section.
        if 'friend_list_target' in inputs:
            if inputs['friend_list_target'][0] == 'N':
                inputs = print_friend_screen()
            elif inputs['friend_list_target'][0] == 'V':
                config.display_profile(inputs['friend_list_target'][16:])
                inputs = print_friend_list_screen('friends')
            elif inputs['friend_list_target'][0:2] == 'Di':  # Remove from friend list
                current_user = config['current_login']
                current_user_friends = config['accounts'][current_user]['friends']
                friend_username = inputs['friend_list_target'][16:]
                friend_friends = config['accounts'][friend_username]['friends']
                edit_friends_list(
                    current_user,
                    current_user_friends,
                    friend_username,
                    friend_friends
                )
                inputs = print_friend_list_screen('friends')
            elif inputs['friend_list_target'][0] == 'A':
                config.accept_friend_request(
                    config['current_login'],
                    inputs['friend_list_target'][25:]
                )
                inputs = print_friend_screen()
            elif inputs['friend_list_target'][0:2] == 'De':
                config.decline_friend_request(
                    config['current_login'],
                    inputs['friend_list_target'][26:]
                )
                inputs = print_friend_screen()
            elif inputs['friend_list_target'][0] == 'R':
                user = config['current_login']
                config.send_friend_request(
                    inputs['friend_list_target'][24:],
                    user
                )
                inputs = print_friend_screen()
            elif inputs['friend_list_target'] == 'Go Back':
                inputs = print_friend_screen()
        # Selection from message screen.
        if 'message_target' in inputs:
            if inputs['message_target'] == 'Send':
                email = ask_for_email()
                config.send_message(*email.values())
                inputs = print_message_screen()
            elif inputs['message_target'] == 'Inbox':
                inputs = print_inbox_screen()
            elif inputs['message_target'] == 'Available recipients':
                inputs = print_recipient_screen()
            elif inputs['message_target'] == 'Go back':
                inputs = print_main_screen()
        # Selection from inbox screen.
        if 'inbox_target' in inputs:
            if inputs['inbox_target'] == 'Go back':
                current_email = ""
                inputs = print_message_screen()
            else:
                current_email = inputs['inbox_target']
                inputs = print_inbox_operation_screen(current_email)
                config.mark_message_read(current_email)
        # Selection from inbox recipient.
        if 'recipient_target' in inputs:
            if inputs['recipient_target'] == 'Go back':
                inputs = print_message_screen()
            else:
                inputs = print_recipient_operation_screen(
                    inputs['recipient_target']
                )
        # Selection from message action screen.
        if 'inbox_operation_target' in inputs:
            if inputs['inbox_operation_target'] == 'Reply':
                config.reply_message(current_email)
                current_email = ""
                inputs = print_inbox_screen()
            elif inputs['inbox_operation_target'] == 'Delete':
                config.delete_message(current_email)
                current_email = ""
                inputs = print_inbox_screen()
            elif inputs['inbox_operation_target'] == 'Go back':
                inputs = print_inbox_screen()
        # Selection from recipient action screen.
        if 'recipient_operation_target' in inputs:
            if inputs['recipient_operation_target'] != 'Go back':
                message = input('Message to send:\n')
                matcher = re.search(
                    "Send a message to (.*)",
                    inputs['recipient_operation_target']
                )
                recipient = matcher.group(1)
                config.send_message(recipient, message)
                inputs = print_message_screen()
            else:
                inputs = print_message_screen()
    # Prints out when the loop breaks.
    print('-#- 🎓 THANKS FOR USING IN COLLEGE CLI!  -#-')


if __name__ == '__main__':
    config = utils.InCollegeConfig()
    config.process_all_APIs()
    user_loop(config)
