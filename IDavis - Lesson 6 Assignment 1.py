def main():
    print("Student Information Program — Manage Student Data\n")

    # Empty dictionary to store student information
    students = {}

    # --- Create Students ---
    # Example data (you can modify or use input() instead)
    students["Jake"] = {
        "id": 2,
        "gpa": 3.8,
        "credits-completed": 90,
        "grades": [89, 90, 100, 88]
    }

    students["Sarah"] = {
"id": 2,
"gpa": 3.8,
"credits-completed": 120,
"grades": [100, 98, 95, 97]
}

    students["Liam"] = {
        "id": 3,
        "gpa": 2.9,
        "credits-completed": 60,
        "grades": [70, 75, 80, 68]
    }

    # --- Print all student names ---
    print("=== Student Names ===")
    for name in students.keys():
        print(name)
    print()

    # --- Print all student information ---
    print("=== Accessing Student Information ===")
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    for name, info in students.items():
        print(f"{name}\t{info['id']}\t{info['gpa']}\t{info['credits-completed']}\t\t{info['grades']}")
    print()

    # --- Remove a student ---
    print("=== Removing a Student ===")
    removed = students.pop("Liam", None)
    if removed:
       print(f"Removed student: Liam\n")
    else:
       print("Student 'Liam' not found.\n")

    print("Updated Student List:")
    for name, info in students.items():
        print(f"{name}: {info}")
    print()

    # --- Access GPA Information ---
    print("=== Accessing GPA Information ===")
    for name in students:
        gpa = students[name].get("gpa")
        print(f"{name}'s GPA: {gpa}")
    print()

    # --- Clear All Students ---
    print("=== Clearing All Students ===")
    students.clear()
    print("All students removed. Current dictionary:", students)
    print()

    # --- Completion Message ---
    print("Completed by, [Isaac Davis]")

 
