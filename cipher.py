def shiftCip(list, key):
    newList = []
    for number in list:
        newList.append((number+key) % 26)
    return newList

def decodeShift(list,key):
    newList = []
    for number in list:
        newList.append((number-key) % 26)
    return newList 


# List is the converted plaintext and keychain is the converted keychain. i is a number that is used to keep track of the specific character in the keychain that we want to use for encrypting.
def vigenereCipher(list,keychain,i):
    newList = []
    for number in list:
        newList.append((number+keychain[i]) % 29)
        i = i+1
    return(newList, i)