import csv
import json
from pathlib import Path
import controller
import data_input
import view

def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    fin.close()
    return employee
            
def find_sotr(employees: list):
    last_name = data_input.get_last_name()
    find_employee = []
    for employee in employees:
        if last_name.lower() in employee['last_name'].lower():
            find_employee.append(employee)
    return find_employee

def find_employees_by_position(employees: list) -> list:
    result = []
    posit = input('Введите должность сотрудника: ')
    for employee in employees:
        if posit.lower() in employee['position'].lower():
            result.append(employee)
    return result

def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = data_input.get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result

def print_select(employees: list) -> list:
    list_id = []
    k = 1
    for el in employees:
        print(str(k) + '. ' + 'id=' + str(el['id']) + ', ' + el['last_name'] + ' ' + el["first_name"] + ', ' + el["position"] + ', тел. ' + el["phone_number"] + ', зарплата ' + str(el["salary"]))
        k += 1
        list_id.append(el['id'])
    return list_id

def get_record(id: int):
    new_record = ''
    new_record = str(id) + ',' + data_input.get_last_name() + ',' + data_input.get_first_name(data_input.get_name(), data_input.get_patronymic()) + ',' + data_input.get_position() + ',' + data_input.get_phone_number() + ',' + str(data_input.get_salary())
    return new_record

def write_new_record_csv(flname: str, new_rec: dict):
    filescv = open(Path.cwd() / flname, 'a', encoding='utf-8')
    filescv.write(new_rec)
    print('СОТРУДНИК ДОБАВЛЕН В БАЗУ')
    filescv.close()

def delete_record_cvs(flname:str, employees: list, id_sotr: int):
    filescv = open(Path.cwd() / flname, 'w', encoding='utf-8')
    for employee in employees:
        if int(employee["id"]) != id_sotr:
            empl_str = str(employee['id']) + ',' + employee['last_name'] + ',' + employee["first_name"] + ',' + employee["position"] + ',' + employee["phone_number"] + ',' + str(employee["salary"]) + '\n'
            filescv.write(empl_str)
    filescv.close()
    print('СОТРУДНИК УДАЛЕН ИЗ БАЗЫ')

def update_record_cvs(flname:str, employees: list, id_sotr: int):
    filescv = open(Path.cwd() / flname, 'w', encoding='utf-8')
    for employee in employees:
        if int(employee["id"]) == id_sotr:
            if view.show_question_last_name() == 1:
                employee['last_name'] = data_input.get_last_name()
            if view.show_question_first_name() == 1:
                employee["first_name"] = data_input.get_first_name(data_input.get_name(), data_input.get_patronymic())
            if view.show_question_position() == 1:
                employee["position"] = data_input.get_position()
            if view.show_question_phone_number() == 1:
                employee["phone_number"] = data_input.get_phone_number()
            if view.show_question_salary() == 1:
                employee["salary"] = data_input.get_salary()
        empl_str = str(employee['id']) + ',' + employee['last_name'] + ',' + employee["first_name"] + ',' + employee["position"] + ',' + employee["phone_number"] + ',' + str(employee["salary"]) + '\n'
        filescv.write(empl_str)
    filescv.close()
    print('ОБНОВЛЕНИЕ ДАННЫХ СОТРУДНИКА ПРОВЕДЕНО')

def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')
    fout.close()
    print('ЭКСПОРТ ДАННЫХ В ФОРМАТЕ json ПРОВЕДЕН')

def write_csv(employees: list):
    with open(Path.cwd() / 'database01.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())
    fout.close()
    print('ЭКСПОРТ ДАННЫХ В ФОРМАТЕ csv ПРОВЕДЕН')

