contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("\n===== ALL CONTACTS =====")

        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")