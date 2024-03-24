import random

user_cards = []
computer_cards = []



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  card = random.choice(cards)
  return card

"""
1. store user cards in user_cards
2. store computer_cards in computer_cards
3. user and computer should each get 2 random cards
4. check blackjack
"""
def assign_user_cards():
   new_card = deal_card()
   user_cards.append(new_card)

def assign_computer_cards():
   new_card = deal_card()
   computer_cards.append(new_card)

def add_user_cards():
   total = sum(user_cards)
   return total

def add_computer_cards():
    total = sum(computer_cards)
    return total

def check_blackjack(total_card_value: int):
   is_blackjack = total_card_value == 21
   return is_blackjack

def replace_user_cards(eleven_or_one: int):
   for card_index in range(len(user_cards)):
       if user_cards[card_index] == 11:
           user_cards[card_index] = eleven_or_one
   return

   
def play_blackjack(is_computer_triggered: bool = False):
    sum_user_cards = add_user_cards()
    sum_computer_cards = add_computer_cards()
    does_user_have_blackjack = check_blackjack(sum_user_cards)
    does_computer_have_blackjack = check_blackjack(sum_computer_cards)

    if does_user_have_blackjack:
        print("User Won")
        return

    if does_computer_have_blackjack:
     print(" User Lose")
     return

    if sum_user_cards > 21:
        if 11 in user_cards:
            print(f'user_cards: {user_cards}')
            ace_check_number = int(input("do you want to keep the ace as 11 or 1 ? "))
            replace_user_cards(ace_check_number)
            play_blackjack()
        else:
            print("User lose") # 8, 7, 1, 6
            return
    else:
        # user cards less than 21
        if is_computer_triggered != True:
            print(f'user_cards: {user_cards}')
            draw_another_card = input("Do you want additional card?").lower()
            if draw_another_card == "yes":
                assign_user_cards()
                play_blackjack()
            else:
                # when user enters "no"
                if sum_computer_cards < 17:
                    assign_computer_cards()
                    play_blackjack(True)
                elif sum_computer_cards > 21:
                    print("User won")
                    return
                elif sum_user_cards > sum_computer_cards:
                    print("User Won")
                    return
                elif sum_user_cards < sum_computer_cards:
                    print("User loose")
                    return
                elif sum_computer_cards > 21:
                    print("User Won")
                    return
                else:
                    print("Draw")
                    return






while True:
    check_play_again = input("do u want to play blackjack? ").lower()
    user_cards.clear()
    computer_cards.clear()
    if check_play_again == "yes":
        assign_user_cards()
        assign_computer_cards()
        assign_user_cards()
        assign_computer_cards()
        play_blackjack()
        print(f'user_cards: {user_cards}')
        print(f'computer_cards: {computer_cards}')
    else:
        break




      
  