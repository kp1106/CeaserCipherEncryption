import random
import pyperclip as pc

def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def ValidString(string):
    return len(string) > 30

userInput = input('Enter a string to encrypt, NO LONGER THAN 30 CHAR:  ')

if ValidString(userInput):
    print("Thanks")

userShift = input('Y/N Do you want to choose a number to shift or allow the system to randomise:  ')
if(userShift == 'Y'):
    shiftNum = int(input("Enter an INTEGER to CeaserCipher Shift by:  "))
else:
    shiftNum = random.randint(1,10)
    print("Your random shift is...")
    print(shiftNum)

originalMessage = userInput
encryptedMessage = encrypt(originalMessage, shiftNum)
print("Your encrypted message is:  " + encryptedMessage)

userClip = input('Y/N Do you want to copy the encrypted message to clipboard')
if(userClip == 'Y'):
    pc.copy(encryptedMessage)