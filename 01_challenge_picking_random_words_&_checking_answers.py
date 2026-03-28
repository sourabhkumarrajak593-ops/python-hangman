# step 1
word_list = ["writing", "playing", "rewriting"]

"""TODO-1 - Randomly choose a word from the word_list and assign
and assign it to a variable called chosen_word"""
import random
chosen_word = random.choice(word_list)

"""TODO-2 - Ask the user to guess a letter and assign their answer
to variable called guess. Make guess lowercase."""
guess = input("Guess a letter: ").lower()

"""TODO-3 - Check if thr letter the user guessed(guess)
is one of the letters in chosen_word"""
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    
