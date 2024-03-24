import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0: 
        raise ValueError
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1,6)
        rolls.append(random_roll)

    return rolls


def sum(rolls: list[int]) -> int:
    total: int = 0

    for roll in rolls:
        total = roll + total
    
    return total

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll?')
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            roll_dice_output: list[int] = roll_dice(int(user_input))
            total_dice_output: int = sum(roll_dice_output)
            print(total_dice_output)
            break
        except ValueError:
            print('(Please enter a valid number)')

if __name__ == '__main__':
    main() 
