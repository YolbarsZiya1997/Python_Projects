# file_path = "D:\\computer_science\\Python_Projects\\files&exceptions\\pi_digits.txt"
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)

file_name = 'pi_digits.txt'
# this makes you read the file line by line
with open(file_name) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())




