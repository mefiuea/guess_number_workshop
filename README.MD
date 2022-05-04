#Workshop: Number games.
Simple console applications to practice the Python language. Additionally, used Flask library.

Workshop includes 6 games:
1. Number guessing game 1,
2. Lotto simulator,
3. Number guessing game 2,
4. Number guessing game 3,
5. Dice,
6. '2001'.


### Number guessing game 1

- This program randomizes numbers from a range 1 to 100
- User is typing his guess (number) on the keyboard
- Program is checking number from computer random pick and compare it with number of the user

### lotto simulator

- This program ask user to enter 6 unique numbers from value 1 to 49 and make list from it
- Generate 6 random unique values and put it to the list
- Compare element (number) from user list with numbers in random list. If any number from user list match to number in 
random list increase counter 1 time


### Number guessing game 2

- This application get one fixed number from user
- In next steps computer is trying to guess user number
- User needs to answer to computer 'too small, too big, you win' based on computer guess


### Number guessing game 3

- This is the same application as 'Number guessing game 2', but Flask library is used


### Dice

- RPG dice roll simulation
- function takes the specified character code as input: xDy+z
  (x - number of dice rolls; if we roll once, this parameter is negligible, y - the type of dice to use (e.g. D6, D10), 
  z -  the number to add (or subtract) to the result of the throws (optional))


## 2001

- A game of which player (user/computer) achieves a score greater than 2001
- In his turn, a player rolls 2 dice (standard hex dice) (The simulation of throwing these dice is imported from an earlier 
  game - 'Dice')
- The number of dots thrown is added to the total score
- Starting on the second turn:
  - if the player rolls a 7, he divides his number of points by this value discarding the fractional part,
  - if he throws 11, multiplies his current number of points by that value.
