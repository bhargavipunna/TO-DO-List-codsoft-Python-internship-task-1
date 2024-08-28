def add_do(task):
    n = input("\nEnter the no.of tasks:")
    if not n.isdigit():
        print("Invalid input. Please enter a number.")
        return

    n = int(n)
    count = 0
    for i in range(1, n + 1):
        task_name = input(f"Enter task {i}:")
        if not task_name.replace(" ", "").isalpha():
            print("Invalid task name. Task names should only contain letters and spaces.")
        elif task_name in task:
            print(f"Task '{task_name}' already exists.Please enter a unique task. ")
        else:
            task.append(task_name)
            count = count + 1

    if count > 0:
        print("========Tasks added successfully!=========")
    else:
        print('No task added')


def update(task):
    try:
        i = int(input("\nEnter the task to be updated:"))
        if 1 <= i <= len(task):
            t = input("task should be updated to:")
            if t.replace(" ", "").isalpha():
                task[i-1] = t
                print("=======Task updated successfully!=========")
            else:
                print("Invalid task name. Task names should only contain letters and spaces.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Please enter a valid number.")


def display(task):
    if not task:
        print("No tasks available.")
        return
    print("\nCurrent Tasks:")
    for i, tasks in enumerate(task, start=1):
        print(f"{i}.{tasks}")


def mark(task):
    if not task:
        print("No tasks to mark as done.")
        return

    display(task)
    try:
        i = int(input("\nEnter the task index to mark as done: "))
        if 1 <= i <= len(task):
            removed_task = task.pop(i-1)
            print(f"Task '{removed_task}' marked as done and removed.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Please enter a valid number.")


def clear_all(task):
    confirmation = input("\nAre you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        task.clear()
        print("All tasks have been cleared.")
    else:
        print("Clear operation cancelled.")


task = []
print("------------------------")
print("Welcome to TO-DO... list")
print("------------------------")


while True:
    print("\nFeatures:")
    print("1. Add task\n2. Update task\n3. Mark task as completed\n4. Display all tasks\n5. Clear all tasks\n-1. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_do(task)
    elif choice == 2:
        display(task)
        update(task)
    elif choice == 3:
        mark(task)
    elif choice == 4:
        display(task)
    elif choice == 5:
        clear_all(task)
    elif choice == -1:
        print("Exiting. Thank you for using the TO-DO List!c")
        break
    else:
        print("Enter the correct choice")
