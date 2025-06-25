tasks = []
completed = []
class Task:
    def __init__(self, name,done):
        self.name = name
        self.done = False
 
    def str(self):
        status = "✓" if self.done else "✗"
        return "{self.name} [{status}]"
 
def add():
        count = int(input("How many tasks do you want to add? "))
        for x in range(count):
            name=input("Enter task: ")
            if name:
                tasks.append(Task(name,False))
 
def done():
    name = input("Enter the name of the task completed: ")
    for task in tasks:
        if task == name and not task.done:
            task.done = True
            completed.append(task)
            print(f"Marked '{task.name}' as done")
            return
    print("Couldn't find that task or it's already done")
 
def view():
    print(" To Do:")
    for task in tasks:
        if not task.done:
            print(f-task)
    print("Completed Tasks:")
    for task in completed:
        print(" {task}")
    print()
 
def main():
    add()
    view()
   
    while True:
        choice = input("Mark a task as done? (yes/no): ")
        if choice in ["yes", "y"]:
            done()
            view()
        else:
            print("Goodbye!")
            break
 
main()