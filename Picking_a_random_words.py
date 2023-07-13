# from collections import random
import random

#Taking out the words from hangman.py 
from hangman_words import words


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chossen_word=random.choice(words)
print(chossen_word)


display=[]
for i in range(0,len(chossen_word)):
    display.append("_")

end_of_game=False
lives=6
while not end_of_game:

    #ckecking guessed letter
    guess=input("Guess the letter ").lower()
    for position in range(0,len(chossen_word)):
        letter=chossen_word[position]
        if letter==guess:
            display[position]=letter
    
    print(display)

    if guess not in chossen_word:
        lives-=1
    if lives==0:
        end_of_game=True
        print("You lost")
    
    print(f"{' '.join(display)}")
    
    #checking if all the letters entered by the user are present in the choosen_word.
    if "_" not in display:
        end_of_game=True
        print("You won")
    
    print(stages[lives])



