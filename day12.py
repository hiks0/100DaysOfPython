import random as rd
print('''
                              _   _                                  _               
                             | | | |                                | |              
   __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
  / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
   __/ |                                                                             
  |___/                                                                              
''')
num_list=[]

for i in range (1, 100):
    num_list.append(i)
chosen_num=rd.choice(num_list)
rounds=1
print("Im thing of a number between 0 and 100")
end_game=False

def set_difficulty():
    level=input("enter difficulty level. 'easy', 'medium', 'hard': ")
    if  level == "easy":
        chances=10
    elif level=="medium":
        chances=7
    elif level=="hard":
        chances=5
    print(f"you have {chances} chances")
    return chances

chance=set_difficulty()
guesses=[]

while(rounds<=chance):
    guess = int(input("Enter your guess:"))
    guesses.append(guess)
    
    if  guess < chosen_num :
        print("Your guess is too low.")
        
    elif guess > chosen_num:
        print("Your guess is too high.")
        
    elif  guess==chosen_num:
        #print("You guessed it right!")
        break
    rounds+=1
        
if chosen_num in guesses:
    print(f"Congratulations you won! The number is {chosen_num}")
else:
    print(f"You ran out of guesses! The number was {chosen_num}")


