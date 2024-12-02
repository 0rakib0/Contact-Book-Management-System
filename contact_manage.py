from validation import check_valid_name, check_number, check_email

class ContactManager():
    
    contacts = []
    
    def add_contact(self):
        name = input("Please Enter name: ").strip()
        email = input("Please Enter email: ").strip()
        phone = input("Please Enter phone number: ").strip()
        address = input("Please Enter address: ").strip()
        
        # check validation of email
        if not check_email(email):
            print("Please Enter a valid email.")
            return
        # check validation of phone number
        elif not check_number(phone):
            print("Phone number can't contain string.")
            return
        # check validation of name
        elif not check_valid_name(name):
            print("Name only can contain string.")
            return
        
        # check have duplicat number or not
        for i in self.contacts:
            if (i['phone']) == phone:
                print("Phone number already exist. Please try with another number!")
                return
            
        

        new_contact = {'name':name, 'email':email, 'phone':phone, 'address':address}
        self.contacts.append(new_contact)
        
        print("New Contact successfully added to the contact book!")
        
    
    def contact_view(self):
        if not self.contacts:
            print("No contact available in your contact list")
            return
        print("\n--- Contact List ---")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
            
            
    def search_contact(self):
        query = input("Enter name, email, or phone to search: ").strip()
        for contact in self.contacts:
            result = query.lower() in str(contact).lower()
            if result:
                print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
            else:
                print("No contact number found...")
                break

    def delete_contact(self):
        query = input("Enter name, email, or phone to search: ").strip()
        for index, contact in enumerate(self.contacts):
            if query.lower() in str(contact).lower():
                self.contacts.pop(index)
                print("Contact Successfully removed!")
                return index
            print("No contact found!")
            