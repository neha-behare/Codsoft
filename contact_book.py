contacts = {}

def display_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    print("Name\t\tPhone Number\t\tEmail\t\t\tAddress")
    print("-" * 80)
    for name, details in contacts.items():
        print(f"{name}\t\t{details['phone']}\t\t{details['email']}\t\t{details['address']}")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter contact name: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contacts[name] = {"phone": phone, "email": email, "address": address}
            print("Contact added successfully.")

    elif choice == 2:
        display_contacts()

    elif choice == 3:
        search_name = input("Enter the name to search: ")
        if search_name in contacts:
            print("\nContact found:")
            print(f"Name: {search_name}")
            print(f"Phone: {contacts[search_name]['phone']}")
            print(f"Email: {contacts[search_name]['email']}")
            print(f"Address: {contacts[search_name]['address']}")
        else:
            print("Contact not found.")

    elif choice == 4:
        update_name = input("Enter the name of the contact to update: ")
        if update_name in contacts:
            print("Enter new details (leave blank to keep old value):")
            phone = input(f"Phone [{contacts[update_name]['phone']}]: ") or contacts[update_name]['phone']
            email = input(f"Email [{contacts[update_name]['email']}]: ") or contacts[update_name]['email']
            address = input(f"Address [{contacts[update_name]['address']}]: ") or contacts[update_name]['address']
            contacts[update_name] = {"phone": phone, "email": email, "address": address}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        delete_name = input("Enter the contact name to delete: ")
        if delete_name in contacts:
            confirm = input(f"Are you sure you want to delete {delete_name}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(delete_name)
                print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
