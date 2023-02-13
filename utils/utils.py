import requests
from datetime import datetime


def get_operation_info():
    """
    Получение списка всех операций из json файла, загруженного на сайт.
    :return: список всех операций.
    """
    response = requests.get('https://www.jsonkeeper.com/b/T1M3')
    operations = response.json()
    return operations


def get_executed_operations_list(operations):
    """
    Получение списка успешно проведенных операций.
    :param operations: список всех операций.
    :return: список успешно проведенных операций.
    """
    exc_operations = []
    for operation in operations:
        if 'state' not in operation:
            continue
        if operation['state'] == 'EXECUTED':
            exc_operations.append(operation)
    return exc_operations


def sorted_exc_operations(operations):
    """
    Сортировка списка успешно проведенных операций, начиная с самой "свежей".
    :param operations: список успешно проведенных операций.
    :return: отсортированный список успешно проведенных операций.
    """
    sorted_operations = sorted(operations,
                               key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
    return sorted_operations


def transform_date(exc_time):
    """
    Извлечение даты проведения операции.
    :param exc_time: дата проведения операции в необработанном виде.
    :return: дата проведения операции в необходимом формате ГГГГ-ММ-ДД.
    """
    time = exc_time.split('T')
    time[1] = time[1][:8]
    time = ' '.join(time)
    return time


def convert_date_format(some_date):
    """
    Преобразование даты в требуемый для вывода формат.
    :param some_date: дата проведения операции ГГГГ-ММ-ДД.
    :return: дата проведения операции ДД-ММ-ГГГГ.
    """
    date = some_date[:10]
    date = date.split('-')
    date.reverse()
    new_format_date = '.'.join(date)
    return new_format_date


def transform_and_hide_data(data):
    """
    Получение зашифрованной информации о транзакции с какого или на какой счет/карту.
    :param data: информация о счете или карты.
    :return: зашифрованная информация о счете или карте.
    """
    card_number = ''
    data_list = data.split(' ')
    if 'Счет' not in data_list:
        card_name_list = []
        for obj in data_list:
            if obj.isdigit():
                card_number = [obj[i:i + 4] for i in range(0, len(obj), 4)]
                card_number = ' '.join(card_number)
            else:
                card_name_list.append(obj)
        card_name = ' '.join(card_name_list)
        hide_data = card_name + ' ' + get_hidden_card_number(card_number)
    else:
        new_data = data_list[0] + ' ' + data_list[1]
        hide_data = 'Счет **' + new_data[len(data) - 4:len(new_data):1]
    return hide_data


def get_hidden_card_number(card_number):
    """
    Шифрование номера карты.
    :param card_number: номер карты.
    :return: зашифрованный номер карты.
    """
    hide_card_number_temp = []
    for i in range(len(card_number)):
        if 7 <= i <= 8 or 10 <= i <= 13:
            hide_card_number_temp.append('*')
        else:
            hide_card_number_temp.append(card_number[i])
    hide_card_number = ''.join(hide_card_number_temp)
    return hide_card_number
