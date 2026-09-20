import csv

FILE = "students.csv"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def search_student():
    roll = input("Enter Roll Number to search: ")

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                print("Student Found")
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                return

    print("Student not found.")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    with open(FILE, "r") as file:
        students = list(csv.DictReader(file))

    found = False

    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Roll Number", "Name", "Marks"]
        )
        writer.writeheader()

        for student in students:
            if student["Roll Number"] == roll:
                found = True
            else:
                writer.writerow(student)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")