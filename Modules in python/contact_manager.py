def add_contact(contacts, name, phone, email):
    contacts.append({'name': name, 'phone': phone, 'email': email})

def view_contact(contacts, name, phone, email):
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(contacts, name, phone, email):
    for contact in contacts:
        if contact['name'].lower == name.lower():
            return contact
    return None

def delete_contact(contacts, name, phone, email):
    for i, contact in enumerate(contacts):
        if contact['name'].lower == name.lower():
            return contacts.pop(i)
        
    return None 