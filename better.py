class Task:
    tasks = []  # Class variable to store all tasks

    def __init__(self, taskName, Done, Priority, Description):
        self.taskName = taskName
        self.Done = Done
        self.Priority = Priority
        self.Description = Description


    def create(cls):
        taskName = input("Enter the task name: ")
        
        done_input = input("Is the task done? (yes/no): ").strip().lower()
        Done = done_input in ["yes", "y", "true", "1"]
        
        Priority = input("Enter the priority of the task (1-10): ").strip()
        Description = input("Enter a description of the task: ").strip()

        task = cls(taskName, Done, Priority, Description)
        cls.tasks.append(task)
        print(f"Task '{taskName}' created successfully.\n")

    def view(cls):
        if not cls.tasks:
            print("No tasks available.")
            return
        
        search_name = input("Enter the name of the task to view: ")
        found = False
        for task in cls.tasks:
            if task.taskName == search_name:
                print(f"\nTask Name: {task.taskName}")
                print(f"Done: {task.Done}")
                print(f"Priority: {task.Priority}")
                print(f"Description: {task.Description}\n")
                found = True
        if not found:
            print(f"No task found with the name '{search_name}'.")

w = Task("Washing",False,10,"Do it!")
