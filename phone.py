import re

class Phone(Field):
    def __str__(self):
        return self.value
    
    @property
    def value(self):
        return self._Field__value

    @value.setter
    def value(self, value):
        self._Field__value = self.validate_phone(value)

    def validate_phone(self, value):
        phone_number = (value.strip()
                        .replace('(', '')
                        .replace(')', '')
                        .replace('-', '')
                        .replace(' ', '')
                        .replace('+', ''))
        if len(phone_number)== 13:
            if re.match('^\\+38\d{10}$', phone_number):
                return phone_number
        elif len(phone_number) == 12:
            if re.match('^\d{12}$', phone_number):
                return '+' + phone_number
        elif len(phone_number) == 10:
            if re.match('^\d{10}$', phone_number):
                return '+38' + phone_number
        raise ValueError('Invalid phone number! Please enter correct number phone!')