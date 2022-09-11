import json


def get_user_name():
    """Get the username"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except ValueError:
        return None
    else:
        return username


def get_new_username():
    """Get a new username"""
    filename = 'username.json'
    username = input("Input your name: ")
    with open(filename, 'a') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user"""
    filename = 'username.json'
    username = input("What is your name")
    if username in filename:
        print(f"Welcome back {username}")
    else:
        print("So you are new here!")
        username = get_new_username()
        print(f"We'll remember you next time {username}")


greet_user()