# String Replacement Tool
# Uses: input, print, .find(), .replace(), .lower(), loops, and basic string operations

def main():
    # Purpose of the program
    print("Welcome to the String Replacement Tool!")
    print("---------------------------------------")
    print("This program will search for a substring inside a main string")
    print("and can replace it with new text if you choose.\n")

    # Get main string and substring from the user
    main_string = get_string_input("Enter the string to search through: ")
    sub_string = get_string_input("Enter the string to search for: ")

    # Use .find() to locate the substring in the main string
    index = find_substring(main_string, sub_string)

    # Only ask about replacement if the substring was found
    if index != -1:
        wants_replace = ask_yes_no(
            "Do you want to replace '" + sub_string + "' with something else (y/n)? "
        )

        if wants_replace:
            # Ask for the new replacement string
            replacement = get_string_input("Enter the replacement string: ")

            # Use .replace(old, new, 1) to replace only the first occurrence
            new_string = replace_first_occurrence(main_string, sub_string, replacement)

            print("New String:", new_string)
        else:
            print("No replacement was made.")

    # End of program message
    print("\nThank you for using our program!")


def get_string_input(prompt):
    # Ask the user for a string and return it
    user_input = input(prompt)
    return user_input


def find_substring(main_string, sub_string):
    # Demonstrates the .find() method from the overview
    print("\nSearching for substring within the main string content, please wait!")
    print("--------------------------------------------------------------------")

    index = main_string.find(sub_string)  # returns starting index or -1

    if index != -1:
        print("'" + sub_string + "' was found in the main string at index", index)
    else:
        print("'" + sub_string + "' was NOT found in the main string.")
        index = -1

    return index


def ask_yes_no(prompt):
    # Ask for a yes/no answer, re-prompting on invalid input
    while True:
        answer = input(prompt)
        answer = answer.lower()  # uses .lower() from the overview

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid entry. Please enter 'y' for yes or 'n' for no.")


def replace_first_occurrence(main_string, sub_string, replacement):
    # Uses the .replace(old, new, num) method from the overview
    print("\nInitiating the string replacement process!")
    print("------------------------------------------")

    new_string = main_string.replace(sub_string, replacement, 1)
    return new_string


# Start the program
main()

# --- Completion message ---
print("Completed by, [Isaac Davis]")  
