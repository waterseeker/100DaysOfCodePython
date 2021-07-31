alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maximum_character_index = len(alphabet)

def encrypt(plain_text, shift_amount):
    encrypted_message = ''
    for character in plain_text:
        shifted_character_index = alphabet.index(character) + shift_amount
        if shifted_character_index > maximum_character_index:
            shifted_character_index -= maximum_character_index
        encrypted_message += alphabet[shifted_character_index]
    print(f"The encoded text is {encrypted_message}")

def decrypt(encoded_text, shift_amount):
    decoded_message = ''
    for character in encoded_text:
        decoded_character_index = alphabet.index(character) - shift_amount
        if decoded_character_index < 0:
            decoded_character_index += maximum_character_index
        decoded_message += alphabet[decoded_character_index]
    print(f"The decoded text is {decoded_message}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking 
# the 'direction' variable. Then call the correct function based on that 
# 'drection' variable. You should be able to test the code to encrypt *AND* 
# decrypt a message.
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("You must choose either encode or decode.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
        break
    if direction == 'decode':
        decrypt(text, shift)
        break
