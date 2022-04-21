import random
from collections import Counter

wordPool='mango apple pear banana orange'.split(' ')
word=random.choice(wordPool)

attemptsCounter=0
guessedLetters=[]

while guessedLetters!=word:
    guess=input('Guess a letter ').lower()
    if guess in word:
        guessedLetters.append(guess)
        print('Correct!')
    else:
        attemptsCounter+=1
        print('Incorrect!')
    print(Counter(guessedLetters))
    