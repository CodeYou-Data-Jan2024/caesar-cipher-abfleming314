user_input = input("Please enter a sentance: ")
user_input = user_input.lower()
converted_input = " "
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipher_alphabet = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]
for letter in user_input:
    if letter in alphabet:
        converted_input += cipher_alphabet[alphabet.index(letter)]
    else:
        converted_input += letter
print("Your cipher message is: ", converted_input)