# Simple Contact Manager using a CSV file
# This program uses only basic Python features: functions, lists, file I/O, and strings.

CONTACTS_FILE = "contacts.csv"


def create_contacts_file():
    """Create a new CSV file with a header row."""
    # "w" mode creates/overwrites the file.
    # newline="" helps avoid blank lines in some systems.
    with open(CONTACTS_FILE, "w", newline="") as file:
        file.write("Name,Phone,Email\n")
    print("Contact file created successfully.")


def add_contact():
    """Append a new contact to the CSV file."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()

    # Make sure the file exists and has a header before appending.
    try:
        # Try reading to confirm the file exists
        with open(CONTACTS_FILE, "r") as file:
            pass
    except FileNotFoundError:
        print("Contact file does not exist yet. Please create the file first (option 1).")
        return

    # Append the new contact
    with open(CONTACTS_FILE, "a", newline="") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully.")


def view_contacts():
    """Read and display all contacts from the CSV file."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Contact file not found. Please create it first (option 1).")
        return

    if len(lines) <= 1:
        print("No contacts found in the file.")
        return

    # lines[0] is the header: Name,Phone,Email
    print("\nContacts in file:")
    print("-" * 70)
    # Basic formatting using str.format for simple columns
    print("{:<4} {:<20} {:<15} {:<30}".format("No.", "Name", "Phone", "Email"))
    print("-" * 70)

    for index, line in enumerate(lines[1:], start=1):
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        if len(parts) != 3:
            continue  # skip any malformed rows
        name, phone, email = parts
        print("{:<4} {:<20} {:<15} {:<30}".format(index, name, phone, email))

    print("-" * 70)


def edit_contact():
    """Edit an existing contact's phone and email."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Contact file not found. Please create it first (option 1).")
        return

    if len(lines) <= 1:
        print("There are no contacts to edit.")
        return

    # Save contacts into a list (array) for editing
    header = lines[0].strip()
    contacts = []

    for line in lines[1:]:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        if len(parts) == 3:
            contacts.append(parts)  # [name, phone, email]

    if len(contacts) == 0:
        print("There are no valid contacts to edit.")
        return

    # Show existing contacts before asking which to edit
    print("\nExisting contacts:")
    print("-" * 70)
    print("{:<4} {:<20} {:<15} {:<30}".format("No.", "Name", "Phone", "Email"))
    print("-" * 70)
    for index, contact in enumerate(contacts, start=1):
        name, phone, email = contact
        print("{:<4} {:<20} {:<15} {:<30}".format(index, name, phone, email))
    print("-" * 70)

    # Ask user which contact number to edit
    choice = input("Enter the number of the contact you want to edit: ").strip()

    if not choice.isdigit():
        print("Contact not found (invalid number).")
        return

    contact_index = int(choice) - 1

    if contact_index < 0 or contact_index >= len(contacts):
        print("Contact not found (number out of range).")
        return

    # Get the new values
    selected_contact = contacts[contact_index]
    name = selected_contact[0]  # keep the same name

    print(f"Editing contact: {name}")
    new_phone = input("Enter new phone number: ").strip()
    new_email = input("Enter new email: ").strip()

    # Update the contact data in the list
    contacts[contact_index][1] = new_phone
    contacts[contact_index][2] = new_email

    # Write all contacts back to the file (including header)
    with open(CONTACTS_FILE, "w", newline="") as file:
        file.write(header + "\n")
        for contact in contacts:
            file.write(",".join(contact) + "\n")

    print("Contact updated successfully.")


def main():
    print("Welcome to the Contact Manager Program.")
    print("This program manages a simple list of contacts stored in a CSV file.")

    while True:
        print("\nMenu:")
        print("1 - Create a new contact CSV file")
        print("2 - Add a new contact to the CSV file")
        print("3 - View all contacts in the file")
        print("4 - Modify an existing contact in the file")
        print("5 - Exit the program")

        choice = input("Please enter your choice (1-5): ").strip()

        if choice == "1":
            create_contacts_file()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            # End of the program
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option selected. Please try again.")

    
    print("Completed by, Isaac Davis")


if __name__ == "__main__":
    main()
