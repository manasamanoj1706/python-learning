questions = {
    1: {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    2: {
        "question": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    3: {
        "question": "2 + 5 = ?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    }
}

students = {}

while True:
    print("\n===== ONLINE EXAMINATION SYSTEM =====")
    print("1. Register Student")
    print("2. Start Exam")
    print("3. View Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        reg_no = input("Enter Register Number: ")

        if reg_no in students:
            print("Student already registered.")
        else:
            name = input("Enter Name: ")
            students[reg_no] = {
                "name": name,
                "score": 0
            }
            print("Registration Successful!")

    elif choice == "2":
        reg_no = input("Enter Register Number: ")

        if reg_no not in students:
            print("Student not found.")
            continue

        score = 0

        for q in questions.values():
            print("\n" + q["question"])

            for option in q["options"]:
                print(option)

            answer = input("Enter Answer (A/B/C/D): ").upper()

            if answer == q["answer"]:
                score += 1

        students[reg_no]["score"] = score

        print