from car import ElectricCar, Car

my_tesla = ElectricCar("Tesla", "model s", 2019)
my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

