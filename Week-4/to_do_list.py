# To-Do List Manager

tasks = []


def add_task():
    task = input("Enter a task: ").strip()

    if task:
        tasks.append({
            "task": task,
            "completed": False
        })
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TO-DO LIST ==========")

    for number, item in enumerate(tasks, start=1):

        status = "✓ Completed" if item["completed"] else "Pending"

        print(f"{number}. {item['task']} - {status}")


def complete_task():

    try:
        view_tasks()

        if not tasks:
            return

        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            raise ValueError("Invalid task number.")

        tasks[number - 1]["completed"] = True

        print("Task marked as completed!")

    except ValueError as error:
        print("Error:", error)


def delete_task():

    try:
        view_tasks()

        if not tasks:
            return

        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            raise ValueError("Invalid task number.")

        removed = tasks.pop(number - 1)

        print("Deleted:", removed["task"])

    except ValueError as error:
        print("Error:", error)


def main():

    while True:

        print("\n==============================")
        print("       TO-DO LIST MANAGER")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()