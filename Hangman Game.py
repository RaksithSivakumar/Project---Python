import random


words = ["python", "java", "ruby", "javascript", "html", "css", "swift", "kotlin", "php", "cplusplus"]

def select_word(words):
    
    return random.choice(words)

def display_word(word, guessed_letters):
    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():

    
    word = select_word(words)
    
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("Incorrect! Attempts left:", attempts_left)
            if attempts_left == 0:
                print("Sorry, you've run out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

    hangman()

    
