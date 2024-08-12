#================================================================
#======== Module 2: Mini-project | To-Do list Application =======
#================================================================

# Introduction
    # In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. The objective of this project is to reinforce your understanding of Python syntax, data types, control structures, functions, and error handling while building a practical and interactive application.
#Project Requirements
    #User Interface (UI):
    #Create a command-line interface (CLI) for the To-Do List Application.
    #Display a welcoming message and a menu with the following options:

            # Welcome to the To-Do List App!
            #           Menu:
            #     1. Add a task
            #     2. View tasks
            #     3. Mark a task as complete
            #     4. Delete a task
            #     5. Quit

# 2. To-Do List Features:
    # Implement the following features for the To-Do List:
    # Adding a task.
    # Viewing the list of tasks 
    # Marking a task as complete. (Bonus) (Hint: Use string manipulation to add "X" to the end of a task)
    # Deleting a task.
    # Quitting the application.

# 3. User Interaction:
    # Allow users to interact with the application by selecting menu options using input().
    # Implement input validation to handle unexpected user input gracefully.

# 4. Error Handling:
    # Implement error handling where necessary using try, except, else, and finally blocks to handle potential issues.

# 5. Code Organization:
    # Organize your code into functions to promote modularity and readability.
    # Use meaningful function names with appropriate comments.

# 6. Testing and Debugging:
    # Thoroughly test your application to identify and fix any bugs.
    # Consider edge cases, such as empty task lists or incorrect user input.

# 7. Optional Features (Bonus):
    # If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

# 8. GitHub Repository:
    # Create a GitHub repository for your project.
    # Commit your code to the repository regularly.
    # Include a link to your GitHub repository in your project documentation.

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================


def display_menu():
    print("\n\n\n\n\n\n")
    print("Welcome to the To-Do List App!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")    
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")


def add_task(todo_list):
    task = input("Please enter the task: ")
    todo_list.append(task)
    print("Task added successfully!!!")


def view_tasks(todo_list):
    print("Tasks:")
    if len(todo_list) == 0:
        print("Im sorry. No tasks were found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


def mark_task_complete(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the number of the task to mark as complete: "))
    if 1 <= task_index <= len(todo_list):
        task = todo_list[task_index - 1]
        todo_list[task_index - 1] = task + " (X)"
        print("Task sucessfully marked as complete!!!")
    else:
        print("!!!Invalid task index!!!" "\n" "Please try again")


def delete_task(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the number of the task to delete: "))
    if 1 <= task_index <= len(todo_list):
        del todo_list[task_index - 1]
        print("Task deleted successfully!!!")
    else:
        print("!!!Invalid task index!!!" "\n" "Please try again")


def main():
    todo_list = []

    display_menu()

    while True:
        user_input = input("\nEnter your selection (1-5): ")

        if user_input == "1":
            add_task(todo_list)
        elif user_input == "2":
            view_tasks(todo_list)
        elif user_input == "3":
            mark_task_complete(todo_list)
        elif user_input == "4":
            delete_task(todo_list)
        elif user_input == "5":
            print("Thank you for using the To-Do List App. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()


                                   #======= END OF CODE =========

#Author: Roger Block