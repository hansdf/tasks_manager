import os, sys
from datetime import date

# roadmap for this project!

# create a main class to act as menu / body, showing all the tasks
# create methods to add, delete, and update(task done/changed) tasks (read about CRUD)

# implement some sort of db system to save the tasks list when finished
    # experiment with JSON?

# additional functionality with more advanced methods, such as search or filter specific tasks

def main():
    while True:
        show_menu()
        keypress = input("enter q to quit ")
        if keypress == "q":
            sys.exit()

def show_menu(): # this shows the "main menu" of our program, with the options for each function
    today = date.today()
    print("Hans's tasks :)")
    print(f"Current date is {today}")
    print("Current tasks open are: ")

def list_tasks(): # shows a list of all the tasks, incluiding the ones marked as complete
    pass

def add_task(): # adds a new task to the start of the list
    pass

def remove_task(): # remove a task
    pass

if __name__ == "__main__":
    main()