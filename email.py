import re


class Email:
    def __init__(self, value=''):
        self.values = []
        if value:
            self.value = value
        else:
            self.value = input('Enter email: ')
        self.validate_email()
        
    def validate_email(self):
        try:
            if re.match(r'^[\w]{1,}([\w.+-]{0,1}[\w]{1,}){0,}@[\w]{1,}([\w-]{0,1}[\w]{1,}){0,}([.][a-zA-Z]{2,}|[.][\w-]{2,}[.][a-zA-Z]{2,})$', self.value):
                self.values.append(self.value)
            else:
                raise ValueError
        except ValueError:
            print('Invalid email! Please enter correct email')