import random
import sys
"""
scoring system:
How many times ai_won or user_won
"""
class RPS:
    def __init__(self):
        print('Welcome tp RPS 9000!')

        self.moves: dict = {'rock':'🪨', 'paper':'📃', 'scissors':'✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.ai_won : int = 0
        self.user_won: int = 0
    def play_game(self):
        user_move: str = input('Rock, paper, or scissor? >>').lower()

        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()
        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()
        
        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        self.scoreboard()

    def scoreboard(self):
        print('----')
        print(f'AI score:{self.ai_won}')
        print(f'User score:{self.user_won}')
        print('----')

    def display_moves(self, user_move: str, ai_move: str):
        print('----')
        print(f'You:{self.moves[user_move]}')
        print(f'You:{self.moves[ai_move]}')
        print('----')
    
    def check_move(self, user_move: str, ai_move: str): 
        if user_move == ai_move:
            print("It's a tie!")
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.user_won = self.user_won + 1
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.user_won = self.user_won + 1
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.user_won = self.user_won + 1
        else:
            print('AI wins..')
            self.ai_won = self.ai_won + 1

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
        

