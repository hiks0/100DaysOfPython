import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pass_letters=int(input("Enter number of letters"))
pass_numbers=int(input("Enter number of numbers"))
pass_characters=int(input("Enter number of characters"))

#Easy

# password=""

# for char in range(0,pass_letters):
#     password +=rd.choice(letters)

# for char in range(0,pass_numbers):
#     password +=rd.choice(numbers)
    
# for char in range(0,pass_characters):
#     password +=rd.choice(symbols)
    
# print(f"Generated password is {password}")

#Hard

password_list=[]
password=""

for char in range(0,pass_letters):
    password_list.append(rd.choice(letters))

for char in range(0,pass_numbers):
    password_list.append(rd.choice(numbers))

    
for char in range(0,pass_characters):
    password_list.append(rd.choice(symbols))
  
rd.shuffle(password_list)
    
for i in range(0, len(password_list)):
    password += password_list[i]

print(f"Generated password is {password}")
