# Description : Basic Hang man game
# Author : Sebastiano GV
# Date Last Updated : 10th May, 2022
# Status : In Progress

import random
from collections import Counter

#wordpool contains words available, currently only two words for testing sake
wordPool='berry berry'.split(' ')
word=random.choice(wordPool)
attemptsCounter=0
guessedLetters=[]
guessedWord=['_','_','_','_','_'] # we will replace the _ with the letters guessed

while guessedLetters!=word:
    guess=input('Guess a letter ').lower()
    if guess in word: #if the letter is in the word
        guessedLetters.append(guess)
        counter=0
        index=word.index(guess)
        print(index)
        guessedWord[index]=guess
        print('Correct!')
    else:
        attemptsCounter+=1
        print('Incorrect!')
    print(guessedWord)
    