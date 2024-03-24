# `random` is a package. From which we import `randomint`
from random import randint
# assign the data to variables
lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}')
"""
problem statement:
1. Try to limit the amount of guesses a user can use.

2. User can guess maximum of 3 times
a. create a new variable whic will store the number of guesses - variable name is guess_limit
3. or else game over
  a. if(guess_limit > 3):
       print("game over")
"""
guess_limit = 1

prev_guess_variable = None
# infinite loop
while True:
    # try except is used for error handling purpose
    try:
        user_guess: int = int(input('Gues:'))
        guess_limit = guess_limit + 1
        if(user_guess == prev_guess_variable):
            print("U have already selected this value, please select another value")
        prev_guess_variable = user_guess
    except ValueError as e:
        print('Please enter a valied number.')
        continue
    
    if user_guess > random_number:
        print('The Number is lower')
    elif user_guess < random_number:
        print('The Number is higher')
    else:
        print('You got it!')
        break

    if guess_limit > 3:
        print("Game over")
        break

    

    