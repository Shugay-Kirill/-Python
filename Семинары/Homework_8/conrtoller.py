import view
from function_phonebook import Phone_book

def start():
    while True:
        choice_function = view.menu()
        match choice_function:
            case 1:
                Pb = Phone_book("dictionary.txt")
                print("Файл открыт")
            case 2: 
                Pb.save_file_phonebook()
                print("Файл сохранен")            
            case 3:
                phone_book = Pb.get()
                view.print_phonebook(phone_book)
            case 4:
                new_contact = view.input_new_contact()
                Pb.add_contact(new_contact)
            case 5:
                if Pb.check_open_file():
                    phone_book = Pb.get()
                    view.print_phonebook(phone_book)
                    id_user = view.input_id_user()
                    contact = view.input_new_contact()
                    Pb.change_contact(id_user, contact)
                else:
                    view.print_check_file() 
            case 6:
                if Pb.check_open_file():
                    find = view.find_contact()
                    result_find = Pb.find(find)
                    view.print_phonebook(result_find)
                else:
                    view.print_check_file()
            case 7:
                if Pb.check_open_file():
                    phone_book = Pb.get()
                    view.print_phonebook(phone_book)
                    id_user = view.input_id_user()
                    name = Pb.get_name(id_user)
                    if view.confirm("удалить", name):
                        Pb.delete_contact(id_user)
                else:
                    view.print_check_file()
            case 8:
                if Pb.check_changes():
                    if view.confirm_changes():
                        Pb.save_file_phonebook()
                print("Всего хорошего")
                break
            
