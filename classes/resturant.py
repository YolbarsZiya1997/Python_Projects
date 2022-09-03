class Restaurant:
    """An attempt to imitate a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine type"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name} is an {self.cuisine} restaurant")
        print(f"It serves traditional {self.cuisine} and western fusion dishes")

    def open_restaurant(self):
        print(f"The restaurant is open come on in")


my_fav = Restaurant('Zafer', 'Uyghur')
my_fav.describe_restaurant()
my_fav.open_restaurant()
print()
second_fav = Restaurant('Köklem', 'Uyghur')
second_fav.describe_restaurant()
second_fav.open_restaurant()
