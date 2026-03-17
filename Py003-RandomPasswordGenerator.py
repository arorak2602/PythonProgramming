# PythonRandomPasswordGenerator

import random

print("Welcome to random password generator")

# Character sets
lowerChar = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

upperChar = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numList = ['0','1','2','3','4','5','6','7','8','9']

specialChar = [
    '!','@','#','$','%','^','&','(',')',
    '_','+','-','=','/','*','`','~'
]

# User input
low = int(input("How many lowercase characters would you like?\n"))
upp = int(input("How many uppercase characters would you like?\n"))
num = int(input("How many numbers would you like?\n"))
sym = int(input("How many symbols would you like?\n"))

# Prevent empty password
if low + upp + num + sym == 0:
    print("Password cannot be empty!")
else:
    # Generate random characters
    lowChar = random.choices(lowerChar, k=low)
    uppChar = random.choices(upperChar, k=upp)
    numChar = random.choices(numList, k=num)
    symChar = random.choices(specialChar, k=sym)

    # Combine and shuffle
    password = lowChar + uppChar + numChar + symChar
    random.shuffle(password)

    print("Your new password is:")
    print("".join(password))


