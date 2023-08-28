def add():
    try:
        with open('todo.txt', 'a') as file:
            a = input("Enter The Task : ")
            file.write(a + "\n")
    except FileNotFoundError:
        print("The file 'todo.txt' does not exist.")


def read_tasks():
    try:
        with open('todo.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file 'todo.txt' does not exist.")


def remove():
    try:
        with open('todo.txt', 'r') as file:
            lines = file.readlines()

        read_tasks()
        a = int(input("Which Line Do You want To Remove? : "))
        if 1 <= a <= len(lines):
            del lines[a - 1]
            with open('todo.txt', 'w') as file:
                file.writelines(lines)
            print(f"Line {a} is removed successfully")
        else:
            print(f"Line {a} not in list")
            print(f"There are only {len(lines)}lines in your List")
    except FileNotFoundError:
        print("The file 'todo.txt' does not exist.")

def main():
    while True:
        a = input("1. Add Task\n2. Remove Task\n3. Display Task\n4. Exit\nSelect An Option : ")
        if a == "1":
            add()
        elif a == "2":
            remove()
        elif a == "3":
            read_tasks()
        elif a == "4":
            print("Exiting!!")
            exit()
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
