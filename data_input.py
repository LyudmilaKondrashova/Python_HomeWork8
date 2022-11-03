def get_salary_range():
    low_salary = int(input('Введите нижнюю границу зарплаты: '))
    high_salary = int(input('Введите верхнюю границу зарплаты: '))
    if low_salary > high_salary:
        low_salary, high_salary = high_salary, low_salary
    return low_salary, high_salary

def get_id() -> int:
    id_sotr = int(input('Введите id сотрудника: '))
    return id_sotr

def get_last_name() -> str:
    last_name = input('Введите фамилию сотрудника: ')
    return last_name

def get_name() -> str:
    name = input('Введите имя сотрудника: ')
    return name

def get_patronymic() -> str:
    patronymic = input('Введите отчество сотрудника: ')
    return patronymic

def get_first_name(name: str, patronymic: str) -> str:
    first_name = name + ' ' + patronymic
    return first_name

def get_position() -> str:
    position = input('Введите должность сотрудника: ')
    return position

def get_phone_number() -> str:
    phone_number = input('Введите телефон сотрудника: ')
    return phone_number

def get_salary() -> float:
    salary = float(input('Введите зарплату сотрудника: '))
    return salary