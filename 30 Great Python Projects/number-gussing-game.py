from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}')

while True:
    try:
        user_guess: int = int(input('Gues:'))
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

    

    