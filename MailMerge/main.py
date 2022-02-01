# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
cleaned_names = [name.strip() for name in names]

for name in cleaned_names:
    with open("Input/Letters/starting_letter.txt") as file:
        letter = file.read()
        replaced_name = letter.replace("[name]", name)
        file_name = f"Output/ReadyToSend/letter_for_{name}.txt"
        with open(file_name, mode="w") as new_file:
            new_file.write(replaced_name)
