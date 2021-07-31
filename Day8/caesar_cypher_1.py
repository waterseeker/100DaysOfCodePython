alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_message = ''
    maximum_character_index = len(alphabet)
    for character in text:
        shifted_character_index = alphabet.index(character) + shift
        if shifted_character_index > maximum_character_index:
            shifted_character_index = shifted_character_index - maximum_character_index
        encrypted_message += alphabet[shifted_character_index]
    print(f"The encoded text is {encrypted_message}")

encrypt(text, shift)