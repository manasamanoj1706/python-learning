print("===== QUIZ LEADERBOARD =====")

players = []

while True:
    print("\n1. Add player score")
    print("2. View leaderboard")
    print("3. Find highest score")
    print("4. Search player")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Player name: ")

        try:
            score = int(input("Enter score: "))

            if score < 0:
                raise ValueError("Score cannot be negative.")

            players.append({
                "name": name,
                "score": score
            })

            print("Score added! ✅")

        except ValueError as error:
            print("Error:", error)

    elif choice == "2":
        if not players:
            print("No scores available.")

        else:
            print("\n===== LEADERBOARD =====")

            ranked = sorted(
                players,
                key=lambda player: player["score"],
                reverse=True
            )

            for position, player in enumerate(ranked, start=1):
                print(
                    f"{position}. {player['name']} "
                    f"- {player['score']} points"
                )

    elif choice == "3":
        if not players:
            print("No players available.")

        else:
            highest = max(players, key=lambda player: player["score"])

            print(
                f"🏆 Highest score: {highest['name']} "
                f"- {highest['score']} points"
            )

    elif choice == "4":
        name = input("Enter player name: ")
        found = False

        for player in players:
            if player["name"].lower() == name.lower():
                print(f"Score: {player['score']} points")
                found = True
                break

        if not found:
            print("Player not found ❌")

    elif choice == "5":
        print("Quiz leaderboard closed! 👋")
        break

    else:
        print("Invalid choice ❌")