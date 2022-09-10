file_name = 'learning_python.txt'

with open(file_name) as file_object:
    content = file_object.read()

print(content.rstrip())
print("*" * 80)
print("Looping over the content")

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print("*" * 80)
print("By making a list and looping over it")

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())