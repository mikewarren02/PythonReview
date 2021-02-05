
def todo():

    tasks = {}

    def display_tasks():
        print(" Current Tasks: ")
        for index, (key, value) in enumerate(tasks.items()):
                print(index + 1, key, value)


    while True:
        print("Press 1 to Add Task") 
        print("Press 2 to Delete Task")
        print("Press 3 to View All tasks")
        print("Press q to quit ")
        

        action = input(" ")

        if action == "q":
            break

        if action == "1":

            title = input("Enter The Task : ")
            priority = input("Priority level (1-10): ")
            tasks[title] = priority
            display_tasks()

            choice = input("Enter q to quit or any key to continue: ")
            if choice == "q":
                break

        elif action == "2":
            
            for index, (key, value) in enumerate(tasks.items()):
                print(index + 1, key, value)

            delete = int(input("Which task to delete? : "))
            task = delete - 1

            toDelete = list(tasks)[task]
            print(task)
            del tasks[toDelete]
            display_tasks()



        elif action == "3":
            print(" Current Tasks: ")
            display_tasks()
            
        

    print("Thanks for using the TODO list !")

todo()