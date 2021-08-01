alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maximum_character_index = len(alphabet)

def caesar(text, shift, direction):
    output = ''
    if direction == 'encode':
        for character in text:
            shifted_character_index = alphabet.index(character) + shift
            if shifted_character_index > maximum_character_index:
                shifted_character_index -= maximum_character_index
            output += alphabet[shifted_character_index]
        print(f"The encoded text is {output}")
    elif direction == 'decode':
        for character in text:
            decoded_character_index = alphabet.index(character) - shift
            if decoded_character_index < 0:
                decoded_character_index += maximum_character_index
            output += alphabet[decoded_character_index]
        print(f"The decoded text is {output}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("You must choose either encode or decode.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    break