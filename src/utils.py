import json
import datetime
import string
import os
import re
from random import randint


class TextColor:
    RESET = '\033[0m'
    NOTIFICATION = '\033[92m'


class InCollegeConfig:
    """
    This is a configuration class that stores all necessary text
    and user information that is used for user interface, communication,
    and content.
    """

    def __init__(self, filename='config.json'):
        """Initialize config by reading json from a given file."""
        self.filename = filename
        self.config = json.load(open(filename, 'r'))

    def __getitem__(self, key):
        """Allow calling self['thing'] instead of self.config['thing']."""
        return self.config[key]

    def __setitem__(self, key, value):
        """Allow setting self['thing'] = val instead of self.config[..."""
        self.config[key] = value

    def save_config(self) -> None:
        """Write current config to file with utf-8 indentation."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
            f.write('\n')  # linux convention.

    def full_name_exists(self, first: str, last: str) -> bool:
        """Check whether given first and last names exist."""
        exists = any([self['accounts'][account]['firstname'] == first and \
                      self['accounts'][account]['lastname'] == last for \
                      account in self['accounts']])
        if exists:
            print(f'🎉 {first} is InCollege! Hooray!')
        else:
            print('🎓 They are not part of our system. Invite them!')
        return exists

    def login_valid(self, username: str, password: str) -> bool:
        """Check whether login/password combination is valid."""
        valid = username in self['accounts'] and \
                self['accounts'][username]['password'] == password
        if valid:
            print(f'🔑 You are logged in. Welcome {username}')
            self.save_login(username)
            self.notification_center(username)
        else:
            print('❌ Credentials invalid. Please try again')
        return valid

    def username_exists(self, username: str) -> bool:
        """Check whether given username exists."""
        return username in self['accounts']

    def password_valid(self, password: str) -> bool:
        """Validate password based on provided guidelines."""
        cap_flag = any([char.isupper() for char in password])
        digit_flag = any([char.isdigit() for char in password])
        special_flag = any([char in string.punctuation for char in password])
        len_flag = 8 <= len(password) <= 12
        if not cap_flag:
            print('❌ Password needs to contain at least 1 capital letter.')
        if not digit_flag:
            print('❌ Password needs to contain at least 1 digit.')
        if not special_flag:
            print('❌ Password needs to contain at least 1 special character')
        if not len_flag:
            print('❌ Password needs to be between 8 and 12 characters long')
        return all([cap_flag, digit_flag, special_flag, len_flag])

    #
    def create_user(
            self,
            username: str,
            password: str,
            firstname: str,
            lastname: str,
            membership: str
    ) -> bool:
        """Validate user information and create new entry in the config."""
        num_users_flag = len(self['accounts']) >= 10
        password_flag = not self.password_valid(password)
        username_flag = self.username_exists(username)
        if num_users_flag:
            print('❌ Too many users in the system. Try again later.')
        if username_flag:
            print('❌ Current username already has an account.')
        if any([num_users_flag, password_flag, username_flag]):
            return False
        else:
            self['accounts'][username] = {
                'password': password,
                'firstname': firstname,
                'lastname': lastname,
                'membership': '',
                'language': 'English',
                'profile': {
                    'title': '',
                    'major': '',
                    'university': '',
                    'about': '',
                    'experience': [],
                    'education': []
                },
                'friends': [],
                'friend_requests': [],
                'applications': {},  # is this a dict or list the config.json shows dict yet here it's a list
                'saved_jobs': [],
                'inbox': [],
                'time_stamps': {
                    'log_out': '\"2000-01-01 00:00:00.000000\"',
                    'job_applied': '\"2000-01-01 00:00:00.000000\"',
                    'user_registered': '\"2000-01-01 00:00:00.000000\"'
                },
                'courses': []
            }

            if membership.strip().lower() == 'pro':
                self['accounts'][username]['membership'] = 'pro'
            # Write new config to json file.
            self.time_stamp_update('user_registered')
            self.time_stamp_update('user_registered', username)
            self.save_config()
            print(f'✅ User {username} has been created')
            if self['current_login'] == '':
                self.save_login(username)
            return True

    def create_posting(
            self,
            author: str,
            title: str,
            description: str,
            employer: str,
            location: str,
            salary: str
    ) -> bool:
        """Create a job posting and update the json config file."""
        # Inefficient, but creates a new id by storing all previous in a set.

        for job in self['jobs']:
            if title == job['title']:
                print('❌ Job title existed. Try again later.')
                return False

        ids = set()
        for job in self['jobs']:
            ids.add(job['id'])
        # Generate new id while it clashes with existing ones.
        new_id = randint(1, 100)
        while new_id in ids:
            new_id = randint(1, 100)
        fullname = self['accounts'][author]['firstname'] + ' ' + \
                   self['accounts'][author]['lastname']
        self['jobs'].append({
            'author': fullname,
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'id': str(new_id)
        })

        if len(self['jobs']) >= 10:
            print('❌ Too many jobs in the system. Try again later.')
            return False
        else:
            self.time_stamp_update('job_posted')
            self.save_config()
            print(f'✅ New posting for {title} has been created!')
            if salary.lower() == 'unpaid':  # Easter egg.
                print('🤨 Unpaid position? We aren\'t into charity business.')
            return True

    def delete_posting(self, job_id: str):
        # Remove job from available postings.
        for job in self['jobs']:
            if job['id'] == job_id:
                self['jobs'].remove(job)
        # Remove job from user's application lists.
        for user in self['accounts']:
            if job_id in self['accounts'][user]['applications']:
                del self['accounts'][user]['applications'][job_id]
        # Save updated config.
        self.time_stamp_update('job_deleted')
        self.save_config()
        # Print success message.
        print(f'✅ Success! Posting {job_id} and associated apps were removed.')

    def unsave_posting(self, job_id: str):
        user = self['accounts'][self['current_login']]
        user['saved_jobs'].remove(job_id)
        print(f'✅ Success! Posting {job_id} has been removed from saved.')
        self.save_config()

    def save_login(self, username: str) -> None:
        """Update current logged in user and write changes to json file."""
        self['current_login'] = username
        if username != '':
            self['current_login_membership'] = self['accounts'][username]['membership']
        else:
            self['current_login_membership'] = ''
            self.time_stamp_update('log_out', self['current_login'])
        self.save_config()

    def save_guest_control(self, username: str, control_setting_list: dict) -> None:
        """Update current guest control setting in user's privacy setting."""
        self['guest_control'].update({username: control_setting_list})
        self.save_config()

    def show_guest_control(self, username: str) -> None:
        """Display the current guest control setting of the current user."""
        guest_control_list = ['InCollege Email', 'SMS', 'Targeted Advertising features']
        print('Your current guest control setting: ')
        # Equivalent to the commented section below
        list(map((lambda x: print(x + ': ' + 'ON')
        if x in self['guest_control'][username]
        else print(x + ': ' + 'OFF')), guest_control_list))

    def save_lang(self, username: str, lang: str) -> None:
        """Update current lang setting in user and write changes to json file."""
        self['accounts'][username]['language'] = lang
        self.save_config()

    def show_lang(self, username: str) -> None:
        """Display the lang setting for the current user."""
        print('Your current language setting: ')
        print(self['accounts'][username]['language'])

    def save_profile(self, username: str, profile: dict) -> None:
        """Update profile of user and write changes to json file."""
        self['accounts'][username]['profile'] = profile
        self.save_config()

    def display_profile(self, username: str) -> None:
        '''Displays a user profile'''
        if self.username_exists(username):
            user = self['accounts'][username]
            profile = user['profile']
            firstname = user['firstname']
            lastname = user['lastname']
            print('{} {}'.format(firstname, lastname))
            # For all keys within the profile.
            for k, v in profile.items():
                if k != 'experience' and k != 'education':
                    print(f'{k}: {v}')
                else:
                    print(f'{k}:')
                    # For every element in the education/experience section.
                    for entry in v:
                        # For each entry in the section of element/education.
                        for entry_k, entry_v in entry.items():
                            print(f'   {entry_k}: {entry_v}')
                        print('')
        else:
            print(f'❌ Error. User {username} does not exist.')

    def display_job(self, job_id: str) -> None:
        """Display job information based on requested job id."""
        # The job is guaranteed to exist, since it's retrieved from config.
        for job in self['jobs']:
            if job['id'] == job_id:
                print('Job information is displayed below:')
                print(f'✍️  Posted by: {job["author"]}')
                print(f'🧑 Role: {job["title"]}')
                print(f'📝 Description: {job["description"]}')
                print(f'🕴️  Employer: {job["employer"]}')
                print(f'🏙️  Location: {job["location"]}')
                print(f'💰 Salary: {job["salary"]}')

    def submit_application(
            self,
            user: str,
            job_id: str,
            grad_date: str,
            start_date: str,
            brief: str
    ) -> None:
        """Apply for a job by adding the id into user's application list."""
        jobs = self['jobs']
        current_user = self['accounts'][self['current_login']]
        fullname = current_user['firstname'] + ' ' + current_user['lastname']
        for job in jobs:
            if job_id in job['id'] and job['author'] == fullname:
                print('❌ Error. You cannot apply a job posted by yourself.')
                return
        print(f'✅ Success! You have applied to the job {job_id}! 🎉')
        self.time_stamp_update('job_applied', self['current_login'])
        if job_id in self['accounts'][user]['applications']:
            print('❌ Error. You have applied this job.')
            return
        self['accounts'][user]['applications'][job_id] = {
            'grad_date': grad_date,
            'start_date': start_date,
            'app_text': brief
        }
        self.save_config()

    def withdraw_application(self, user: str, job_id: str) -> None:
        """Withdraw application by removing it from user's application list."""
        print(f'✅ Success. The application {job_id} was withdrawn.')
        # del may throw an error when the job_id is non-existed
        # del self['accounts'][user]['applications'][job_id]
        # try to delete a non-existed key. This will return None.
        self['accounts'][user]['applications'].pop(job_id, None)
        self.save_config()

    def save_application(self, user: str, job_id: str) -> None:
        print(f'✅ Success. The application {job_id} was saved.')
        if job_id not in self['accounts'][user]['saved_jobs']:
            self['accounts'][user]['saved_jobs'].append(job_id)
        self.save_config()

    def get_list_jobs(
            self,
            user: dict,
            browse=False,
            my_apps=False,
            my_posts=False,
            saved=False
    ) -> list:
        """Return a list of jobs to be displayed in the menu based on user."""
        jobs = list()
        # Create a list of flags to filter the jobs with.
        fullname = user['firstname'] + ' ' + user['lastname']
        all_jobs = not my_apps and not my_posts and not saved and not browse
        for job in self['jobs']:
            in_applications = job['id'] in user['applications']
            in_saved = job['id'] in user['saved_jobs']
            is_author = fullname == job['author']
            if (browse and not in_applications and not is_author or
                    my_apps and in_applications or
                    my_posts and is_author or
                    saved and in_saved or
                    all_jobs):
                # FIlter job based on the flag provided.
                ind = '✅ ' if all_jobs and in_applications else ''
                ind += '🔖 ' if all_jobs and in_saved else ''
                job_line = [job['id'], ind + job['title'], job['location']]
                jobs.append(' | '.join(job_line))
        return jobs

    def search_student(self, key: str, val: str):
        """Returns an array of all the account usernames that match key/val."""
        valid_keys = ["lastname", "major", "university"]
        accounts, matches = self['accounts'], []
        if key in valid_keys:
            for user, data in accounts.items():
                is_login = user == self['current_login']
                is_fr = self['current_login'] in accounts[user]['friends']
                if (key == 'lastname' and data[key] == val or
                    ((key == 'major' or key == 'university') and
                     data['profile'][key] == val)) and not (is_login or is_fr):
                    matches.append(user)
        return matches

    def display_friends(self, username: str):
        user = self['accounts'][username]
        if len(user['friends']) == 0:
            print('None')
        else:
            for friend_username in user['friends']:
                self.display_profile(friend_username)
                print(' ')

    def save_friends(self, username: str, friendList: list) -> None:
        """Update friends list and write to json"""
        self['accounts'][username]['friends'] = friendList
        self.save_config()

    def send_friend_request(self, target_user: str, sender: str) -> None:
        """Update friend_requests list and write to json"""
        self['accounts'][target_user]['friend_requests'].append(sender)
        self.save_config()

    def accept_friend_request(self, user: str, accepted_username: str) -> None:
        self['accounts'][user]['friends'].append(accepted_username)
        self['accounts'][user]['friend_requests'].remove(accepted_username)

        self['accounts'][accepted_username]['friends'].append(user)
        self.save_config()

    def decline_friend_request(self, user: str, declined_username: str) -> None:
        self['accounts'][user]['friend_requests'].remove(declined_username)
        self.save_config()

    def mark_message_read(self, email: str) -> None:
        inbox = self['accounts'][self['current_login']]['inbox']
        matcher = re.search("(.*): (.*)", email)
        sender = matcher.group(1)
        message = matcher.group(2)
        if '[unread]' in email:
            marked_message = message.replace('[unread]', '', 1)
            counter = 0
            for element in inbox:
                if sender in element and (element[sender] == message):
                    inbox[counter][sender] = marked_message
                counter += 1
        self.save_config()

    def send_message(self, recipient: str, message: str) -> None:
        email = {self['current_login']: '[unread]' + message}
        if recipient == '':
            print('\n❌ Please do not leave the recipient and the message blank.\n')
        elif recipient == self['current_login']:
            print('\n❌ You need a friend.\n')
        elif recipient in self['accounts']:
            if self['current_login_membership'] != 'pro' and recipient.strip() not in \
                    self['accounts'][self['current_login']]['friends']:
                print('\n❌ Standard user can not send message to whom are not your friend.\n')
            else:
                self['accounts'][recipient]['inbox'].append(email)
                print('\n✅ Your message has been sent.\n')
        else:
            print('\n❌ The recipient does not exist.\n')
        self.save_config()

    def reply_message(self, email: string) -> None:
        matcher = re.search("(.*):", email)
        sender = matcher.group(1)
        reply_message = input('Reply: \n')
        reply_message = '[unread]' + reply_message
        reply = {self['current_login']: reply_message}
        self['accounts'][sender]['inbox'].append(reply)
        self.save_config()

    def delete_message(self, email: string) -> None:
        matcher = re.search("(.*): (.*)", email)
        sender = matcher.group(1)
        message = matcher.group(2)
        marked_message = message.replace('[unread]', '', 1)
        counter = 0
        for element in self['accounts'][self['current_login']]['inbox']:
            if sender in element and (element[sender] == message or element[sender] == marked_message):
                self['accounts'][self['current_login']]['inbox'].pop(counter)
            counter += 1
        self.save_config()

    def notification_center(self, username: str,
                            job_notify=True,
                            profile_alert=True,
                            unread_msg=True,
                            job_posted=True,
                            job_deleted=True,
                            new_user=True,
                            job_num=False
                            ) -> None:
        print(TextColor.NOTIFICATION + 'Notification Center: ')
        if job_notify:
            self.if_job_notification(username)
        if profile_alert:
            self.no_profile_notificaton(username)
        if unread_msg:
            self.unread_message_notification(username)
        if job_posted:
            self.job_posted_notification()
        if job_deleted:
            self.applied_job_deleted_notification()
        if new_user:
            self.new_user_notification()
        if job_num:
            self.num_job_notification(username)
        print(TextColor.RESET)

    @staticmethod
    def send_notification(message: str) -> str:
        print(message)
        return message

    @staticmethod
    def datetime_convert(data: datetime) -> str:
        if isinstance(data, datetime.datetime):
            return data.__str__()

    def json_time_convert(self, event: str, username: str = '') -> datetime:
        if username != '':
            json_time = self['accounts'][username]['time_stamps'][event]
        else:
            json_time = self['time_stamps'][event]
        time = datetime.datetime.strptime(json_time, '\"%Y-%m-%d %H:%M:%S.%f\"')  # "\"2021-11-02 02:09:10.286317\""
        return time

    def time_stamp_update(self, event: str, username: str = '') -> None:
        time = json.dumps(datetime.datetime.now(), default=self.datetime_convert)
        time_stamp = {event: time}
        if username != '':
            self['accounts'][username]['time_stamps'].update(time_stamp)
            self.save_config()
            return
        self['time_stamps'].update(time_stamp)
        self.save_config()

    def if_job_notification(self, username: str) -> None:
        # Happens once every time you logs in
        # Resuming will not trigger this function
        time_stamps = self['accounts'][username]['time_stamps']
        message = 'Remember – you\'re going to want to have a job when you graduate.\n' \
                  'Make sure that you start to apply for jobs today!'
        # new create user function now initialize the time stamp of job_applied
        # though not all old users have that
        if 'job_applied' not in time_stamps:
            self.send_notification(message)
            return
        time_diff = datetime.datetime.now() - self.json_time_convert('job_applied', username)
        if time_diff.days >= 7:
            self.send_notification(message)
        self.save_config()

    def no_profile_notificaton(self, username: str) -> None:
        profile = self['accounts'][username]['profile']
        message = 'Don\'t forget to create a profile'
        if profile['title'].strip() == '' and profile['major'].strip() == '' and profile['university'].strip() == '' and \
                profile['about'].strip() == '' and len(profile['experience']) == 0 and len(profile['education']) == 0:
            self.send_notification(message)
        self.save_config()

    def unread_message_notification(self, username: str) -> None:
        inbox = self['accounts'][username]['inbox']
        message = 'You have messages waiting for you'
        for d in inbox:
            for k, v in list(d.items()):
                if '[unread]' in v:
                    self.send_notification(message)
                    return

    def num_job_notification(self, username: str) -> str:
        applications = self['accounts'][username]['applications']
        jobs_applied = len(applications)
        message = f'You have currently applied for {jobs_applied} jobs'
        self.send_notification(message)
        return message

    def job_posted_notification(self) -> str:
        if len(self['jobs']) != 0:
            title = self['jobs'][-1]['title']
            job_posted_time = self.json_time_convert('job_posted')
            log_out_time = self.json_time_convert('log_out', self['current_login'])
            message = f'new job {title} has been posted.'
            if job_posted_time > log_out_time:
                self.send_notification(message)
        return message

    def applied_job_deleted_notification(self) -> str:
        applications = self['accounts'][self['current_login']]['applications']
        jobs = self['jobs']
        saved_jobs = self['accounts'][self['current_login']]['saved_jobs']
        count = 0
        job_ids_in_applications = list(key for key in applications.keys())
        job_ids_updated = list(job['id'] for job in jobs)
        diff = list(filter(lambda x: x not in job_ids_updated, job_ids_in_applications))
        for job_id in diff:
            applications.pop(job_id, None)
            count += 1
        for job_id in saved_jobs:
            if job_id not in job_ids_updated:
                saved_jobs.remove(job_id)
        message = f'{count} job(s) that you applied for has been deleted'
        if count != 0:
            self.send_notification(message)
        self.save_config()
        return message

    def new_user_notification(self) -> str:
        log_out_time = self.json_time_convert('log_out', self['current_login'])
        for key, value in self['accounts'].items():
            registered_time = self.json_time_convert('user_registered', key)
            if registered_time > log_out_time:
                first_name = value['firstname']
                last_name = value['lastname']
                message = f'{first_name} {last_name} has joined InCollege'
                self.send_notification(message)
                return message

    def save_course(self, username: str, course: str) -> None:
        """ Saves the courses a user has completed"""
        self['accounts'][username]['courses'].append(course)
        self.save_config()

    def append_file(self, filename: str, new_content: str) -> None:
        """Write current config to file with utf-8 indentation."""
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(new_content)
            f.write('\n=====\n')  # linux convention.

    def clear_file(self, filename) -> None:
        with open(filename, 'w+', encoding='utf-8') as f:
            pass

    def process_all_APIs(self) -> None:
        self.process_student_account_API()
        self.process_job_API()
        self.process_training_API()
        self.process_profile_API()
        self.process_applied_job_API()
        self.process_saved_job_API()

    def process_student_account_API(self) -> None:
        with open('studentAccounts.txt', 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 5):
                username = lines[i].strip()
                firstname, lastname = lines[i + 1].split()
                password = lines[i + 2].strip()
                membership = lines[i + 3].strip()
                self.create_user(username, password, firstname, lastname, membership)

        self.clear_file('studentAccounts.txt')
        self.clear_file('MyCollege_users.txt')

        for account_name in self['accounts'].keys():
            username = account_name
            account_type = ' standard'
            if self['accounts'][username]['membership'] == 'pro':
                account_type = ' plus'
            self.append_file('MyCollege_users.txt', username + account_type)

    def process_job_API(self) -> None:
        with open('newJobs.txt', 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            i = 0
            while (i < len(lines)):
                title = lines[i].strip()
                description = ''
                while (lines[i + 1] != '&&&&&&&&&&&&&\n'):
                    description += lines[i + 1]
                    i += 1
                poster = lines[i + 2].strip()
                employer = lines[i + 3].strip()
                location = lines[i + 4].strip()
                salary = lines[i + 5].strip()
                i += 7

                if poster in self['accounts'].keys():
                    self.create_posting(poster, title, description, employer, location, salary)
                # if len(poster.split()) == 2:
                #     firstname, lastname = poster.split()
                #     for username in self['accounts'].keys():
                #         if firstname == self['accounts'][username]['firstname'] and lastname == self['accounts'][username]['lastname']:
                #             self.create_posting(poster, title, description, employer, location, salary)

        self.clear_file('newJobs.txt')
        self.clear_file('MyCollege_jobs.txt')

        for job in self['jobs']:
            title = job['title']
            description = job['description']
            employer = job['employer']
            location = job['location']
            salary = job['salary']
            content = title + '\n' + description + '\n' + employer + '\n' + location + '\n' + salary
            self.append_file('MyCollege_jobs.txt', content)

    def process_training_API(self) -> None:
        with open('newtraining.txt', 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            for course in lines:
                if course.strip() not in self['courses'] and course != '' and course != '=====\n':
                    self['courses'].append(course.strip())
                    print(f'✅ New course added.')
                    self.save_config()
                elif course.strip() in self['courses']:
                    print(f'❌ The course has already existed.')

        self.clear_file('newtraining.txt')
        self.clear_file('MyCollege_training.txt')

        for username in self['accounts'].keys():
            courses = ''
            for course in self['accounts'][username]['courses']:
                courses += '\n' + course
            self.append_file('MyCollege_training.txt', username + courses)

    def process_profile_API(self) -> None:
        self.clear_file('MyCollege_profiles.txt')
        for username in self['accounts'].keys():
            profile = self['accounts'][username]['profile']
            title = profile['title']
            major = profile['major']
            university = profile['university']
            about = profile['about']
            experience = ''
            for exp in profile['experience']:
                experience += (exp['title'] + '\n' + exp['employer'] + '\n' + exp['date_started'] + '\n' + exp[
                    'date_ended'] + '\n' + exp['location'] + '\n' + exp['description'] + '\n')
            education = ''
            for edu in profile['education']:
                education += (edu['name'] + '\n' + edu['degree'] + '\n' + edu['years'] + '\n')
            content = username + '\n' + title + '\n' + major + '\n' + university + '\n' + about + '\n' + experience + education
            self.append_file('MyCollege_profiles.txt', content)

    def process_applied_job_API(self) -> None:
        self.clear_file('MyCollege_appliedJobs.txt')
        for job in self['jobs']:
            content = job['title'] + '\n'
            for username in self['accounts'].keys():
                application = self['accounts'][username]['applications']
                if job['id'] in application.keys():
                    content += (username + '\n' + application[job['id']]['app_text'] + '\n')
            self.append_file('MyCollege_appliedJobs.txt', content)

    def process_saved_job_API(self) -> None:
        self.clear_file('MyCollege_savedJobs.txt')
        for username in self['accounts'].keys():
            saved_jobs = ''
            for job_id in self['accounts'][username]['saved_jobs']:
                for job in self['jobs']:
                    if job_id == job['id']:
                        saved_jobs += job['title'] + '\n'
            content = username + '\n' + saved_jobs
            self.append_file('MyCollege_savedJobs.txt', content)
