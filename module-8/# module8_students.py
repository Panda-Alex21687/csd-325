# module8_students.py
# Author: Alexander Baldree
# Assignment: Module-8
# Date: 2025-11-20


import json

# ------------------------------
# Function to print each student
# ------------------------------
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")
    print()  # blank line


# ------------------------------
# Main Program
# ------------------------------
def main():
    # Load JSON file
    with open("/Users/alexbaldree/csd/csd-325/module-8/student.json", "r") as file:
        students = json.load(file)


    print("Original Student List:")
    print_students(students)

    # Adds a student entry
    new_student = {
        "F_Name": "Alexander",
        "L_Name": "Baldree",
        "Student_ID": 21400194,
        "Email": "alex.baldree@example.com"
    }

    students.append(new_student)

    print("Updated Student List:")
    print_students(students)

    # Write back to JSON
    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)

    print("The JSON file has been updated.")


# Run program
if __name__ == "__main__":
    main()
