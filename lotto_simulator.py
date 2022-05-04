import random


# Function to get 6 numbers from user and insert it to list
def get_numbers_from_user():
    entered_number = input('Please type your number from range 1 to 49: ')
    while not entered_number.isnumeric() or not entered_number.isdecimal():
        print()
        print('This is not a number.')
        entered_number = input('Please type your number from range 1 to 49: ')
    else:
        entered_number = int(entered_number)
        while entered_number < 1 or entered_number > 49:
            print()
            print('Number out of range! Try again')
            entered_number = int(input('Please type your number from range 1 to 49: '))
        else:
            print(f'Your number is {entered_number}')
            return entered_number


# Function to generate and check if number repeat in list
def generating_list_of_numbers():
    user_number_list = []
    while len(user_number_list) < 6:
        number_from_user = get_numbers_from_user()
        while number_from_user in user_number_list:
            print('Number repeats. Try another one.')
            number_from_user = get_numbers_from_user()
        else:
            print('Number does not repeat, added to list.')
            user_number_list.append(number_from_user)
    else:
        return user_number_list


# Function to sort list of numbers
def sort_function(list_of_numbers):
    return sorted(list_of_numbers)


# Function to generate 6 random numbers without repeat
def number_generator():
    random_number_list = []
    while len(random_number_list) < 6:
        random_number = random.randint(1, 49)
        while random_number in random_number_list:
            random_number = random.randint(1, 49)
        else:
            random_number_list.append(random_number)
    else:
        return random_number_list


# Function to check match numbers from user list and generator list
def checking_matches():
    user_number_list = generating_list_of_numbers()
    print(f'User list: {sort_function(user_number_list)}')
    print()
    generator_number_list = number_generator()
    print(f'Random list: {sort_function(generator_number_list)}')
    counter = 0

    for number in user_number_list:
        if number in generator_number_list:
            counter += 1

    print()
    if counter == 0:
        return print(f'Unfortunately you didnt guess anything.')
    else:
        return print(f'Congratulations, you guessed {counter} numbers!')


if __name__ == '__main__':
    checking_matches()
