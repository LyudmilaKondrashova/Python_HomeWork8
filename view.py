def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def show_menu_update() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие:")
    print("1. Вывести список всех сотрудников")
    print("2. Найти сотрудника по фамилии")
    print("3. Вернуться назад")
    return int(input("Введите номер необходимого действия: "))

def show_question_last_name() -> int:
    print("\n" + "=" * 20)
    print("Будете обновлять фамилию сотрудника?")
    print("1. да")
    print("2. нет")
    return int(input("Введите номер необходимого действия: "))

def show_question_first_name() -> int:
    print("\n" + "=" * 20)
    print("Будете обновлять имя/отчество сотрудника?")
    print("1. да")
    print("2. нет")
    return int(input("Введите номер необходимого действия: "))

def show_question_position() -> int:
    print("\n" + "=" * 20)
    print("Будете обновлять должность сотрудника?")
    print("1. да")
    print("2. нет")
    return int(input("Введите номер необходимого действия: "))

def show_question_phone_number() -> int:
    print("\n" + "=" * 20)
    print("Будете обновлять телефон сотрудника?")
    print("1. да")
    print("2. нет")
    return int(input("Введите номер необходимого действия: "))

def show_question_salary() -> int:
    print("\n" + "=" * 20)
    print("Будете обновлять зарплату сотрудника?")
    print("1. да")
    print("2. нет")
    return int(input("Введите номер необходимого действия: "))