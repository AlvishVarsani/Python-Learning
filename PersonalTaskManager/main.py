from task import Task
from task_manager import TaskManager

print("="*50)
print("Welcome to Personal Task Manager")
print("="*50)  

print("1. Add Task")
print("2. View Tasks")
print("3. Mark Task as Completed")      
print("4. Delete Task")
print("5. Exit")

file_path="tasks.txt"
while True: 
    choice=input("Enter your choice: ")
    task_manager=TaskManager()

    match choice:
        case "1":
            task_id=input("Enter task id: ")
            title=input("Enter task title: ")
            description=input("Enter task description: ")
            priority =input("Enter task priority: ")
            priority = priority.capitalize()
            if priority not in ["Low", "Medium", "High"]:
                print("Invalid priority Please enter Low, Medium or High.")
                continue
            task=Task(task_id,title,description,priority)
            task_manager.add_task(task,file_path)
        case "2":
            task_manager.view_tasks(file_path)
        case "3":
            task_id=input("Enter task id to mark as completed: ")
            task_manager.mark_complete(task_id,file_path)
        case "4":
            task_id=input("Enter task id to delete: ")
            task_manager.delete_task(task_id,file_path)
        case "5":
            break
        case _:
            print("Invalid choice. Please try again.")