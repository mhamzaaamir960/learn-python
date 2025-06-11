import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file if it exists"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, description=""):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            print(f"[{status}] {task['id']}. {task['title']}")
            if task['description']:
                print(f"   Description: {task['description']}")
            print(f"   Created: {task['created_at']}")
            print("-" * 50)

    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task '{task['title']}' marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")

    def delete_task(self, task_id):
        """Delete a task"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task '{task['title']}' deleted successfully!")
                return
        print(f"Task with ID {task_id} not found!")

def main():
    todo = TodoApp()
    
    while True:
        print("\n=== Todo App ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            todo.add_task(title, description)
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo.complete_task(task_id)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 