file_name = 'reasons.txt'

reasons = []
while True:
    answers = input("Why do you like programming?: ")
    reasons.append(answers)

    continue_poll = input("Would do like to continue the poll?:(y/n) ")
    if continue_poll == 'n':
        break

with open(file_name, 'a') as file_object:
    for reason in reasons:
        file_object.write(f"{reason}\n")