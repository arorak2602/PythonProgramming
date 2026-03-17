# PythonWordListGenerator

import random

print("Welcome to word list generator")

firstName = input("Enter the first name of the person : \n")
lastName = input("Enter the last name of the person : \n")
birthDate = input("Enter the birth date : \n")
birthMonth = input("Enter the birth month : \n")
birthYear = input("Enter the birth year : \n")
fName = input("Enter the father's first name : \n")
mName = input("Enter the mother's first name : \n")
sName = input("Enter the sibling name (if any): \n")
pName = input("Enter the pet name (if any) : \n")

numList = ['0','1','2','3','4','5','6','7','8','9']
specialChar = ['!','@','#','$','%','^','&','(',')']

# store inputs
words = [
    firstName, lastName,
    birthDate, birthMonth, birthYear,
    fName, mName, sName, pName
]

# remove empty inputs
words = [w for w in words if w != ""]

useNumbers = input("Include numbers? (y/n): ").lower() == "y"
useSymbols = input("Include symbols? (y/n): ").lower() == "y"

numCount = int(input("How many numbers to add?: ")) if useNumbers else 0
symCount = int(input("How many symbols to add?: ")) if useSymbols else 0

wordList = []

# make 2-word pairs
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            wordList.append([words[i], words[j]])

finalList = []

for pair in wordList:
    w1 = pair[0]
    w2 = pair[1]

    # case variations
    variations = [
        w1.capitalize() + w2.capitalize(),
        w1.lower() + w2.capitalize(),
        w1.capitalize() + w2.lower(),
        w1.lower() + w2.lower()
    ]

    for v in variations:
        temp = [v]

        # add numbers
        for _ in range(numCount):
            temp.append(random.choice(numList))

        # add symbols
        for _ in range(symCount):
            temp.append(random.choice(specialChar))

        random.shuffle(temp)
        finalList.append("".join(temp))

# remove duplicates
finalList = list(set(finalList))

random.shuffle(finalList)

# print results
for i in range(min(20, len(finalList))):
    print(finalList[i])