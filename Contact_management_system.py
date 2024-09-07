#Function to chect whether the name is alphabetic or not
def is_valid_name(name):
    return name.isalpha()

#Function to check phone number contains only digits and length of phone no should be 10
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

#Function to add contacts 
def add_contacts(contacts):
    name = input("Enter contact name:").strip()

    if not name or not is_valid_name(name):
        print("Enter valid name.Name contain only alphabetes").strip()
    elif name in contacts:
        print("Name already present in contact")

        return
    phone = input("Enter contact number:").strip()

    if not phone or not is_valid_phone(phone):
        print("Enter valid contact number and length of contact number must be 10 digit:").strip()
        return
    contacts[name]= {'name':name,'phone': phone}
    print(f"Contact {name} added successfully.")

#Function to search contacts  
def search_contacts(contacts):
    name=input("Enter  contact name to search:").strip()
    print("-" * 30)  # Separator for better readability
    contact=contacts.get(name)
    
    if contact :
        print("Name:",contact['name'])
        print("Phone:",contact['phone'])
    else:
        print("Contact not found")

#Function to update contacts
def update_contacts(contacts):
    name=input("Enter contact name to update:").strip()
    if not name or not is_valid_name(name):
        print("Enter valid contact name:").strip()
        return
    if name not in contacts:
        print("Contact not found to update")

    phone=input("Enter new phone number to update").strip()
    contacts[name]={'name':name,'phone':phone}
    print("Contact updated successfully")

#Function to view contacts    
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("-" * 30)  # Separator for better readability
    print("Printing contacts...")
    
    for name,info in contacts.items():
      
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print("-" * 30)  # Separator for better readability
      
    

def main():
    contacts={}


    while True:
        print(" ********** Contact Management System **********")  
        print("1.Add new contact")
        print("2.Search contact")
        print("3.Update contact")
        print("4.Print all contacts")
        print("5.Quit")
        choice=input("Enter your choice:")
        if choice=="1":
            add_contacts(contacts)
        elif choice=="2":
            search_contacts(contacts)
        elif choice=="3":
            update_contacts(contacts)
        elif choice=="4":
            view_contacts(contacts) 
        elif choice=="5":
            print()
            print("Goodbye")
        else:
            print("Invalid choice")
if __name__ =="__main__":
    main()

    
        
