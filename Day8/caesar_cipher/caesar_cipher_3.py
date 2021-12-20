alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(shift_direction, message_text, shift_amount):
    mutated_text = ""
    if shift_direction == "encode":
        for letter in message_text:
            position = alphabet.index(letter)
            if shift_direction == "encode":
                new_position = position + shift_amount
            elif shift_direction == "decode":
                new_position = position - shift_amount
            mutated_text += alphabet[new_position]
        if shift_direction == "encode":
            print(f"The encoded text is {mutated_text}")
        elif shift_direction == "decode":
            print(f"The decoded text is {mutated_text}")


caesar(direction, text, shift)
