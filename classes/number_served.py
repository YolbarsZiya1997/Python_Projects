class Restaurant:
    """An attempt to imitate a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name} is an {self.cuisine} restaurant")
        print(f"It serves traditional {self.cuisine} and western fusion dishes")

    def open_restaurant(self):
        print(f"The restaurant is open come on in")

    def set_number_served(self, servings):
        self.number_served = servings

    def increment_number_served(self, times):
        self.number_served += times

    def serving_reader(self):
        print(f"This restaurant have served {self.number_served} guests")


fav_restaurant = Restaurant('Zafer', 'Uyghur')
fav_restaurant.set_number_served(1000)
fav_restaurant.increment_number_served(200)
fav_restaurant.serving_reader()
