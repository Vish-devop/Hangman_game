
import random

#Taking out the words from hangman.py 
from hangman_words import words
#importing hangman_art 
from hangman_art import logo
print(logo)
from hangman_art import stages



chossen_word=random.choice(words)
# print(chossen_word)


display=[]
for i in range(0,len(chossen_word)):
    display.append("_")

end_of_game=False
lives=6
lost="You lost, better luck next-time."
win="You won!!"

while not end_of_game:

    #ckecking guessed letter
    guess=input("Guess the letter ").lower()
    for position in range(0,len(chossen_word)):
        letter=chossen_word[position]
        if letter==guess:
            display[position]=letter
    
    print(f"{' '.join(display)}")
    # check if guessed word is present in chossen_word    
    if guess not in chossen_word:
        print(f"\nYou guessed {guess}, that's not present in the word. You lost a life.")
        lives-=1
    if lives==0:
        end_of_game=True
        print(lost)
        
    #checking if all the letters entered by the user are present in the choosen_word.
    if "_" not in display:
        end_of_game=True
        print(win)
  
    
    print(stages[lives])



