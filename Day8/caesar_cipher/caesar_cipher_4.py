from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)
run_program_again = True

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) % 26

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
while run_program_again:
    run_again = input("Would you like to restart the cipher program?\n")
    if run_again == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to \
decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    elif run_again == "no":
        run_program_again = False
    else:
        print(f"Sorry, I don't understand {run_again}. \
You have to enter either yes or no.")
        continue
