import pickle
import os

class TaskManager:
    def __init__(self):
        self.categories = {}
        self.filename = "tasks.dat"
        self.load_tasks()

    def add_task(self, category, task):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(task)

    def pop_task(self, category):
        if category in self.categories and self.categories[category]:
            task = self.categories[category].pop(0)
            if not self.categories[category]:
                del self.categories[category]
            return task
        else:
            return None

    def merge_categories(self, source_category, destination_category):
        if source_category in self.categories and destination_category in self.categories:
            self.categories[destination_category].extend(self.categories[source_category])
            del self.categories[source_category]
        else:
            return "Invalid category names."

    def list_category(self, category):
        if category in self.categories:
            return self.categories[category]
        else:
            return "Invalid category name."

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.categories, file)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.categories = pickle.load(file)

def main():
    task_manager = TaskManager()

    print("\nTask Manager Options:")
    print("add <category> <task>")
    print("pop <category>")
    print("merge <source_category> <destination_category>")
    print("list <category> (use only when necessary)")
    print("quit")

    while True:
        print(f"\nCategories: {list(task_manager.categories.keys())}")

        command = input("Enter your command: ").strip().split()

        if len(command) == 0:
            print("Invalid command. Please try again.")
            continue

        action = command[0].lower()

        if action == 'add':
            if len(command) < 3:
                print("Invalid command. Usage: add <category> <task>")
            else:
                category = command[1]
                task = ' '.join(command[2:])
                task_manager.add_task(category, task)
                print(f"Task '{task}' added to category '{category}'.")

        elif action == 'pop':
            if len(command) < 2:
                print("Invalid command. Usage: pop <category>")
            else:
                category = command[1]
                popped_task = task_manager.pop_task(category)
                if popped_task:
                    print(f"Popped task from '{category}': {popped_task}")
                else:
                    print(f"No tasks available in the '{category}' category.")

        elif action == 'merge':
            if len(command) < 3:
                print("Invalid command. Usage: merge <source_category> <destination_category>")
            else:
                source_category = command[1]
                destination_category = command[2]
                result = task_manager.merge_categories(source_category, destination_category)
                if result:
                    print(result)
                else:
                    print(f"Categories '{source_category}' and '{destination_category}' merged successfully.")

        elif action == 'list':
            if len(command) < 2:
                print("Invalid command. Usage: list <category>")
            else:
                category = command[1]
                result = task_manager.list_category(category)
                print(result)

        elif action == 'quit':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid command. Please try again.")

        task_manager.save_tasks()

if __name__ == "__main__":
    main()
