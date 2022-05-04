# Function to get value from keyboard and check this values
def enter_value():
    entered_number = input('Please type your number from range 1 to 1000: ')
    while not entered_number.isnumeric():
        print('This is not a number.')
        print()
        entered_number = input('Please type your number from range 1 to 1000: ')
    else:
        entered_number = int(entered_number)
        while entered_number < 1 or entered_number > 1000:
            print('Number out of range! Try again')
            print()
            entered_number = int(input('Please type your number from range 1 to 1000: '))
        else:
            print(f'Your number is {entered_number}')
            return entered_number


# Function to check computer number with user number
def guessing_number():
    user_fixed_number = enter_value()
    print(f'User fixed number: {user_fixed_number}')

    min_range = 1
    max_range = 1001
    counter = 0

    print()
    while counter < 11:
        guess = int((max_range-min_range) // 2) + min_range
        print(f'Computer guess: {guess}')

        user_answer = input('Type answer [too small, too big, you win]: ')

        counter += 1
        print(f'Counter status {counter}')

        if user_answer == 'you win':
            print('I win! (computer)')
            break
        elif user_answer == 'too small':
            min_range = guess
        elif user_answer == 'too big':
            max_range = guess

        if user_fixed_number == guess and user_answer != 'you win':
            print('Please dont cheat.')
            print('I have one more try for your cheating.')
            counter -= 1

        if counter == 0:
            print()
            print('Too much cheating - exit')
            break


if __name__ == '__main__':
    guessing_number()
