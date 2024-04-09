import view
import model
import os


def begin():
    view.print_list_start_operation()
    operation = view.get_operation()
    if is_terminate(operation):
        return

    phonebook = None
    if operation == '1':
        file_name = view.get_file_name()
        if file_name is not None:
            phonebook = model.Phonebook(file_name)
    elif operation == '2':
        phonebook = model.Phonebook()

    if phonebook is None:
        return

    begin_operation_with_phonebook(phonebook)


def begin_operation_with_phonebook(phonebook: model.Phonebook):
    while True:
        view.print_list_operation()
        operation = view.get_operation()
        if is_terminate(operation):
            break
        execute_operation(operation, phonebook)
        print()


def is_terminate(operation):
    if operation == "exit":
        return True
    return False


def execute_operation(operation, phonebook: model.Phonebook):
    if operation == "1":
        view.print_table(phonebook)
    elif operation == "2":
        view.add_record(phonebook)
    elif operation == "3":
        view.del_record(phonebook)
    elif operation == "4":
        view.search(phonebook)
    elif operation == "5":
        change_record(phonebook)
    elif operation == "6":
        add_record_from_file(phonebook)
    else:
        view.report_bug(ValueError("Действие не определено"))


def add_record_from_file(phonebook: model.Phonebook):
    data_record = view.get_data_record_from_file()
    file_name = data_record.get('file_name')
    line_number = data_record.get('line_number')

    if file_name is None:
        view.report_bug(Exception("Файл не задан"))
        return
    elif not os.path.isfile(file_name):
        view.report_bug(Exception("Файл не найден"))
        return

    if line_number is None:
        view.report_bug(Exception("Не указана строка для копирования"))
        return
    elif not line_number.isdigit():
        view.report_bug(Exception("Строка для копирования указана неверно"))
        return

    index = int(line_number) - 1

    try:
        pb = model.Phonebook(file_name)
        record_pb = pb[index]

        phonebook.add_record(record_pb)
    except Exception as e:
        view.report_bug(Exception("Возникла ошибка при добавлении данных"))


def change_record(phonebook: model.Phonebook):
    n = view.get_number_record()
    index = int(n) - 1

    record = None
    try:
        record = phonebook[index]
    except Exception as e:
        view.report_bug(IndexError("Некорректный номер строки"))
        return

    view.change_operations()
    operation = view.get_operation()

    if operation == "1":
        name = view.get_value("имя: ")
        record.name = name
    elif operation == "2":
        phone = view.get_value("телефон: ")
        record.telephone = phone
    elif operation == "3":
        comment = view.get_value("комментарий: ")
        record.comment = comment
    elif operation == "4":
        return
    else:
        view.report_bug(Exception("Действие не определено"))
        return

    phonebook[index] = record


def search():
    name = view.get_value("имя: ")

