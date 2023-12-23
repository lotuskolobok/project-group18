from collections import UserDict
from datetime import date, datetime
import json
from pathlib import Path
import re
import copy
import os


FILE_NAME = "addressbook.bin"
SERIALIZATION_PATH = Path(FILE_NAME)


class Record:
    def __init__(self, name, phone=None, address=None, email=None, birthday=None):
        self.name = name
        self.phones = []
        if phone and phone.value != None:
            self.add_phone(phone)
        self.address = address
        self.email = email
        if isinstance(birthday, Birthday):
            self.birthday = birthday
        else:
            self.birthday = None

    def __str__(self):
        return f"Name: {self.name.value} Phone: {self.phones} Address: {self.address.value} Email: {self.email.value} Birthday: {self.birthday}"

    def __repr__(self):
        return f"Name: {self.name.value} Phone: {self.phones} Address: {self.address.value} Email: {self.email.value} Birthday: {self.birthday}"

    def add_phone(self, phone):
        self.phones.append(phone)

    def add_birthday(self, birthday):
        if isinstance(birthday, Birthday):
            self.birthday = birthday
        else:
            self.birthday = Birthday(birthday)

    def change_phone(self, phone):
        self.phones = phone

    def delete_phone(self):
        self.phones = []

    def show_contact(self):
        return {"name": self.name.value,
                "phone": [phone.value for phone in self.phones] if self.phones else [],
                "birthday": self.birthday.value if self.birthday else self.birthday}

    def days_to_birthday(self):
        birthday = datetime(year=int(datetime.now().year),
                            month=int(self.birthday.value[3:5]), day=int(self.birthday.value[:2])).date()
        time_now = datetime.now().date()
        delta = birthday - time_now
        if int(delta.days) >= 0:
            return delta.days
        else:
            birthday = datetime(year=int(datetime.now().year)+1,
                                month=int(self.birthday.value[3:5]), day=int(self.birthday.value[:2])).date()
            delta = birthday - time_now
            return delta.days


class Field:

    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Address(Field):
    pass


class Email(Field):
    def __init__(self, email):
        self.__value = None
        self.value = email

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)

    def check_email(self, email):
        result = re.match(
            r'^[\w]{1,}([\w.+-]{0,1}[\w]{1,}){0,}@[\w]{1,}([\w-]{0,1}[\w]{1,}){0,}([.][a-zA-Z]{2,}|[.][\w-]{2,}[.][a-zA-Z]{2,})$', email)
        if result:
            return email
        else:
            return None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_email):
        if new_email == None:
            self.__value = None
        elif self.check_email(new_email):
            self.__value = self.check_email(new_email)


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, phone):
        self.__value = None
        self.value = phone

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)

    def check_phone(self, phone):
        phone_number = (str(phone).strip()
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
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_phone):
        if self.check_phone(new_phone):
            self.__value = self.check_phone(new_phone)


class Birthday(Field):

    def __init__(self, birthday):
        self.__value = None
        self.value = birthday

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_birthday):
        if new_birthday == None:
            self.__value = None
        elif self.check_birthday(new_birthday):
            self.__value = self.check_birthday(new_birthday)

    def check_birthday(self, birthday):
        try:
            year = int(birthday[6:])
            month = int(birthday[3:5])
            day = int(birthday[:2])
            test_date = date(year, month, day)
            delta = datetime.now().date() - test_date
            if len(str(year)) < 4:
                raise ValueError
            if delta.days < 0:
                raise TypeError
        except TypeError:
            print("No one can be born in the future :)")
        except ValueError:
            print("Wrong date, should be - dd.mm.yyyy, only numbers")
        else:
            return birthday


class NoteName:

    def __init__(self, value):
        if len(value) < 30:
            self.value = value
        else:
            self.value = value[:30]

    def __repr__(self):
        return f'{self.value}'


class Status:

    def __init__(self, value="in progress"):
        self.value = "in progress"

    def __repr__(self):
        return f'{self.value}'


class Notes:

    def __init__(self, value):
        if len(value) < 250:
            self.value = value
        else:
            self.value = value[:250]


class Tags:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class RecordNote:
    def __init__(self, name, note: Notes, tag: Tags = None, status="in progress"):
        self.name = name
        self.note = note
        self.tags = []
        if tag:
            self.tags.append(tag)
        self.status = Status(status)

    def __str__(self):
        return f"Name: {self.name.value} Note: {self.note.value} Tags: {self.tags} Status: {self.status.value}"

    def __repr__(self):
        return f"Name: {self.name.value} Note: {self.note.value} Tags: {self.tags} Status: {self.status.value}"


class NoteBook(UserDict):
    def __init__(self):
        self.data = {}

    def __repr__(self):
        return f'{self.data}'

    def add_note(self, record):
        self.data[record.name.value] = record

    def change_name(self, old_name, new_name):
        self.data[new_name] = copy.deepcopy(self.data[old_name])
        self.data[new_name].name.value = new_name
        self.data.pop(old_name)

    def change_tag(self, name, tags):
        new_tag = Tags(tags)
        for k, v in self.data.items():
            if k == name:
                self.data[k].tags = []
                self.data[k].tags.append(new_tag)

    def change_note(self, name, new_note):
        new_note = Notes(new_note)
        for k in self.data:
            if k == name:
                self.data[k].note = new_note

    def change_status(self, name, new_status):
        if new_status.lower() in ["in progress", "done"]:
            self.data[name].status.value = new_status.lower()

    def show_record(self, name):
        if name in self.data.keys():
            return self.data[name]

    def show_note(self, name):
        for k in self.data:
            if k == name:
                return self.data[k]

    def delete_note(self, rec: RecordNote):
        for a, v in self.data.items():
            if v.note == rec.note:
                deleted_note = a.note
                self.data.pop(a)
                return deleted_note

    def delete_notes_by_status(self, status):
        result = {}
        for name, record in self.data.items():
            if record.status.value != status:
                result[name] = record
        self.data = result

    def delete_tag(self, name, del_tag):
        old_tags = self.data[name].tags
        new_tags = [tag for tag in old_tags if tag.value != del_tag]
        self.data[name].tags = new_tags

    def add_tag(self, name, new_tag):
        if new_tag.value not in [i.value for i in self.data[name].tags]:
            self.data[name].tags.append(new_tag)

    def find_info_by_name(self, keyword):
        result = []
        for name, record in self.data.items():
            if keyword.lower() == name.lower():
                result.append(self.data[name])
                break
        return result

    def find_info_by_tag(self, keyword):
        result = []
        for name, record in self.data.items():
            for tag in record.tags:
                if keyword.lower() == tag.value.lower():
                    result.append(self.data[name])
                    break
        return result

    def find_info_by_status(self, keyword):
        result = []
        for name, record in self.data.items():
            if keyword.lower() == record.status.value.lower():
                result.append(self.data[name])
        return result

    def get_tags(self, name):
        return self.data[name].tags

    def change_tag(self, name, old_tag, new_tag):
        for i in range(len(self.data[name].tags)):
            if old_tag.value == self.data[name].tags[i].value:
                self.data[name].tags[i].value = new_tag.value

    def serialize(self, file_name="notebook.bin"):
        with open(file_name, 'wb') as file:
            json.dump(self.data, file)

    def deserialize(self, file_name="notebook.bin"):
        with open(file_name, 'rb') as file:
            self.data = json.load(file)

    def show_records(self):
        return self.data
    
    # def get_notes(self):
    #     return self.notes
