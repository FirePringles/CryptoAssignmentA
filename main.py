from HelpFunctions import*
from cipher import*

#Here we set the size of the plaintext that we want to encrypt
size_of_file = 509

# Opens and reads from a file called text.txt.
with open('text.txt', 'r', encoding='utf8') as file:

    # Key that will be used to encrypt
    key = "warhammer"

    keychain = str(repeat_string(key, size_of_file))

    # Turns the repeated key string into a list of the corresponding numbers
    numberKeychain = wordToNumber(keychain)

    numberList = []

    # Here we convert every character in the plaintext into lowercase. We also remove any special characters and then turn every letter into the corresponding number.
    for line in file:
        for word in line.split():
            word = word.lower()
            word = ''.join(char for char in word if char.isalnum())
            numberList.append(wordToNumber(word))

    document = ""   
    i = 0

    # We go through the list of numbers and encrypt them using the vigenereCipher function. We then convert these numbers into letters again and put the result into a new string.
    for list in numberList:
        newTuple = vigenereCipher(list,numberKeychain,i)
        encodedList = newTuple[0]
        i = newTuple[1]
        document = document + (numbToLetter(encodedList)) + " "

    # The result string is then written into a file called result.txt
    f = open("result.txt", "w")
    f.write(document)