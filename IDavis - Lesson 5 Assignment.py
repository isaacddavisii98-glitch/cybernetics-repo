import random

def main():
    # Create an empty list to store grades
    grades = []

    # Input loop
    while True:
        try:
            grade = int(input("Please enter the grade or -1 to stop: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if grade == -1:
          break
        else:
          grades.append(grade)

# Print list of grades entered
        print("\nThe list of grades entered:")
        print(grades)

# -----------------------------------------
# Removing the lowest grade
        print("\n--- Removing the lowest grade ---")
        if grades:
         lowest = min(grades)
         grades.pop(grades.index(lowest))
         print("Lowest grade removed:", lowest)
         print("Updated list:", grades)
        else:
         print("No grades entered.")

# -----------------------------------------
# Removing a random grade
        print("\n--- Removing a random grade ---")
        if grades:
         random_grade = random.choice(grades)
         grades.remove(random_grade)
         print("Random grade removed:", random_grade)
         print("Updated list:", grades)
        else:
         print("No grades left to remove.")

# -----------------------------------------
# Editing a grade
    print("\n--- Editing a grade ---")
    if grades:
     for i, g in enumerate(grades, start=1):
        print(f"{i}. {g}")

    while True:
        try:
            choice = int(input("Enter the number of the grade you would like to edit: "))
            if 1 <= choice <= len(grades):
                new_grade = int(input("Enter the new grade: "))
                grades[choice - 1] = new_grade
                break
            else:
                print("Error: Invalid grade index.")
        except ValueError:
            print("Please enter a valid number.")

            print("Updated list:", grades)
        else:
            print("No grades to edit.")

# -----------------------------------------
# Sorting and reversing the list
    print("\n--- Sorting and Reversing Grades ---")
    grades.sort()
    print("Sorted grades:", grades)
    grades.reverse()
    print("Reversed grades:", grades)

# -----------------------------------------
# Total and average
    print("\n--- Grade Total and Average ---")
    if grades:
        total = sum(grades)
        average = total / len(grades)
        print("Total of grades:", total)
        print("Average grade:", round(average, 2))
    else:
        print("No grades to calculate total or average.")

# -----------------------------------------
# Completion message
print("\nCompleted by, [Isaac Davis]")


# Run the main function
if __name__ == "__main__":
    main()