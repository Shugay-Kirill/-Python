import view
import function_phonebook

def start():
    while True:
        choice_function = view.menu()
        match choice_function:
            case 1:
                function_phonebook.open_phonebook()
                print("Файл открыт")
            case 2: 
                function_phonebook.save_file_phonebook()  
                print("Файл сохранен")            
            case 3:
                phone_book = function_phonebook.get()
                view.print_phonebook(phone_book)
                
            case 4:
                new_contact = view.input_new_contact()
                function_phonebook.add_contact(new_contact)
            case 5:
                if function_phonebook.check_open_file():
                    phone_book = function_phonebook.get()
                    view.print_phonebook(phone_book)
                    id_user = view.input_id_user()
                    contact = view.input_new_contact()
                    function_phonebook.change_contact(id_user, contact)
                else:
                    view.print_check_file() 
            case 6:
                if function_phonebook.check_open_file():
                    find = view.find_contact()
                    result_find = function_phonebook.find(find)
                    view.print_phonebook(result_find)
                else:
                    view.print_check_file()
            case 7:
                if function_phonebook.check_open_file():
                    phone_book = function_phonebook.get()
                    view.print_phonebook(phone_book)
                    id_user = view.input_id_user()
                    name = function_phonebook.get_name(id_user)
                    if view.confirm("удалить", name):
                        function_phonebook.delete_contact(id_user)
                else:
                    view.print_check_file()
            case 8:
                if function_phonebook.check_changes():
                    if view.confirm_changes():
                        function_phonebook.save_file_phonebook()
                print("Всего хорошего")
                break
            
