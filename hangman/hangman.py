import random

def play_game():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden = "-" * len(word)
    attempts = 8
    guessed_letters = set()

    print("HANGMAN")
    print(hidden)

    while attempts > 0:
        guess = input("Input a letter:\n>>> ")

        # перевірка введення
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if not guess.isalpha() or not guess.islower():
            print("Please enter a lowercase English letter")
            continue
        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(guess)

        if guess in word:
            # розкриваємо літери
            new_hidden = ""
            for i in range(len(word)):
                if word[i] == guess or hidden[i] != "-":
                    new_hidden += word[i]
                else:
                    new_hidden += "-"
            hidden = new_hidden
            print(hidden)
            if hidden == word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1
            print(hidden)

    print("You lost!")

def main():
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit:\n>>> ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break
        else:
            continue

if __name__ == "__main__":
    main()
