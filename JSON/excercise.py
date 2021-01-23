import json


def get_stored_number():
    """get number if eixts, or it will return None"""
    try:
        filename = 'number.json'
        with open(filename) as f_obj:
            stored_number = json.load('f_obj')
        return stored_number
    except FileNotFoundError:
        return None


def get_new_number():
    """if number does not exists, prompt for a new number"""
    new_number = input('What\'s your favorite number? ')
    filename = 'number.json'
    with open(filename, 'w') as f_obj:
        json.dump(new_number, f_obj)
    return new_number


def printNum():
    """print if the number exists"""
    newNumber = get_new_number()
    if newNumber:
        print('Welcome back, your number was ' + newNumber)
    else:
        newNumber = get_new_number()
        print('Well, when you return I will remember your number was' + newNumber)


if __name__ == '__main__':
    printNum()
