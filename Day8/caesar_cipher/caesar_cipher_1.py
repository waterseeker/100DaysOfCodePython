alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    list_of_characters = list(plain_text)
    counter = 0
    for character in list_of_characters:
        if character.isalpha():
            original_index = alphabet.index(character)
            new_index = original_index + shift_amount
            if new_index > 25:
                new_index = new_index % 25
            list_of_characters[counter] = alphabet[new_index]
        counter += 1
    print(f"The encrypted text is {''.join(list_of_characters)}")


encrypt(text, shift)
