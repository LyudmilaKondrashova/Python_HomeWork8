import view
import module
import data_input

def button_click():
    us_choice = view.show_menu()
    list_sotr = module.read_csv()
    if us_choice == 1:
        list_find = module.find_sotr(list_sotr)
        if len(list_find) == 0:
            print("В компании нет сотрудников с такой фамилией!")
        else:
            print("НАЙДЕННЫЕ СОТРУДНИКИ:")
            list_id = module.print_select(list_find)
        button_click()
    elif us_choice == 2:
        list_find = module.find_employees_by_position(list_sotr)
        if len(list_find) == 0:
            print("В компании нет сотрудников с такой должностью!")
        else:
            print("НАЙДЕННЫЕ СОТРУДНИКИ:")
            list_id = module.print_select(list_find)
        button_click()
    elif us_choice == 3:
        list_find = module.find_employees_by_salary_range(list_sotr)
        if len(list_find) == 0:
            print("В компании нет сотрудников с такой зарплатой!")
        else:
            print("НАЙДЕННЫЕ СОТРУДНИКИ:")
            list_id = module.print_select(list_find)
        button_click()
    elif us_choice == 4:
        new_id = list_sotr[len(list_sotr) - 1]["id"] + 1
        new_sotr = module.get_record(new_id)
        module.write_new_record_csv('database.csv', new_sotr)
        button_click()
    elif us_choice == 5:
        list_find = module.find_sotr(list_sotr)
        if len(list_find) == 0:
            print("В компании нет сотрудников с такой фамилией!")
        else:
            print("НАЙДЕННЫЕ СОТРУДНИКИ:")
            list_id =  module.print_select(list_find)
            id_del = data_input.get_id()
            if id_del not in list_id:
                print("Введен некорректный id!")
            else:
                module.delete_record_cvs('database.csv', list_sotr, id_del)
        button_click()
    elif us_choice == 6:
        us_choice_update = view.show_menu_update()
        if us_choice_update == 1:
            list_id =  module.print_select(list_sotr)
            id_update = data_input.get_id()
            if id_update not in list_id:
                print("Введен некорректный id!")
            else:
                module.update_record_cvs('database.csv', list_sotr, id_update)
            button_click()
        if us_choice_update == 2:
            list_find = module.find_sotr(list_sotr)
            if len(list_find) == 0:
                print("В компании нет сотрудников с такой фамилией!")
            else:
                print("НАЙДЕННЫЕ СОТРУДНИКИ:")
                list_id = module.print_select(list_find)
                id_update = data_input.get_id()
                if id_update not in list_id:
                    print("Введен некорректный id!")
                else:
                    module.update_record_cvs('database.csv', list_sotr, id_update)
            button_click()
        if us_choice_update == 3:
            button_click()
    elif us_choice == 7:
        module.write_json(list_sotr)
        button_click()
    elif us_choice == 8:
        module.write_csv(list_sotr)
        button_click()
    elif us_choice == 9:
        print('РАБОТА ПРИЛОЖЕНИЯ ЗАВЕРШЕНА!')
        