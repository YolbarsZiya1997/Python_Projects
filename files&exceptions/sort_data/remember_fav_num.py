import json


def get_fav_num():
    """Get the fav number"""
    filename = 'fav_num.json'
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def new_fav_num():
    """Register a new fav number"""
    filename = 'fav_num.json'
    new_number = input("Your new favorite number: ")
    with open(filename, 'a') as f:
        json.dump(new_number, f)
    return new_number


def fav_num_guesser():
    """Guesses your favorite number"""
    fav_num = get_fav_num()
    if fav_num:
        print(f"Your favorite number is {fav_num}")
    else:
        fav_num = new_fav_num()
        print("We will remember your new favorite number")


fav_num_guesser()