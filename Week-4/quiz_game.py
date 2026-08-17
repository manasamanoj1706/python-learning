# Quiz Game

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Program Unit",
            "B. Central Processing Unit",
            "C. Computer Processing User",
            "D. Control Processing Unit"
        ],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    }
]


def start_quiz():
    score = 0

    print("\n==============================")
    print("       PYTHON QUIZ GAME")
    print("==============================")

    for number, question in enumerate(questions, start=1):

        print("\nQuestion", number)
        print(question["question"])

        for option in question["options"]:
            print(option)

        try:
            answer = input("Enter your answer (A/B/C/D): ").upper()

            if answer not in ["A", "B", "C", "D"]:
                raise ValueError("Please enter A, B, C, or D.")

            if answer == question["answer"]:
                print("Correct! 🎉")
                score += 1
            else:
                print("Wrong answer.")

        except ValueError as error:
            print("Error:", error)

    print("\n==============================")
    print("         QUIZ RESULT")
    print("==============================")
    print("Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100

    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Excellent performance! 🌟")
    elif percentage >= 50:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")


def main():
    try:
        while True:

            print("\n1. Start Quiz")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                start_quiz()

            elif choice == "2":
                print("Thanks for playing!")
                break

            else:
                print("Invalid choice.")

    except Exception as error:
        print("Unexpected error:", error)

    finally:
        print("Quiz program closed.")


main()