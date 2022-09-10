file_name = 'guest_book.txt'

with open(file_name, "a") as file_object:
    while True:
        guest_name = input("Please input your name: ")
        if guest_name == "quit":
            break
        else:
            file_object.write(f"{guest_name}\n")
