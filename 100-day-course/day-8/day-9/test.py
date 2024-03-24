import os

auction = {}

def bid_game():
    name = input("What is your name? /n").lower()

    bid_amount = int(input("What is your Bid amount"))

    auction[name] = bid_amount

    check_other_bidders = input("Are there any other bidders?").lower()

    
    if check_other_bidders == "yes":
        bid_game()
    if check_other_bidders == "no":
        auction_get = auction.get
        print("auction_get", auction_get)
        highest_bidder = max(auction, key=auction.get)
        print(f" The winner is: {highest_bidder}")


bid_game()

print("auction", auction)


