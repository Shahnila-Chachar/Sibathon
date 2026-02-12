contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Count Contacts")
    print("6. Delete Contact")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added.")
    
    elif choice == '2':
        if contacts:
            print("\nContacts List:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    
    elif choice == '3':
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"Contact {name} not found.")
    
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")
    
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")