
class ContactManager():
    
    contacts = []
    
    def add_contact(self):
        name = input("Please Enter name: ").strip()
        email = input("Please Enter email: ").strip()
        phone = input("Please Enter phone number: ").strip()
        address = input("Please Enter address: ").strip()
        
        new_contact = {'name':name, 'email':email, 'phone':phone, 'address':address}
        
        self.contacts.append(new_contact)
        print(self.contacts)
        
    
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
            