from collections import UserDict
from datetime import datetime
from datetime import date

class Field:
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__value)

    # додали getter для атрибутів value спадкоємців Field.
    @property
    def value(self):
        return self.__value

    # додали setter для атрибутів value спадкоємців Field.
    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass

class Mail(Field):
    pass

class Address(Field):
    pass

class Phone(Field):

    def __str__(self):
        return self.value

    # додали getter для атрибуту value
    @property
    def value(self):
        return self._Field__value

    # додали setter для атрибуту value
    @value.setter
    def value(self, value):
        self._Field__value = self.validate(value)

    def validate(self, value):

        if len(value) == 10 and value.isdigit():
            return value
        else:
            raise ValueError('Phone should be 10 digits')


# додали клас Birthday, який наслідуємо від класу Field
class Birthday(Field):

    # додали getter для атрибуту value
    @property
    def value(self):
        return self._Field__value

    # додали setter для атрибуту value
    @value.setter
    def value(self, value):
        self._Field__value = self.validate(value)


class Record:
    def __init__(self, name, birthday=None, mail=None, address=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)
        self.mail = Mail(mail)
        self.address = Address(address)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    # додали метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий
    def days_to_birthday(self):

        if self.birthday.value is None:
            delta_days = None

        else:
            try:
                this_date = date.today()
                birthday_date = date.fromisoformat(str(self.birthday.value))
                birthday_date = datetime(
                    year=this_date.year, month=birthday_date.month, day=birthday_date.day).date()

                delta_days = (birthday_date - this_date).days

                if delta_days < 0:
                    birthday_date = datetime(
                        year=this_date.year + 1, month=birthday_date.month, day=birthday_date.day).date()

                    delta_days = (birthday_date - this_date).days
            except:
                delta_days = None

        return delta_days


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record