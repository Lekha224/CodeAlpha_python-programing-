import random

# List of words
words = ['cat', 'dog', 'bat', 'rat']

# Randomly select a word
word = random.choice(words)

# Display word as underscores
guessed_word = ['_'] * len(word)

# Number of attempts
attempts = 6

# Game loop
while attempts > 0:
    print(' '.join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"Incorrect! Attempts left: {attempts}")

    if '_' not in guessed_word:
        print(f"Congratulations! You guessed the word '{word}'!")
        break

if attempts == 0:
    print(f"Game over! The word was '{word}'.")
