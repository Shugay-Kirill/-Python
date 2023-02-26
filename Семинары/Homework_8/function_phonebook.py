from copy import deepcopy

class Phone_book():
    # file_directory = "dictionary.txt"
    phone_book = []
    new_phone_book = []
    def __init__(self, file_directory):
        self.file_directory = file_directory
        
        with open(file_directory, "r", encoding="UTF-8") as file:
            data = file.readlines()
            for contact in data:
                record = contact.strip().split(";")
                record_contact = {}
                record_contact["name"] = record[0]
                record_contact["phone"] = record[1]
                record_contact["comment"] = record[2]
                self.phone_book.append(record_contact)
            self.new_phone_book = deepcopy(self.phone_book)
        
                
    def save_file_phonebook(self):
        # global phone_book
        # global file_directory
        # global new_phone_book
        data = []
        for contact in self.phone_book:
            data.append(";".join(contact.values()))
        data = "\n".join(data)
        with open(self.file_directory, "w", encoding="UTF-8") as file:
            file.write(data)
        self.new_phone_book = deepcopy(self.phone_book)
            
    def get(self):
        # global phone_book
        return self.phone_book

    def add_contact(self,new_contact: dict):
        # global phone_book
        self.phone_book.append(new_contact)
        
    def change_contact(self, id_user: int, contact):
        # global phone_book
        self.phone_book.pop(id_user-1)
        self.phone_book.insert(id_user-1, contact)
        
    def find(self, find_contact: str):
        # global phone_book
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_contact.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def get_name(self, id_user: int):
        # global phone_book
        return self.phone_book[id_user-1].get("name")

    def delete_contact(self, id_user):
        # global phone_book
        self.phone_book.pop(id_user-1)

    def check_changes(self):
        # global phone_book
        # global new_phone_book
        if self.phone_book != self.new_phone_book:
            return True
        return False

    def check_open_file(self):
        # global phone_book
        if self.phone_book != []:
            return True
        return False