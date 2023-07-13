# from collections import random
import random

#creating a list of words: 
words=['ardvark','baboon','camel']

chossen_word=random.choice(words)
print(chossen_word)

guess=input("Guess the letter ")
guess.lower()

if guess in chossen_word:
    print(True)
else: 
    print(False)