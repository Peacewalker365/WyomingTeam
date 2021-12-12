from flask import Flask, json, jsonify, request

app = Flask(__name__)
import utils

@app.route("/")
def index():
    return 'The InCollege APIs are Launched.'


@app.route('/api/in/users', methods=['GET', 'POST'])
def student_account_API():
    config = utils.InCollegeConfig()
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        firstname = data['firstName']
        lastname = data['lastName']
        membership = data['membership']
        content = username + '\n' + firstname + ' ' + lastname + '\n' + password + '\n' + membership
        config.append_file('studentAccounts.txt', content)
        # config.create_user(username, password, firstname, lastname, membership)
        return username + ": In Queue\n"

@app.route('/api/in/jobs', methods=['GET', 'POST'])
def job_API():
    config = utils.InCollegeConfig()
    if request.method == 'POST':
        data = request.get_json()
        poster = data['poster']
        title = data['title']
        description = data['description']
        employer = data['employer']
        location = data['location']
        salary = data['salary']

    content = title + '\n' + description + '\n&&&&&&&&&&&&&\n' + poster + '\n' + employer + '\n' + location + '\n' + salary
    config.append_file('newJobs.txt', content)
    return title + ": In Queue\n"

@app.route('/api/in/training', methods=['POST'])
def training_API():
    config = utils.InCollegeConfig()
    data = request.get_json()

    course = data['course']

    config.append_file('newtraining.txt', course)
    return course + ": In Queue\n"






if __name__ == '__main__':
    app.run(debug=True)
