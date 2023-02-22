from copy import deepcopy


phone_book = []
new_phone_book = []
file_directory = "dictionary.txt"

def open_phonebook():
    global phone_book
    global file_directory
    global new_phone_book
    with open(file_directory, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for contact in data:
            record = contact.strip().split(";")
            record_contact = {}
            record_contact["name"] = record[0]
            record_contact["phone"] = record[1]
            record_contact["comment"] = record[2]
            phone_book.append(record_contact)
        new_phone_book = deepcopy(phone_book)
    
            
def save_file_phonebook():
    global phone_book
    global file_directory
    global new_phone_book
    data = []
    for contact in phone_book:
        data.append(";".join(contact.values()))
    data = "\n".join(data)
    with open(file_directory, "w", encoding="UTF-8") as file:
        file.write(data)
    new_phone_book = deepcopy(phone_book)
        
def get():
    global phone_book
    return phone_book

def add_contact(new_contact: dict):
    global phone_book
    phone_book.append(new_contact)
    
def change_contact(id_user: int, contact):
    global phone_book
    phone_book.pop(id_user-1)
    phone_book.insert(id_user-1, contact)
    
def find(find_contact: str):
    global phone_book
    all_find = []
    for contact in phone_book:
        for element in contact.values():
            if find_contact.lower() in element.lower():
                all_find.append(contact)
    return all_find

def get_name(id_user: int):
    global phone_book
    return phone_book[id_user-1].get("name")

def delete_contact(id_user):
    global phone_book
    phone_book.pop(id_user-1)

def check_changes():
    global phone_book
    global new_phone_book
    if phone_book != new_phone_book:
        return True
    return False

def check_open_file():
    global phone_book
    if phone_book != []:
        return True
    return False