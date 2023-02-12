import utils
from operation import Operation

modified_exc_operations = []

def main():
    operations_list = utils.get_operation_info()
    exc_operations = utils.get_executed_operations_list(operations_list)
    for i in range(len(exc_operations)):
        if 'from' not in exc_operations[i]:
            continue
        modified_operation = Operation(exc_operations[i]['id'], exc_operations[i]['date'],
                                               exc_operations[i]['operationAmount'], exc_operations[i]['description'],
                                               exc_operations[i]['from'], exc_operations[i]['to'])
        modified_exc_operations.append(modified_operation)
    print(modified_exc_operations)












main()