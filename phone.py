import re

class Phone:
    def __init__(self, value=''):
        self.values = []
        if value:
            self.value = value
        else:
            self.value = input('Enter phone: ')
        self.validate_phone()

    def validate_phone(self):
        try:
            phone_number = (self.value.strip()
                        .replace('(', '')
                        .replace(')', '')
                        .replace('-', '')
                        .replace(' ', ''))
            if len(phone_number)== 13:
                if re.match('^\\+38\d{10}$', phone_number):
                    self.values.append(phone_number)
            elif len(phone_number) == 12:
                if re.match('^\d{12}$', phone_number):
                    self.values.append('+' + phone_number)
            elif len(phone_number) == 10:
                if re.match('^\d{10}$', phone_number):
                    self.values.append('+38' + phone_number)
            else:
                raise ValueError
        except ValueError:
            print('Invalid phone number! Please enter correct number phone!')