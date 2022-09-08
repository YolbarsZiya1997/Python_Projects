class Users:
    """An imitaiton of a user class """

    def __init__(self, first_name, last_name, user_name, email, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.sex = sex

    def user_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"User name: {self.user_name}")
        print(f"Sex: {self.sex}")
        print(f"Email address: {self.email}")

    def say_hello(self):
        print(f"Hello there {self.user_name}, long time no see")


class Privileges:
    """A privileges class"""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are some of the privileges: ")
        for privs in self.privileges:
            print(privs)


class Admin(Users):
    """An imitation of an admin class"""

    def __init__(self, first_name, last_name, user_name, email, sex):
        super().__init__(first_name, last_name, user_name, email, sex)
        self.privileges = Privileges()


my_vip_account = Admin("Baybars", "İlkhan", "Tulun", "karalungtagh@gmail.com", "Male")
admin_privs = ["can do what ever the fuck he wants",
               "he is a top G",
               "can ban people",
               "can swim in the pool"
               ]
my_vip_account.privileges.privileges = admin_privs
my_vip_account.privileges.show_privileges()


