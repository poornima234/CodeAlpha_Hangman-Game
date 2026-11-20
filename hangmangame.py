
import random

# List of 5 predefined words
words = ["apple", "banana", "python", "school", "tiger"]

secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("===== WELCOME TO HANGMAN =====")

while incorrect_guesses < max_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)
    
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break


    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)


    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")


if incorrect_guesses == max_guesses:
    print("\nGame Over! You ran out of guesses.")
    print("The correct word was:", secret_word)

print("\n===== THANK YOU FOR PLAYING =====")
