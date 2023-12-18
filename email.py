import re

class Email(Field):
    def __str__(self):
        return self.value
    
    @property
    def email_value(self):
        return self._Field__value

    @email_value.setter
    def email_value(self, value):
        self._Field__value = self.validate_email(value)
        
    def validate_email(self, value):
        if re.match(r'^[\w]{1,}([\w.+-]{0,1}[\w]{1,}){0,}@[\w]{1,}([\w-]{0,1}[\w]{1,}){0,}([.][a-zA-Z]{2,}|[.][\w-]{2,}[.][a-zA-Z]{2,})$', self.value):
            return value
        else:
            raise ValueError('Invalid email address! Please enter correct email')