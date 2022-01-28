
# Repeats a string a to a specific length t
def repeat_string(a_string, target_length):
    number_of_repeats = target_length // len(a_string) + 1
    a_string_repeated = a_string * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:target_length]
    return a_string_repeated_to_target

#PRE: Characters must be lowercase and be from the swedish alphabet
# Converts every characters in a string into their corresponding number and returns it as a list
def wordToNumber(word):
    numberList = []
    for element in word:
        if element == 'å':
            number = 26
        elif element == 'ä':
            number = 27
        elif element == 'ö':
            number = 28
        else:
            number = ord(element) - 97
        numberList.append(number)
    return numberList

# PRE: numbers must be from 0-28
# Converts numbers into their corresponding lowercase characters and returns them as a string
def numbToLetter(numbers):
    word = ""
    for element in numbers:
        if element == 26:
            letter = 'å'
        elif element == 27:
            letter = 'ä'
        elif element == 28:
            letter = 'ö'
        else:
            letter = chr(element+97)
        word = word + letter
    return word
