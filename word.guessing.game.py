import random

def display_word(word, guesses):
    return "".join(letter if letter in guesses else "_" for letter in word)

def play():
    name = input("Please enter your name: ").strip()
    print(f"\nHey, welcome {name}!")

    words = [
        'rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water'
    ]

    word = random.choice(words)
    guesses = set()
    rounds = len(word)

    while rounds > 0:
        print(f"\n-------> Rounds left: {rounds} <-------")
        print(display_word(word, guesses))

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Enter ONE valid letter only.")
            continue

        if guess in guesses:
            print("⚠️ You already guessed that.")
            continue

        guesses.add(guess)

        if guess not in word:
            print("Wrong!")
            rounds -= 1
        else:
            print("Correct!")

        # Check win
        if all(letter in guesses for letter in word):
            print(f"\n🎉 You won! The word was: {word}")
            return

    print(f"\n💀 Game over! You lost.\nThe word was: {word}")

play()

