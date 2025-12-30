import random as rm

word_bank = [
    "apple", "chair", "house", "water", "bread",
    "smile", "light", "green", "table", "clock",
    "phone", "shirt", "plant", "music", "river"
]

def get_random_word():
    return rm.choice(word_bank)

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
    word = get_random_word()
    guess_word = ['_'] * len(word)
    guessed_letters = set()
    attempts = 10
    
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
    if attempts == 0  and "_" in guess_word:
        print(f"Game Over!\nThe word was {word}")
        
play_game()