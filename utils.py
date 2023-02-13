import requests
from datetime import datetime


def get_operation_info():
    response = requests.get('https://www.jsonkeeper.com/b/T1M3')
    operations = response.json()
    return operations


def get_executed_operations_list(operations):
    exc_operations = []
    for operation in operations:
        if 'state' not in operation:
            continue
        if operation['state'] == 'EXECUTED':
            exc_operations.append(operation)
    return exc_operations


def sorted_exc_operations(operations):
    sorted_operations = sorted(operations,
                               key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
    return sorted_operations


def transform_date(exc_time):
    time = exc_time.split('T')
    time[1] = time[1][:8]
    time = ' '.join(time)
    return time


def convert_date_format(some_date):
    date = some_date[:10]
    date = date.split('-')
    date.reverse()
    new_format_date = '.'.join(date)
    return new_format_date


def transform_and_hide_data(data):
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
    hide_card_number_temp = []
    for i in range(len(card_number)):
        if 7 <= i <= 14:
            hide_card_number_temp.append('*')
        else:
            hide_card_number_temp.append(card_number[i])
    hide_card_number = ''.join(hide_card_number_temp)
    return hide_card_number
