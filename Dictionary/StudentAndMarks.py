students = {}

while True:
    char = input(
        "'A' - Add a student\n"
        "'B' - Update marks\n"
        "'C' - Search for a student\n"
        "'D' - Display all students and marks\n"
        "'E' - Exit\n"
        "Enter a key (A/B/C/D/E): "
    ).upper()

    match char:

        case 'A':
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))

            students[name] = marks

            print(f"Student {name} added successfully.")
        
        case 'B':
            name = input("Enter student name: ")

            if name not in students:
                print(f"Student {name} does not exist!")
            else:
                updated_marks = int(input("Enter updated marks: "))
                students[name] = updated_marks

            print(f"Marks updated successfully.")

        case 'C':
            name = input("Enter student name: ")
            if name not in students:
                print(f"Student {name} does not exist!")
            else:
                print(f"Student {name} has {students[name]} marks.")
        
        case 'D':
            if not students:
                print("No students found.")
            else:
                print("Students and marks:")

                for name, marks in students.items():
                    print(f"{name}: {marks}")

        case 'E':
            print("Thank you!")
            break

        case _:
            print("Invalid input")