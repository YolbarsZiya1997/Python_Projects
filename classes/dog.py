class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 9)

print(f"My dog's name is {my_dog.name}")
print(f"She is {my_dog.age} years old")
print(" ")
print(f"Your dog's name is {your_dog.name}")
print(f"She is {your_dog.age} years old, she is an old hag")
# Calling method
my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()