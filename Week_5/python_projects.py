# @title 2. To-Do List Application
# Initialize tasks list
tasks = []
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
def remove_task():
    display_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
def mark_task_complete():
    display_tasks()
    try:
        task_num = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= task_num < len(tasks):
            print(f"Task '{tasks[task_num]}' marked complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")
def display_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved.")
def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks.")
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task complete")
        print("4. Display tasks")
        print("5. Save tasks")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            save_tasks()
            break
        else:
            print("Invalid choice.")
main()


# @title 13. Email Slicer(Extract Username from Email)
def email_slicer(email):
    try:
        # Split the email at '@'
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        # Handle invalid email format
        return None, None

def main():
    # Get email from user
    email = input("Enter an email address: ")
   
    # Validate if email contains '@'
    if '@' not in email:
        print("Invalid email format. Email should contain '@'.")
    else:
        username, domain = email_slicer(email)
        if username and domain:
            print(f"Username: {username}")
            print(f"Domain: {domain}")
        else:
            print("Failed to parse email.")
main()





















