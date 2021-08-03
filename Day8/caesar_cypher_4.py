from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maximum_character_index = len(alphabet)

def caesar(text, shift, direction):
    output = ''
    if direction == 'encode':
        for character in text:
            if character.isalpha():
                shifted_character_index = alphabet.index(character) + (shift % len(alphabet))
                if shifted_character_index > maximum_character_index:
                    shifted_character_index -= maximum_character_index
                output += alphabet[shifted_character_index]
            else:
                output += character
        print(f"The encoded text is {output}")
    elif direction == 'decode':
        for character in text:
            if character.isalpha():
                decoded_character_index = alphabet.index(character) - (shift % len(alphabet))
                if decoded_character_index < 0:
                    decoded_character_index += maximum_character_index
                output += alphabet[decoded_character_index]
            else:
                output += character
        print(f"The decoded text is {output}")

print(logo)
user_continues = True
while user_continues == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("You must choose either encode or decode.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    choice = input("Would you like to go again? Y or N?").lower()
    if choice != 'y' and choice != 'n':
        print("You must choose Y or N.")
    elif choice == 'n':
        print("Thank you for using the Caesar Cypher!")
        user_continues = False
    if user_continues == True:
        continue
    break