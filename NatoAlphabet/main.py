import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)


def encode_word():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
    finally:
        encode_word()


encode_word()
