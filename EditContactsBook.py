class ContactsBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, info, birthday=None):
        self.contacts[name] = {'info': info, 'birthday': birthday}
        print(f"Contact {name} successfully added.")

    def edit_contact(self, name, new_info=None, new_birthday=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_info is not None:
                contact['info'] = new_info
            if new_birthday is not None:
                contact['birthday'] = new_birthday
            print(f"Information for contact {name} successfully edited.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} successfully deleted.")
        else:
            print(f"Contact {name} not found.")

    def show_contacts(self):
        print("Contacts:")
        for name, data in self.contacts.items():
            info = data['info']
            birthday = data['birthday']
            print(f"{name}: {info}, Birthday: {birthday if birthday else 'Not specified'}")