alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maximum_character_index = len(alphabet)

def caesar(text, shift, direction):
    output = ''
    if direction == 'encode':
        for character in text:
                #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
            shifted_character_index = alphabet.index(character) + shift
            if shifted_character_index > maximum_character_index:
                shifted_character_index -= maximum_character_index
            output += alphabet[shifted_character_index]
        print(f"The encoded text is {output}")
    elif direction == 'decode':
        for character in text:
                #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
            decoded_character_index = alphabet.index(character) - shift
            if decoded_character_index < 0:
                decoded_character_index += maximum_character_index
            output += alphabet[decoded_character_index]
        print(f"The decoded text is {output}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("You must choose either encode or decode.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    break

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).