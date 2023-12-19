from os.path import exists  # Импорт функции exists из модуля os.path.
from csv import DictReader, DictWriter  # Импорт классов DictReader и DictWriter из модуля csv.

def get_personal_info():
    # Функция для получения и возврата персональной информации в виде списка.
    first_name = "Антон"  # Присвоение примера имени.
    last_name = "Дмитриев"   # Присвоение примера фамилии.
    phone_number = "79111111111"  # Присвоение примера номера телефона.
    return [first_name, last_name, phone_number]

def initialize_file(file_name):
    # Функция для инициализации CSV-файла с указанными заголовками.
    with open(file_name, "w", encoding='utf-8') as data:
        writer = DictWriter(data, fieldnames=['First Name', 'Last Name', 'Phone Number'])
        writer.writeheader()  # Запись заголовка в файл.

def initialize_copies_file(file_name_copies):
    # Функция для инициализации пустого файла копий.
    with open(file_name_copies, 'w', encoding='utf-8') as data:
        data.write("")  # Запись пустого содержимого в файл.

def get_line_to_copy():
    # Функция для получения номера строки для копирования от пользователя.
    line_index = int(input("Введите номер строки для копирования: ")) - 1
    return line_index

def read_data(file_name):
    # Функция для чтения данных из CSV-файла и возврата их в виде списка словарей.
    with open(file_name, "r", encoding='utf-8') as data:
        reader = DictReader(data)
        return list(reader)

def write_data(file_name, data_list):
    # Функция для записи данных в CSV-файл.
    existing_data = read_data(file_name)  # Чтение существующих данных из файла.
    new_entry = {"First Name": data_list[0], "Last Name": data_list[1], "Phone Number": data_list[2]}
    existing_data.append(new_entry)  # Добавление новой записи к существующим данным.
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        writer = DictWriter(data, fieldnames=['First Name', 'Last Name', 'Phone Number'])
        writer.writeheader()  # Запись заголовка в файл.
        writer.writerows(existing_data)  # Запись всех данных в файл.

file_name = 'personal_data.csv'  # Присвоение имени основного CSV-файла.
file_name_copies = 'copies.csv'  # Присвоение имени файла копий.

def copy_data_line(file_name, file_name_copies, line_index):
    # Функция для копирования определенной строки из основного файла в файл копий.
    copied_line = []  # Инициализация списка для скопированных данных.
    with open(file_name, 'r', encoding='utf-8') as data:
        content = data.read()
        lines = list(content.split("\n"))  # Разделение содержимого на строки.
        if line_index < len(lines):
            copied_line.append(lines[line_index])  # Добавление скопированной строки в список.
        else:
            print('Эта строка отсутствует в файле!\n')

    with open(file_name_copies, 'a', encoding='utf-8') as copy_data:
        copy_data.seek(2)
        copy_data.write("\n")  # Добавление новой строки перед вставкой данных.
        copy_data.writelines("\n".join(copied_line))  # Запись скопированных данных в файл копий.

    if line_index < len(lines):
        print(f'Строка #{line_index + 1} скопирована.\n')

def main():
    # Основная функция для выполнения команд пользователя в цикле.
    while True:
        print("Список команд: Запись, Чтение, Копировать")
        com = input("Введите команду: ")
        if com == 'Выйти':
            break
        elif com == 'Запись':
            if not exists(file_name):
                initialize_file(file_name)  # Инициализация файла, если он не существует.
            write_data(file_name, get_personal_info())  # Запись новых данных в основной файл.
        elif com == 'Чтение':
            if not exists(file_name):
                print("Файл не найден. Пожалуйста, создайте его.")
                continue
            print(*read_data(file_name))  # Вывод данных из основного файла.
        elif com == 'Копировать':
            copy_data_line(file_name, file_name_copies, get_line_to_copy())  # Копирование строки в файл копий.

main()
