# Number Guessing Game

import random


def play_game():
    try:
        secret_number = random.randint(1, 100)
        attempts = 0

        print("\n===== NUMBER GUESSING GAME =====")
        print("Guess a number between 1 and 100!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    raise ValueError("Enter a number between 1 and 100.")

                if guess < secret_number:
                    print("Too low! Try again.")

                elif guess > secret_number:
                    print("Too high! Try again.")

                else:
                    print("\n🎉 Correct!")
                    print("The number was:", secret_number)
                    print("Attempts:", attempts)
                    break

            except ValueError as error:
                print("Error:", error)

    except Exception as error:
        print("Something went wrong:", error)

    finally:
        print("Game finished!")


play_game()