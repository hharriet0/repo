tasks = []
completed = []

class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"{self.name} [{status}]"

def add():
    count = int(input("How many tasks do you want to add? "))
    for _ in range(count):
        name = input("Enter task: ")
        if name:
            tasks.append(Task(name))

def done():
    name = input("Enter the name of the task completed: ")
    for task in tasks:
        if task.name == name and not task.done:
            task.done = True
            completed.append(task)
            print(f"Marked '{task.name}' as done")
            if task.name == name and task.done:
                c = input("would you like to remove this task from the list?")
            if c == "yes":
                for i in tasks:
                    if i == {task.name}:
                        tasks.remove(i)
                        print("Removed!")
            else:
                print("understood!")
            return
    print("Couldn't find that task or it's already done")

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
        choice = input("Mark a task as done? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            done()
            view()
        else:
            print("Goodbye!")
            break

main()