alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = "yes"
from art import logo
print(logo)
while again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction == "encode": 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def encrypt(text, shift):
      cipher_text = ""
      for i in range(0,len(text)):
        if text[i] not in alphabet:
          cipher_text += text[i]
        else:
          position = alphabet.index(text[i])
          if position + shift > 25:
            position = (position+shift) % 26 -shift
          cipher_text += alphabet[position+shift]
      print(f"The encoded message is : {cipher_text}")
    encrypt(text, shift)
  else:
    cipher_text = input("Type your encrypted message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def decrypt(cipher_text, shift):
      text = ""
      for i in range (0,len(cipher_text)):
        if cipher_text[i] not in alphabet:
          text += cipher_text[i]
        else:
          position = alphabet.index(cipher_text[i])
          if position - shift <0:
            position = (position-shift) %26 +shift
          text +=alphabet[position-shift]
      print(f"The decoded message is : {text}")
    decrypt(cipher_text, shift)
  again = input("Do you want to go again? yes or no\n").lower()