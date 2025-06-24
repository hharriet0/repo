class Task:
    def __init__(self,taskName,Done,Priority,Description):
        self.taskName = taskName
        self.Done = Done
        self.Priority = Priority
        self.Description = Description


    # def create(self):
    #     taskName = input("Enter the task you want to add to the list : ")
    #     count = 0
    #     for x in self.list:
    #         if x != "":
    #             count += 1
    #         else:
    #             StopIteration
            
                
        # desc = input("Do you want to add a description?")
        # if desc.lower() == "yes":
        #     d = input("Enter your description to be assigned to the task : ")
        #     desc_listt.append(d[count])

    def Create():
        taskName = input("Please enter the name of the task : ")
        Done = bool(input("Please enter, in boolean, whether the task is done or not."))
        Priority = str(input("What is the priority of the task from 1-10?"))
        Description = str("Enter a description of the task.")
        x = Task(taskName,Done,Priority)
    
    def view():
        y = input("Enter the task you want to view.")
        for i in list:
            if y == i:
                print("The task you want to view is "+i)

    







        





