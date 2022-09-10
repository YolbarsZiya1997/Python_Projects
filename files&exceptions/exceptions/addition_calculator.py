print("This is an addition calculator")
print("Press 'q' to exit")

while True:
    number_1 = input("Enter your first number: ")
    if number_1 == "q":
        break
    number_2 = input("Enter your second number: ")
    if number_2 == "q":
        break
    try:
        answer = int(number_1) + int(number_2)
    except ValueError:
        print("Only numbers are accepted!")
    else:
        print(answer)
