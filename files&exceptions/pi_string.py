# file_name = 'pi_digits.txt'
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()   # unlike rstrip() this strips the whitespace

# print(pi_string)
# print(len(pi_string))

file_name_1 = "D:\\computer_science\\ehmatthes-pcc_2e-078318e\\chapter_10\\pi_million_digits.txt"

with open(file_name_1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(f"{pi_string[:52]}")
# print(len(pi_string))

birth_day = input("Enter your birthday, in teh form mmddyy: ")
if birth_day in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")
