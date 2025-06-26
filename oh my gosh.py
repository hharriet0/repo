tasks = []
completed = []
file = open("memory.txt","a")

class Task:
    def __init__(self, name, description="", done=False):
        self.name = name
        self.description = description
        self.done = done

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"{self.name} [{status}] - {self.description}"

def add():
    count = int(input("How many tasks do you want to add? "))
    for _ in range(count):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        if name:
            tasks.append(Task(name, description))

def done():
    name = input("Enter the name of the task completed: ")
    for task in tasks[:]:
        if task.name == name and not task.done:
            task.done = True
            c = input("Would you like to remove this task from the list? (yes/no): ").lower()
            if c in ["yes", "y"]:
                tasks.remove(task)
                print("Removed!")
            else:
                completed.append(task)
                print("Marked as done and kept in completed list.")
            return
    print("Couldn't find that task or it's already marked done.")

def edit_description():
    name = input("Enter the name of the task to edit: ")
    for task in tasks + completed:
        if task.name == name:
            print(f"Current description: {task.description}")
            new_desc = input("Enter new description: ")
            task.description = new_desc
            print("Description updated!")
            return
    print("Task not found.")

def view():
    print("\nTo Do:")
    for task in tasks:
        if not task.done:
            print(f"  {task}")
    print("Completed Tasks:")
    for task in completed:
        print(f"  {task}")
    print()

def main():
    add()
    view()

    while True:
        print("\nOptions: [done] mark done, [edit] edit description, [view] show tasks, [exit] to quit")
        choice = input("What would you like to do? ").strip().lower()
        
        if choice in ["done"]:
            done()
        elif choice in ["edit"]:
            edit_description()
        elif choice in ["view"]:
            view()
        elif choice in ["exit", "no", "n"]:
            file.write("Tasks currently completed : ",completed,"\n","Tasks to do : ",tasks,)
            print("Goodbye!")
            file.close()
            break
        else:
            print("Invalid option. Try again.")

main()