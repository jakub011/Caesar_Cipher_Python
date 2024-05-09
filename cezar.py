import art
from art import logo

def cezar(direction,text,shift):
    encrypt_text = "" 
    for i in text:
        if i.isalpha():
            if direction == 'encode':
                encrypt_text += chr((ord(i)-97+shift)%26+97)
            elif direction == 'decode':
                encrypt_text += chr((ord(i)-97-shift)%26+97)
        else:
            encrypt_text += i
    print(encrypt_text)

stop = False

print(logo)
while(stop == False):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cezar(direction,text,shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no' ")
    if again == "no":
        stop = True
        print("Goodbye")

