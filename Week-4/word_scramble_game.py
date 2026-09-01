# Word Scramble Game

import random


def play_game():
    words = [
        "python",
        "computer",
        "developer",
        "programming",
        "database",
        "machine"
    ]

    word = random.choice(words)
    scrambled = list(word)

    random.shuffle(scrambled)
    scrambled_word = "".join(scrambled)

    print("\n==============================")
    print("       WORD SCRAMBLE")
    print("==============================")
    print("Unscramble this word:")
    print("👉", scrambled_word)

    attempts = 3

    while attempts > 0:

        guess = input("Your answer: ").lower().strip()

        if guess == word:
            print("🎉 Correct! You won!")
            return

        attempts -= 1

        if attempts > 0:
            print("Wrong answer!")
            print("Attempts left:", attempts)

    print("\n😅 Game over!")
    print("The correct word was:", word)


def main():

    try:
        play_game()

    except Exception as error:
        print("Error:", error)

    finally:
        print("\nGame finished!")


main()