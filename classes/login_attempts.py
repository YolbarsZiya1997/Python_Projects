class Users:
    """Imitation of a user information"""

    def __init__(self, first_name, last_name, user_name, sex, email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.sex = sex
        self.email = email
        self.login_attempt = 0

    def describe_user(self):
        print(f"You are {self.first_name} {self.last_name}")
        print(f"Your user name is {self.user_name}")
        print(f"You are {self.sex}")
        print(f"Lastly your email is {self.email}")

    def greet_user(self):
        print(f"Oh hi there {self.user_name}, welcome aboard.")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


new_user = Users('Attila', 'Arıgh', 'Qamcha', 'Male', 'scurgeofgod@gmail.com')
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(f"There were total {new_user.login_attempt} login attempts")
print()
new_user.reset_login_attempts()
print(f"There are total {new_user.login_attempt} login attempts")