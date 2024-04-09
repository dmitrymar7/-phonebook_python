import model


def get_number_record():
    n = input("Введите номер строки: ")
    if not n.isdigit():
        print("Введенное значение не число")
        return get_number_record()

    return int(n)


def print_list_start_operation():
    text = "Выберите действие: \n" \
           "1 - Указать файл телефонного справочника \n" \
           "2 - Использовать файл по-умолчанию \n" \
           "exit - Завершить"

    print(text)


def print_list_operation():
    text = "Выберите действие: \n" \
           "1 - Отобразить справочник \n" \
           "2 - Добавить запись \n" \
           "3 - Удалить запись \n" \
           "4 - Найти телефон \n" \
           "5 - Редактировать запись \n" \
            "6 - Копировать из другого справочника \n" \
           "exit - Завершить"

    print(text)


def report_bug(text):
    print(text)


def get_file_name():
    file_name = input('Введите имя файла телефонного справочника: ')
    file_name = file_name if len(file_name) > 0 else None
    return file_name


def get_operation():
    n = input("Ваше действие: ")
    return n


def print_table(phonebook: model.Phonebook):
    print(phonebook)


def get_data_record_from_file():
    file_name = input('Введите адрес файла: ')
    line_number = input('Введите номер строки: ')

    file_name = file_name if len(file_name) > 0 else None

    return {'file_name': file_name, 'line_number': line_number}


def add_record(phonebook: model.Phonebook):

    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    comment = input("Введите комментарий: ")

    record = model.Record(name, phone, comment)
    phonebook.add_record(record)


def del_record(phonebook: model.Phonebook):

    n = input("Введите номер строки: ")
    if not n.isdigit():
        print("Введенное значение не число")
        return

    index = int(n) - 1
    try:
        del phonebook[index]
    except Exception as e:
        print(e)


def search(phonebook: model.Phonebook):
    name = input("Введите имя: ")
    records = phonebook.get_records()

    lst = list()
    lst = list(filter(lambda x: isinstance(x, model.Record) and x.name == name, records))

    for index, record in enumerate(lst):
        print(f"- Телефон: {record.telephone}  Комментарий: {record.comment}")


def change_operations():
    text = "Что хотите изменить? \n" \
           "1 - имя \n" \
           "2 - телефон \n" \
           "3 - комментарий \n" \
           "4 - отмена"

    print(text)


def get_value(description=""):
    return input(description)
