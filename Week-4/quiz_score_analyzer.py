# Quiz Score Analyzer

import random


def generate_scores():
    scores = []

    for _ in range(5):
        scores.append(random.randint(0, 100))

    return scores


def analyze_scores(scores):

    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("\n========== QUIZ SCORE ANALYZER ==========")

    for number, score in enumerate(scores, start=1):
        print(f"Quiz {number}: {score}")

    print("-----------------------------------------")
    print("Total   :", total)
    print("Average :", round(average, 2))
    print("Highest :", highest)
    print("Lowest  :", lowest)

    if average >= 90:
        print("Grade   : A+")
    elif average >= 80:
        print("Grade   : A")
    elif average >= 70:
        print("Grade   : B")
    elif average >= 60:
        print("Grade   : C")
    else:
        print("Grade   : F")


def main():

    try:
        print("Generating random quiz scores...")

        scores = generate_scores()

        analyze_scores(scores)

    except Exception as error:
        print("Error:", error)

    finally:
        print("\nScore analysis completed.")


main()