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

def transform_from_card(info):
    card_data = {'card_name': None, 'card_number': None}
    temporary_card_name = []
    info_list = info.split(' ')
    for example in info_list:
        if example.isdigit():
           temp_example = [example[i:i+4] for i in range(0, len(example), 4)]
           temp_example = ' '.join(temp_example)
           card_data['card_number'] = example
        else:
           temporary_card_name.append(example)
    if len(temporary_card_name) > 1:
        card_data['card_name'] = ' '.join(temporary_card_name)
    else:
        card_data['card_name'] = temporary_card_name[0]
    return card_data

def hide_card_info(card_number, flag):
    hide_card_number_temp = []
    if flag == 'from':
        for i in range(len(card_number)):
            if 7 <= i <= 14:
                hide_card_number_temp.append('*')
            else:
                hide_card_number_temp.append(card_number[i])
        hide_card_number = ''.join(hide_card_number_temp)
    else:
        hide_card_number = '**' + card_number[15:19]
    return hide_card_number




#print(hide_card_info('4195 1911 7258 3802', 'from'))

#print(transform_from_card("Visa Classic 4195191172583802"))

#print(transform_from_card("Счет 73654108430135874305"))

#print(get_executed_operations_list(get_operation_info()))

print(convert_date_format('2019-12-08 22:46:21'))

