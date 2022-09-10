def file_reader(filename):
    """ A basic file reader"""

    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist")
        # if you wanna silent pass this just type "pass"
    else:
        for name in contents:
            print(name.rstrip())


file_names = ['cats.txt', 'dogs.txt']
for filename in file_names:
    print(f"Reading file '{filename}': ")
    file_reader(filename)