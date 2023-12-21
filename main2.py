from collections import UserDict
from datetime import datetime
from datetime import date

import cmd
import pickle
import re

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


class Phone():
    def __init__(self, value) -> None:
        p = self.validate(value)
        if p != None:
            self.__value = value

    def __str__(self):
        return self.__value

    # додали getter для атрибуту value
    @property
    def value(self):
        return self.__value

    # додали setter для атрибуту value
    @value.setter
    def value(self, value):
        p = self.validate(value)
        if p != None:
            self.__value = p

    def validate(self, value):

        phone_number = (value.strip()
                        .replace('(', '')
                        .replace(')', '')
                        .replace('-', '')
                        .replace(' ', '')
                        .replace('+', ''))

        if len(phone_number) == 13:
            if re.match('^\\+38\d{10}$', phone_number):
                return phone_number
        elif len(phone_number) == 12:
            if re.match('^\d{12}$', phone_number):
                phone_number = '+' + phone_number
                return phone_number
        elif len(phone_number) == 10:
            if re.match('^\d{10}$', phone_number):
                phone_number = '+38' + phone_number
                return phone_number
        else:
            phone_number = None

        return phone_number


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

    # додели метод для перевірки правильності вказаної дати
    def validate(self, value):
        if value == None:
            return None

        try:
            datetime.strptime(value, '%Y-%m-%d')
            return value

        except ValueError:
            return None

# додали необов'язковий параметр birthday


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    # додали метод, який повертає значення параметра birthday
    def show_birthday(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday.value}"

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

    def add_phone(self, phone_number: str):
        p = Phone(phone_number)
        if p:
            self.phones.append(p)

    def find_phone(self, phone_number: str):
        result = False
        for phone in self.phones:
            if phone.value == phone_number:
                result = True
                return phone

        if result == False:
            return None

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = new_phone
        else:
            raise ValueError

    def remove_phone(self, rem_phone):
        for phone in self.phones:
            if phone.value == rem_phone:
                self.phones.remove(phone)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    # пошук записів за збігом в імені або номері телефона
    def find_record(self, part: str):
        finded = {}

        for item, record in self.items():
            # пошук в номері телефона
            for p in record.phones:
                if part in str(p):
                    finded[item] = self.data[item]

            # пошук в імені
            if part.lower() in item.lower():
                finded[item] = self.data[item]

        return finded

    # додали ітератор
    def iterator(self, N):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}\n'
            counter += 1
            if counter >= N:
                yield result
                counter = 0
                result = ''

    # додали метод для сериалізації адресної книги та запису її у файл
    def dump(self):
        with open(self.file, 'wb') as file:
            pickle.dump((self.record_id, self.record), file)

    # додали метод для десериалізації адресної книги з файла
    def load(self):
        if not self.file.exists():
            return False
        with open(self.file, 'rb') as file:
            self.record_id, self.record = pickle.load(file)


# клас для сериалізації адресної книги при виході з програми
class Controller(cmd.Cmd):
    def exit(self):
        self.book.dump()
        return True

# ----------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John", "2000-10-05")
    john_record.add_phone("1234567890")
    john_record.add_phone("555555555p")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane", "2001-02-20")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Створення та додавання нового запису для Sara
    sara_record = Record("Sara")
    sara_record.add_phone("5566997711")
    book.add_record(sara_record)
    sara_record.birthday = Birthday("1976-07-14")

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    f = '9'
    print(f'-----Пошук за [{f}]--------')
    f = book.find_record(str(f))
    for name, record in f.items():
        print(record)
    print('-' * 30)

    # Виведення дати народження та кількості днів до дати народження
    print(jane_record.show_birthday(), jane_record.days_to_birthday())
    print(john_record.show_birthday(), john_record.days_to_birthday())
    print(sara_record.show_birthday(), sara_record.days_to_birthday())

    # Видалення запису Jane
    book.delete("Jane")
