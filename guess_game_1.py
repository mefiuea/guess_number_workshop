import random


# Function to get value from keyboard and check this values
def enter_value():
    entered_number = input('Please type your number from range 1 to 100: ')
    while not entered_number.isnumeric():
        print('This is not a number.')
        print()
        entered_number = input('Please type your number from range 1 to 100: ')
    else:
        entered_number = int(entered_number)
        while entered_number < 1 or entered_number > 100:
            print('Number out of range! Try again')
            print()
            entered_number = int(input('Please type your number from range 1 to 100: '))
        else:
            print(f'Your number is {entered_number}')
            return entered_number


# Function to drawing number from range 1 to 100
def number_generator():
    return random.randint(1, 100)


# Function to compare number from user and generator
def number_comparator():
    user_number = enter_value()
    generator_number = number_generator()
    while True:
        if user_number < generator_number:
            print('Your number is too low')
        elif user_number > generator_number:
            print('Your number is too high')
        else:
            print('You guessed the number!')
            return True

        print()
        user_number = enter_value()


if __name__ == '__main__':
    print(__name__)
    number_comparator()
