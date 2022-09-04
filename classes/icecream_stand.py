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


class IceCreamStand(Restaurant):
    """An attempt to imitate an ice cream stand"""

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavor = ["straw berry", "lemon", "chocolate", "vanilla"]

    def flavor_reader(self):
        print("We have the following flavors in our store")
        for flavors in self.flavor:
            print(flavors)


marujna = IceCreamStand('Doghapchi', 'Ice cream')
marujna.flavor_reader()