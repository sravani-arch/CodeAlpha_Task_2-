import random

words = ["apple", "mango", "grapes", "python", "laptop"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining attempts:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The word was:", word)