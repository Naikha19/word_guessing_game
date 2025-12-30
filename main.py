import random as rm

easy_words = [
    "apple", "chair", "house", "water", "bread",
    "smile", "light", "green", "table", "clock"
]

medium_words = [
    "python", "library", "picture", "holiday",
    "monster", "journey", "battery", "science"
]

hard_words = [
    "programming", "architecture", "intelligence",
    "cybersecurity", "cryptography", "biotechnology"
]

def choose_difficulty():
    while True:
        print(f"\nChoose difficulty.")
        print(f"1️⃣  Easy")
        print(f"2️⃣  Medium")
        print(f"3️⃣  Hard")

        choice = input("Enter 1,2 or 3: ")
        if choice == "1":
            return easy_words,12
        elif choice == "2":
            return medium_words,9
        elif choice == "3":
            return hard_words,6
        else:
            print("Invalid choice! Try again")
            
def get_random_word(word_list):
    return rm.choice(word_list)

def display_state(attempts, guessed_letters, guess_word):
    print(f"\nAttempts remaining: {attempts}")
    print("Current word: "+" ".join(guess_word))
    print("Guessed letters: "+" ".join(sorted(guessed_letters)))
    
def get_valid_guess(guessed_letters):
    #Input check
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print(f"⚠️  Please enter a single letter only")
        elif guess in guessed_letters:
            print(f"⚠️  You already guessed that letter")
        else:
            return guess
def update_word(word, guess_word,guess):
    found = False
    for i in range(len(word)):
        if word[i] == guess:
            guess_word[i] = guess
            found = True
    return  found         

def play_game():
    word_list, attempts = choose_difficulty()
    word = get_random_word(word_list)
    guess_word = ['_'] * len(word)
    guessed_letters = set()
    
    while attempts > 0:    
        display_state(attempts,guessed_letters, guess_word)  

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if update_word(word,guess_word,guess):
            print(f"Great guess 😊")
        else:
            attempts -= 1
            print("Wrong guess ❌")
        
        if "_" not in guess_word:
            print(f"Congratulations 🎉 You guessed the word '{word}'")
            return

    print(f"Game Over!\nThe word was {word}")
        
play_game()