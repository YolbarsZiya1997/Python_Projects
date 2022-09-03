class Users:
    """Imitation of a user information"""

    def __init__(self, first_name, last_name, user_name, sex, email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.sex = sex
        self.email = email

    def describe_user(self):
        print(f"You are {self.first_name} {self.last_name}")
        print(f"Your user name is {self.user_name}")
        print(f"You are {self.sex}")
        print(f"Lastly your email is {self.email}")

    def greet_user(self):
        print(f"Oh hi there {self.user_name}, welcome aboard.")


user_1 = Users('Babur', 'Temur', 'Barlas', 'Male', 'barlas1322@gmail.com')
user_1.describe_user()
user_1.greet_user()

