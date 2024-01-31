import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0: 
        raise ValueError
    if amount <= 6:
        print('values under or equal to 6')

rolls: list[int] = []
amount = 6
for i in range(amount):
    random_roll: int = random.randint(1,6)
    rolls.append(random_roll)

def print_home_address():
    print('18145 hidden creek trail , lakeville, mn, 55044')

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll?')
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            print(roll_dice(int(user_input)))
        except ValueError:
            print('(Please enter a valid number)')

if __name__ == '__main__':
    print_home_address() 
