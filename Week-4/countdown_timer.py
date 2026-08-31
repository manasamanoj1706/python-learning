# Countdown Timer

import time


def countdown(seconds):

    while seconds > 0:

        minutes = seconds // 60
        remaining_seconds = seconds % 60

        print(
            f"\rTime remaining: {minutes:02d}:{remaining_seconds:02d}",
            end=""
        )

        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")


def main():

    try:
        seconds = int(input("Enter countdown time in seconds: "))

        if seconds <= 0:
            raise ValueError("Enter a positive number.")

        print("\nCountdown started!")
        countdown(seconds)

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Timer completed.")


main()