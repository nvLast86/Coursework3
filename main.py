import utils
from operation import Operation

modified_exc_operations = []


def main():
    operations_list = utils.get_operation_info()
    exc_operations = utils.get_executed_operations_list(operations_list)

    for exc_operation in exc_operations:
        exc_operation['date'] = utils.transform_date(exc_operation['date'])

    exc_operations = utils.sorted_exc_operations(exc_operations)

    for operation in exc_operations:
        operation['date'] = utils.convert_date_format(operation['date'])

    for i in range (0,5):
        print(f'{exc_operations[i]["date"]} {exc_operations[i]["description"]}')

#        print(f'{utils.transform_from_card(exc_operations[i])}')




"""
    for i in range(len(exc_operations)):
        if 'from' not in exc_operations[i]:
            exc_operations[i]['from'] = 'сведения отсутствуют'
        modified_operation = Operation(exc_operations[i]['id'], exc_operations[i]['date'],
                                       exc_operations[i]['operationAmount'], exc_operations[i]['description'],
                                       exc_operations[i]['from'], exc_operations[i]['to'])
        modified_exc_operations.append(modified_operation)

    print(modified_exc_operations)
"""


main()
