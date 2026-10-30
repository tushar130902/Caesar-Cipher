alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""

    if encode_or_decode == "decode":
            shift_amount *= -1

    for letter in original_text:
        

        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount 
            shifted_position %= len(alphabet) 
            cipher_text += alphabet[shifted_position]

        else:
            cipher_text += letter

    print(f"here is {encode_or_decode} result: {cipher_text}")

should_continue = True

while True:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("type your message: \n").lower()
    shift = int(input("type the shift number: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    tx = input("Type 'yes' if you want to go again, otherwise, type 'no': \n ").lower()
    if tx == "no":
        should_continue = False
        print("Goodbye")

