contacts = {}

def add_contacts():
    name = input("Enter name: ")
    if name in contacts:
        print ("Contact already exists.\n")
        return
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone":phone,"Email":email,"Address":address}
    print("Contact added successfully.\n")

def view_contacts():
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['Phone']}")
        print(f"  Email: {info['Email']}")
        print(f"  Address: {info['Address']}")
        print("-------------------------")
    print()
    if not contacts:
        print("No contacts found.\n")
        return

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info['Phone']:
            print(f"Found: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            print()
            found = True
    if not found:
        print("No matching contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.\n")
        return
    phone = input(f"Enter new phone ({contacts[name]['Phone']}): ") or contacts[name]['Phone']
    email = input(f"Enter new email ({contacts[name]['Email']}): ") or contacts[name]['Email']
    address = input(f"Enter new address ({contacts[name]['Address']}): ") or contacts[name]['Address']
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact updated successfully.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("------Contact Book------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
    

