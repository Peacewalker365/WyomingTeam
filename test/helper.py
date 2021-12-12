import json

def create_config(file_path: str) -> None:
    config = {
        "messages": {
            "welcome": "Welcome"
        },
        "time_stamps": {
            "job_deleted": "\"2000-01-01 00:00:00.000000\"",
            "job_posted": "\"2000-01-01 00:00:00.000000\"",
            "user_registered": "\"2000-01-01 00:00:00.000000\""
          },
        "jobs": [
            {
                "author": "Some Author",
                "title": "Software Engineer",
                "description": "Needs to test CLI applications",
                "employer": "Sunny Side Up LLC",
                "location": "San Jose, CA",
                "salary": "$7000 a month",
                "id": "2"
            },
            {
                "author": "Other Author",
                "title": "QA Engineer",
                "description": "Needs to QA robotics applications",
                "employer": "Pick Me Corp",
                "location": "Mountainview, CA",
                "salary": "$5500 a month",
                "id": "4"
            }
        ],
        "courses": [
            "Train the trainer",
            "Understanding the Architectural Design Process",
            "How to use InCollege learning",
            "Gamification of Learning",
            "Project Management Simplified",
            "How to get your first job!"
        ],
        "stories": [
            "Some story of a successful guy",
            "Another story of a very successful guy"
        ],
        "accounts": {
            "admin": {
                "password": "admin",
                "firstname": "admin",
                "lastname": "admin",
                "membership": "pro",
                "language": "English",
                "profile": {
                    "title": "admin",
                    "major": "admin",
                    "university": "admin",
                    "about": "admin",
                    "experience": [
                        {
                            "title": "admin",
                            "employer": "admin",
                            "date_started": "admin",
                            "date_ended": "admin",
                            "location": "admin",
                            "description": "admin"
                        }
                    ],
                    "education": []
                },
                "friends": [],
                "friend_requests": [],
                "saved_jobs": [],
                "applications": {},
                "inbox": [],
                "time_stamps": {
                    "log_out": "\"2000-01-01 00:00:00.000000\"",
                    "job_applied": "\"2000-01-01 00:00:00.000000\"",
                    "user_registered": "\"2000-01-01 00:00:00.000000\""
                    },
                "courses": []
            },
            "test": {
                "password": "test",
                "firstname": "test",
                "lastname": "test",
                "membership": "",
                "language": "Spanish",
                "profile": {
                    "title": "test",
                    "major": "test",
                    "university": "test",
                    "about": "test",
                    "experience": [
                        {
                            "title": "test",
                            "employer": "test",
                            "date_started": "test",
                            "date_ended": "test",
                            "location": "test",
                            "description": "test"
                        }
                    ],
                    "education": []
                },
                "friends": [],
                "friend_requests": [],
                "saved_jobs": [],
                "applications": {},
                "inbox": [],
                "time_stamps": {
                    "log_out": "\"2000-01-01 00:00:00.000000\"",
                    "job_applied": "\"2000-01-01 00:00:00.000000\"",
                    "user_registered": "\"2000-01-01 00:00:00.000000\""
                    },
                "courses": []
            }
        },
        "current_login": "",
        "current_login_membership": "",
        "guest_control": {
                "admin": ['InCollege Email']
        },
    }
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
        f.write('\n')

