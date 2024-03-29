import random as rd
words=["ant", "camel", "elephant","whale","eagle"]
print( ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word=rd.choice(words)



display=[]
for i in range(len(chosen_word)):
    display+="_"
print(f"{' '.join(display)}\n")


tries=6
status=False
while(status==False and tries>=0):
    letter=input("Guess a letter: ").lower()

    if letter in display:
      print("you have already guessed this letter")
      
    for i in range(len(chosen_word)):
        if letter==chosen_word[i]:
           display[i]=letter
          

    print(f"{' '.join(display)}\n")

    
  
    if letter not in display:
      print(stages[tries])
      print("WRONG CHOICE\n")
      tries-=1

    if "_" not in display:
      status=True 
      print("YOU WIN")

if tries<0:
  print("YOU LOSE")
      
  
