# To-Do List App

tasks = []  # List to hold all tasks


def add_task():
    description = input("Enter task description: ")
    due_date = input(
        "Enter due date (YYYY-MM-DD) or press Enter to skip: ") or "No due date"
    task = {"description": description,
            "due_date": due_date, "completed": False}
    tasks.append(task)
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['description']} - Due: {task['due_date']}")


def mark_complete():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= num < len(tasks):
                # Toggle status
                tasks[num]["completed"] = not tasks[num]["completed"]
                print("Task updated!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a number.")


# Main program loop
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task Complete\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
