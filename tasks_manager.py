import os, sys
from datetime import date

# roadmap for this project!

# create a main class to act as menu / body, showing all the tasks
# create methods to add, delete, and update(done/changed) tasks (read about CRUD)

# implement some sort of db system to save the tasks list when finished
    # experiment with JSON?

# additional functionality with more advanced methods, such as search or filter specific tasks

def main():
    
    while True:
        show_menu()
        keypress = input("press q to exit ")
        if keypress == "q":
            sys.exit()

def show_menu():
    today = date.today()
    print("Hans's tasks :)")
    print(f"Current date is {today}")
    print("Task 1...")
    print("Task 2...")
    print("Task 3...")
    print("Task 4...")
    print("Task 5...")

if __name__ == "__main__":
    main()