import os, sys
from datetime import date

# roadmap for this project!

# create a main class to act as menu / body, showing all the tasks
# create methods to add, delete, and update(task done/changed) tasks (read about CRUD)

# implement some sort of db system to save the tasks list when finished
    # experiment with JSON?

# add error handling

# additional functionality with more advanced methods, such as search or filter specific tasks


dict_of_tasks = {} # global dictionary to hold tasks, for ease access from the different functions such as add, remove, etc

def main():

    while True: # could maybe use a switch here instead of a bunch of ifs? 
        show_menu()
        keypress = input("enter your action:\nq(QUIT)\na(ADD NEW ITEM)\nls(LIST ITEMS)\nr(REMOVE ITEM)\n... ")
        if keypress == "q":
            sys.exit()
        elif keypress == "a":
            add_task()
        elif keypress == "ls":
            list_tasks()
        elif keypress == "r":
            remove_task()
        

def show_menu(): # this shows the "main menu" of our program, with the options for each function
    today = date.today()
    print("\nHans's tasks :)")
    print(f"Current date is {today}")
    print("Current tasks open are:\n")
    list_tasks()

def list_tasks(): # shows a list of all the tasks, incluiding the ones marked as complete, should be a dictionary?
    for key, value in dict_of_tasks.items(): # loop to print the dict line by line
        print(key, value)

    print(f"Task list has currently {len(dict_of_tasks)} items open.")

def add_task(): # adds a new task to the start of the list
    task_description = input("Enter the task description: ")
    task_id = f"Task {len(dict_of_tasks) + 1:02d}"  # task ID with leading zeroes
    dict_of_tasks[task_id] = task_description
    print(f"Task '{task_id}' added.")

def remove_task(): # remove a task
    # will use .pop()?
    pass

if __name__ == "__main__":
    main()