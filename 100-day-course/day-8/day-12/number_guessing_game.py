import random

numbers = list(range(1, 101))

print("Welcome to the Number Guessing Game!!!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number_choosen = []

def random_number():
    random_number_choosen = random.choice(numbers)
    return random_number_choosen



number_of_guesses = 10




def difficulty_choosen():
    if difficulty == "easy":
        print("You have 10 attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess < random_number_choosen:
            print("Too Low")
            print("Guess again")
            return user_guess
        elif user_guess > random_number_choosen:
            print("Too High")
            print("Guess again")
            return user_guess
        else:
            print(f"You got it!! the number was {random_number_choosen}")
    elif difficulty == "hard":
        print("You have 5 attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess < random_number_choosen:
            print("Too Low")
            print("Guess again")
            return user_guess
        elif user_guess > random_number_choosen:
            print("Too High")
            print("Guess again")
            return user_guess
        else:
            print(f"You got it!! the number was {random_number_choosen}")
    else:
        return






