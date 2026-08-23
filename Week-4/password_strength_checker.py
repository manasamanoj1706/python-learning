# Password Strength Checker


def check_password(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    return score


def main():

    try:
        password = input("Enter your password: ")

        if not password:
            raise ValueError("Password cannot be empty.")

        score = check_password(password)

        print("\n========== PASSWORD CHECK ==========")
        print("Score:", score, "/ 5")

        if score == 5:
            print("Strength: Very Strong 🔐")
        elif score >= 4:
            print("Strength: Strong 💪")
        elif score >= 3:
            print("Strength: Medium")
        elif score >= 2:
            print("Strength: Weak")
        else:
            print("Strength: Very Weak")

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Password checking completed.")


main()