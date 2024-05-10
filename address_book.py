'''
Address book module for managing user phones
'''

from collections import UserDict
import re

class AddressBookException(Exception):
    '''
    Custom error class
    '''

class Field:
    '''
    Generic class for address book data
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, value) -> bool:
        return self.value == value.value

    def __hash__(self) -> int:
        return self.value.__hash__()

class Name(Field):
    '''
    Name field declaration
    '''

class Phone(Field):
    '''
    Phone field declaration with validations
    '''
    def __init__(self, phone):
        if re.match(r"^\d{10}$", phone):
            super().__init__(phone)
        else:
            raise AddressBookException("Phone should consist of 10 numbers.")

class Record:
    '''
    Address record composite
    '''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = {}

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

    def add_phone(self, phone: str):
        self.phones[Phone(phone)] = True

    def remove_phone(self, phone: str):
        self.find_phone(phone)
        del self.phones[Phone(phone)]

    def edit_phone(self, old_phone: str, phone: str):
        self.find_phone(old_phone)
        self.remove_phone(old_phone)
        self.add_phone(phone)
    
    def find_phone(self, phone: str):
        if self.phones.get(Phone(phone)) is not None:
            return phone
        raise AddressBookException(f"The phone {phone} is not present")

class AddressBook(UserDict):
    '''
    Main Address book class
    '''
    def add_record(self, record: Record):
        self[str(record.name)] = record

    def find(self, name: str):
        if self.get(name) is not None:
            return self[name]
        raise AddressBookException(f"The name {name} is not present in the address book")

    def delete(self, name: str):
        self.find(name)
        del self[name]
