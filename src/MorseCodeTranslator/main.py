#Morse to text, as well as text to morse translations
morseDict={
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',}

message='.... . .-.. .-.. --- .-- --- .-. .-.. -..'
def textToMorse(message):
    morseMessage=''
    for letter in message:
        if letter.upper() in morseDict:
            morseMessage+=morseDict[letter.upper()]+' '
    return morseMessage

def morseToText(message):
    textMessage=''
    for letter in message.split(' '):
        for key,value in morseDict.items():
            if value==letter:
                textMessage+=key
    return textMessage

print(morseToText(message))