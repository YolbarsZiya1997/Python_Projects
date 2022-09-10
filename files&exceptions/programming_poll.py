file_name = 'reasons.txt'

with open(file_name, "a") as file_object:
    while True:
        name = input("What is your name: ")
        reason = input(f"So {name} tell us why do like programming: ")
        if name and reason == "quit":
            break
        else:
            file_object.write(f"Name: {name} \nReason: {reason} \n")