import requests
from operation import Operation

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

#def exc_operations_in_needed_view(operations):
#    operations_in_required_view= {}
#    for operation in operations:
#        operations_in_required_view['description'] == operation['description']

def transform_date(exc_time):
    time_ = exc_time[0:10]
    time = time_.split('-')
    time.reverse()
    return time

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




print(hide_card_info('4195 1911 7258 3802', 'from'))

#print(transform_from_card("Visa Classic 4195191172583802"))

#print(transform_from_card("Счет 73654108430135874305"))

#print(get_executed_operations_list(get_operation_info()))



