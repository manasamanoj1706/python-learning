# Rock Paper Scissors Game

import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def decide_winner(player, computer):

    if player == computer:
        return "draw"

    if (
        (player == "rock" and computer == "scissors")
        or
        (player == "paper" and computer == "rock")
        or
        (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


def play_game():

    player_score = 0
    computer_score = 0

    print("\n================================")
    print("     ROCK PAPER SCISSORS")
    print("================================")

    while True:

        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4":
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice!")
            continue

        options = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        player = options[choice]
        computer = get_computer_choice()

        print("\nYou chose:", player)
        print("Computer chose:", computer)

        result = decide_winner(player, computer)

        if result == "player":
            print("🎉 You win!")
            player_score += 1

        elif result == "computer":
            print("Computer wins!")
            computer_score += 1

        else:
            print("It's a draw!")

        print("Your Score:", player_score)
        print("Computer Score:", computer_score)

    print("\n========== FINAL SCORE ==========")
    print("Your Score:", player_score)
    print("Computer Score:", computer_score)
    print("Thanks for playing!")


try:
    play_game()

except Exception as error:
    print("Something went wrong:", error)

finally:
    print("Game closed.")