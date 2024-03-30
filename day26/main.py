import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in df.iterrows()}

word = input("Enter the word: ").upper()
letter_list = [letter for letter in word]
new_list = [new_dict[letter] for letter in letter_list]
print(new_list)
