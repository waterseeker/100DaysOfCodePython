import pandas

# TODO 1. Create a dictionary in this format: basically convert the csv into a dict
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# the user gets a prompt asking them "Enter a word:"
while True:
    user_input = input("Enter a word:\n").upper()
    # they get a list of the code words printed out for the word they entered
    # ex. Enter a word: Thomas
    # ["Tango", "Hotel", "Oscar", "Mike", "Alfa", "Sierra"]
    nato_code_list = [phonetic_dictionary[letter] for letter in user_input]
    print(nato_code_list)
