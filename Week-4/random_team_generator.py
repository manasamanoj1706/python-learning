# Random Team Generator

import random


def create_teams():

    try:
        names = input("Enter names separated by commas: ").split(",")

        names = [name.strip() for name in names if name.strip()]

        if len(names) < 2:
            raise ValueError("Enter at least 2 names.")

        team_size = int(input("Enter team size: "))

        if team_size <= 0:
            raise ValueError("Team size must be greater than zero.")

        random.shuffle(names)

        print("\n========== RANDOM TEAMS ==========")

        team_number = 1

        for i in range(0, len(names), team_size):

            team = names[i:i + team_size]

            print("\nTeam", team_number)

            for member in team:
                print("-", member)

            team_number += 1

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nTeam generation completed.")


create_teams()