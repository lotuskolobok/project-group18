def search_contact(self, search_item):
        results = [contact for contact in self.data if search_item in contact['name'] or search_item in contact['phone'] or search_item in contact['email']]
        return results