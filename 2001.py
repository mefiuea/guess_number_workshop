from dice import dice_generator


def calculate_points(points):
    roll = dice_generator('2D6')
    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points


def game_2001():
    user_points = 0
    computer_points = 0

    input("Press ENTER to roll the dice")
    user_points += dice_generator('2D6')
    computer_points += dice_generator('2D6')

    while user_points < 2001 and computer_points < 2001:
        print()
        print(f"User points: {user_points}\nComputer points: {computer_points}")
        input("Press ENTER to roll the dice")
        user_points = calculate_points(user_points)
        computer_points = calculate_points(computer_points)

    print(f"User points: {user_points}\nComputer points: {computer_points}")
    if computer_points > user_points:
        print("Computer wins!")
    elif user_points > computer_points:
        print("User wins!")
    else:
        print("Draw")


if __name__ == '__main__':
    game_2001()
