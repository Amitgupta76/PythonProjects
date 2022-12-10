alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for i in text:
        j = alphabet.index(i) + shift
        new = alphabet[j]
        cipher_text += new
    print(f"The encoded text is {cipher_text}")

def decrypt(cipheri_text, shift):
    text = ""
    for i in cipheri_text:
        j = alphabet.index(i) - shift
        new = alphabet[j]
        text += new
    print(f"The decoded text is {text}")

if(direction == "encode"):
    encrypt(text, shift)
elif(direction == "decode"):
    decrypt(cipheri_text = text, shift = shift)
    

