PLACEHOLDER = "[name]"
with open("/Users/pranaymathur/Desktop/100daysPython/day24/Input/Names/invited_names.txt") as name:
    names = name.readlines()

with open("/Users/pranaymathur/Desktop/100daysPython/day24/Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final:
            final.write(new_letter)

