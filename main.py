import random as rm

word_bank = [
    "apple", "chair", "house", "water", "bread",
    "smile", "light", "green", "table", "clock",
    "phone", "shirt", "plant", "music", "river"
]

word = rm.choice(word_bank)

guessWord = ['_'] * len(word)

attempts = 10
guess_letters = set()
while attempts > 0:
    print("Current word: "+" ".join(guessWord))
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha:
        print(f"⚠️  Please enter a single letter only")
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        if guess in guess_letters:
            print(f"You already guessed that letter")
            continue    
        guess_letters.add(guess)
        print(f"Great guess 😊")  
        
    else:
        attempts -= 1
        print(f"Wrong guess ❌ {attempts} attempts remaining !!")
        
    if '_' not in guessWord:
        print(f"Congratulations 🎉 You guess the word {word}")
        break
    
    if attempts == 0  and "_" in guessWord:
        print(f"Game Over!\nThe word was {word}")