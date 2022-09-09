from random import choice


def get_winning_tickets(possibilities: list, digit_length: int) -> list:
    """Return a winning ticket from a set of possibilities
    """
    winning_ticket = []

    # we don't want the content in the winning ticket to repeat
    # we shall use while loop
    while len(winning_ticket) < digit_length:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket: list, winning_ticket: list) -> bool:
    """Check all the element in the played ticket, if any are not in the
    winning ticket return false"""
    for element in played_ticket:
        if element not in winning_ticket:
            return False


def make_random_ticket(possibilities: list, digit_length: int) -> list:
    """Return a random ticket"""
    ticket = []
    while len(ticket) < digit_length:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


digit_length = 4
possibilities = [5, 8, 20, 1, 22, 6, 4, 9, 25, 2, "z", "a", "n", "s", "ş"]
winning_ticket = get_winning_tickets(possibilities, digit_length)

plays = 0
won = False

# let's take a max number of tries, in case this might take forever
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities, digit_length)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break


if won:
    print("We have a winning ticket!")
    print(f"Your ticket was {new_ticket}")
    print(f"The winning ticket was {winning_ticket}")
    print(f"It only took {plays} plays to get it")

else:
    print(f"Tries {plays} times, without a winning ticket")
    print(f"Your ticket: {new_ticket}")
    print(f"The winning ticket: {winning_ticket}")