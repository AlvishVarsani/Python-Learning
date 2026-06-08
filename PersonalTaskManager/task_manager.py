from task import Task


class TaskManager:

    def add_task(self, task, file_path):
        try:
            with open(file_path, 'a') as file:
                file.write(
                    f"{task.task_id},{task.title},{task.description},{task.priority},{task.completed}\n"
                )
        except Exception as e:
            print(f"Error adding task: {e}")

    def view_tasks(self, file_path):
        try:
            with open(file_path, 'r') as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks found.")
                return

            for task in tasks:
                parts = task.strip().split(',')

                task_id, title, description, priority, completed = parts
                print(
                    f"Task ID: {task_id}, Title: {title}, "
                    f"Description: {description}, Priority: {priority}, Completed: {completed}"
                )

        except FileNotFoundError:
            print("File not found. No tasks available yet.")

        except Exception as e:
            print(f"Error reading tasks: {e}")

    def mark_complete(self, target_id, file_path):
        try:
            with open(file_path, 'r') as file:
                tasks = file.readlines()

            updated_tasks = []

            for task in tasks:
                parts = task.strip().split(',')

                task_id, title, description, priority, completed = parts

                if task_id == target_id:
                    if completed == 'False':
                        completed = 'True'
                        print("Task marked as completed.")
                    else:
                        print("Task is already completed.")

                updated_tasks.append(
                    f"{task_id},{title},{description},{priority},{completed}\n"
                )

            with open(file_path, 'w') as file:
                file.writelines(updated_tasks)

        except FileNotFoundError:
            print("File not found. Cannot update task.")

        except Exception as e:
            print(f"Error updating task: {e}")

    def delete_task(self, target_id, file_path):
        try:
            with open(file_path, 'r') as file:
                tasks = file.readlines()

            updated_tasks = []

            for task in tasks:
                parts = task.strip().split(',')
                task_id, title, description, priority, completed = parts

                if task_id != target_id:
                    updated_tasks.append(task)

            with open(file_path, 'w') as file:
                file.writelines(updated_tasks)

            print("Task deleted successfully (if ID existed).")

        except FileNotFoundError:
            print("File not found. Nothing to delete.")

        except Exception as e:
            print(f"Error deleting task: {e}")