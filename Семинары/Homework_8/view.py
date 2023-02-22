
def menu():
    print("""\nГлавное меню
          1. Открыть файл
          2. Сохранить файл
          3. Показать контакт
          4. Создать контакт
          5. Изменить контакт 
          6. Найти контакт
          7. Удалить контакт
          8. Выход""")
    while True:
        try:
            choice_function = int(input("Выберите пунет меню: "))
            if 0 < choice_function < 9:
                return choice_function
            else:
                print("\nВведите цифру от 1 до 8")
        except:
            print("\nВведите цирфу функции")
            
def print_phonebook(phone_book: list[dict]):
    if phone_book == []:
        print("\nСправочник пустой или не открыт")
    else:
        for i, contact in enumerate(phone_book, 1):
            name = contact.get("name")
            phone = contact.get("phone")
            comment = contact.get("comment")
            print(f"{i}. {name:30} {phone:<15} {comment:<20}")
            
def input_new_contact():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    new_contact = {"name": name,
                   "phone": phone,
                   "comment": comment}
    return new_contact

def input_id_user():
    id_user = int(input("\nВведите номер(ID) контакта для изменения: "))
    return id_user

def find_contact():
    find_contact = input("\nВведите, что надо найти: ")
    return find_contact

def confirm(condition: str, name: str):
    confirmation_answer =  input(f"\nВы действительно хотите {condition} конетакт {name}? (y/n): ")
    if confirmation_answer == "y":
        return True
    else:
        return False
    
def confirm_changes():
    answer = input("\nУ вас есть несохраненные изменения, хотете их сохранить? (y/n): ")
    if answer == "y":
        return True
    return False
    
def print_check_file():
    print("\nТелефонная книга не открыта или пустая")