from random import choice
luck = (1, 2, 7, 4, 11, 13, 19, 98, 12, 17, "a", "z", "s", "n", "ş")
digit_number = 4
winning_ticket = []

while len(winning_ticket) < digit_number:
    pulled_item = choice(luck)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)


print(winning_ticket)