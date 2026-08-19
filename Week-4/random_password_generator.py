# Random Password Generator

import random
import string


def generate_password():
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            raise ValueError("Password length must be at least 4.")

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

    except ValueError as error:
        print("Error:", error)


generate_password()