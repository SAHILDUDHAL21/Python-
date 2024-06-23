#	CodSoft Internship (Python Programming)
#	Task 5

contacts = []

def add(name, phone, email, address):
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added")

def view():
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print_contact(contact)
    else:
        print("Contact list is empty.")

def searchc(name):
    f = False
    for contact in contacts:
        if contact["name"] == name:
            f = True
            print_contact(contact)
    if not f:
        print("Contact not found.")

def update(name, phone=None, email=None, address=None):
    for contact in contacts:
        if contact["name"] == name:
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address
            print("Contact updated")
            print_contact(contact)
            return
    print("Contact not found.")

def delete(name):
    global contacts
    contacts = [contact for contact in contacts if contact["name"] != name]
    print("Contact deleted")

def print_contact(contact):
    print("Name:	",contact['name'])
    print("Phone:	",contact['phone'])
    print("Email:	",contact['email'])
    print("Address: ",contact['address'])
    

while True:
    print("\n1 :: Add Contact")
    print("2 :: View List")
    print("3 :: Search Contact")
    print("4 :: Update Contact")
    print("5 :: Delete Contact")
    print("6 :: Exit ...\n")

    choice = int(input("Enter your choice :: "))
    print("\n")

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add(name, phone, email, address)
    elif choice == 2:
        view()
    elif choice == 3:
        name = input("Enter name to search: ")
        searchc(name)
    elif choice == 4:
        name = input("Enter name to update: ")
        phone = input("Enter new phone number (leave Empty to keep current): ")
        email = input("Enter new email (leave Empty to keep current): ")
        address = input("Enter new address (leave Empty to keep current): ")
        update(name, phone, email, address)
    elif choice == 5:
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == 6:
        print("exiting.............................")
        break
    else:
        print("Invalid choice. Please try again.")