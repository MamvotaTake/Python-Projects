PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    start_letter = letter.read()

# for each name in invited_names.txt
for name in invited_names:
    stripped_name = name.strip()
    new_letter = start_letter.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
