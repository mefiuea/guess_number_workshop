import random


# Function to generate dice roll
def dice_generator(str_object):
    number_of_rolls = str_object[0:str_object.find('D')]
    if len(list(number_of_rolls)) == 0:
        number_of_rolls = '1'

    stop_plus = str_object.find('+')
    if stop_plus > 0:
        mark = '+'
        stop = str_object.find('+')
    elif stop_plus == -1:
        stop = 0
        mark = 'None'

    if stop_plus > 0:
        pass
    else:
        stop_minus = str_object.find('-')
        if stop_minus > 0:
            mark = '-'
            stop = str_object.find('-')
        elif stop_minus == -1:
            stop = 0
            mark = 'None'

    if stop > 0:
        dice_type = str_object[str_object.find('D')+1:stop]
    elif stop == 0:
        dice_type = str_object[str_object.find('D')+1:]

    if stop > 0:
        extra_number = str_object[stop+1:]
    else:
        extra_number = 'None'

    print(f'x(number of rolls) = {number_of_rolls}; y(dice type) = {dice_type}; mark = {mark}; extra number = {extra_number}')

    # Simulation
    i = 0
    sum = 0
    while i < int(number_of_rolls):
        roll = random.randint(1, int(dice_type))
        sum += roll
        print(f'Roll = {roll}')
        i += 1

    if mark == '+':
        print(f'Your score {sum} + {int(extra_number)} = {sum + int(extra_number)}')
        return sum + int(extra_number)
    elif mark == '-':
        print(f'Your score {sum} - {int(extra_number)} = {sum - int(extra_number)}')
        return sum - int(extra_number)
    else:
        print(f'Your score {sum}')
        return sum


if __name__ == '__main__':
    dice_generator('2D10+10')
    dice_generator('D6')
    dice_generator('2D3')
    dice_generator('D12-1')
