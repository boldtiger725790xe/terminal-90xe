"""Simple terminal task manager."""

def main():
    tasks = []
    while True:
        print("\nTask Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            if tasks:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("No tasks.")
        elif choice == "2":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                print("Added.")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                idx = int(input("Task number to remove: "))
                if 1 <= idx <= len(tasks):
                    tasks.pop(idx - 1)
                    print("Removed.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()