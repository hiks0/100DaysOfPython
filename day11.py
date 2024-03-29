import random as rd
from replit import clear
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards=[]
computer_cards=[]
game_over=False

def dealcard():
    card=rd.choice(cards)
    return card

def sum_cards(cards):
    if sum_cards==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
        
def compare_score(user_score, computer_score):
    if user_score==computer_score:
        return "Draw"
    elif user_score==0:
        return "win with a blackjack"
    elif computer_score==0:
        return "lose, opponent has blackjack"
    elif user_score>21:
        return "bust! You lose!"
    elif computer_score>21:
        return "You win! The computer busted."
    elif user_score>computer_score:
        return "You win!"
    else: #if computer_score > user_score
        return "Computer wins!"
    
        
        
    

for i in range(2):
        user_cards.append(dealcard())
        computer_cards.append(dealcard())

while game_over==False:
    user_score=sum_cards(user_cards)
    computer_score=sum_cards(computer_cards)
    print(f"Your cards are {user_cards}, current score: {user_score}")
    print(f"computers first card is {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
        game_over=True
    else:
        user_should_deal=input("Type yes to get another card, type n to pass: ")
        if user_should_deal=="y":
            user_cards.append(dealcard())
        else:
            game_over=True

while computer_score != 0 and computer_score<17:
    computer_cards.append(dealcard())
    computer_score=sum_cards(computer_cards )
print(f"your final hand is {user_cards}, and final score is {user_score}")
print(f"computer final hand is {computer_cards}, computer final scors is {computer_score}")
print(compare_score(user_score, computer_score))
