file_name = 'D:\\computer_science\\Python_Projects\\files&exceptions\\learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())