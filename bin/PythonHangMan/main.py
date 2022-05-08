import random
from collections import Counter

wordPool='berry berry'.split(' ')
word=random.choice(wordPool)
attemptsCounter=0
guessedLetters=[]
guessedWord=['_','_','_','_','_']
#cuogk
while guessedLetters!=word:
    guess=input('Guess a letter ').lower()
    if guess in word:
        guessedLetters.append(guess)
        counter=0
        if guess in word:
            index=word.index(guess)
            print(index)
            guessedWord[index]=guess
        print('Correct!')
    else:
        attemptsCounter+=1
        print('Incorrect!')
    print(guessedWord)
    