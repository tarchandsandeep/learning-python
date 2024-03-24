from random import choice

def run_game():
    # word: str = choice(['apple', 'secret', 'banana'])
    word: str = choice([ 'banana'])

    username: str = input('What is your name? >> ')
    print(f'Welcom to hangman, {username}!')

    # Setup
    guessed: str = ''
    tries: int = 3
# we should 
    # 1. should limit to enter 1 character or
    # 2. allow the maximum characters in the word - leverage blanks variable
    while tries > 0:
        blanks: int = 0
        print('Word: ', end='')
        # word = 'banana'
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks+=1 # blanks = blanks + 1

        print() # Adds a blank line

        if blanks == 0:
            print('You got it!')
            break 
        guess: str = input('Enter a letter: ')
        if len(guess) != blanks or len(guess) != 1:
            print("illegal")
            tries -= 1
            is_tries_0_check = is_tries_0(tries)
            if is_tries_0_check:  
                break
            continue
        if guess in guessed:
            print(f'You already used: "{guess}". Please try another letter!')
            continue
        # guessed = guessed + guess
        guessed += guess 

        if guess not in word:
            # tries = tries - 1
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            is_tries_0_check = is_tries_0(tries)
            if is_tries_0_check:  
                break

def is_tries_0(tries):
    if tries == 0:
        return True
    return False

if __name__ == '__main__':
    run_game()