print("This is a addition app")
print("Please only input numbers")

number_1 = input("Enter your firs number: ")
number_2 = input("Enter your second number: ")

try:
    answer = int(number_1) + int(number_2)
except ValueError:
    print("Please only enter numbers, texts are not acceptable")
else:
    print(answer)