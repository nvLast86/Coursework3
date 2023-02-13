import utils


def main():
    # Получаем список всех операций из json файла
    operations_list = utils.get_operation_info()
    # Получаем список только из успешно проведенных операций
    exc_operations = utils.get_executed_operations_list(operations_list)

    # Преобразуем дату в нужную форму и добавляем сообщение "нет сведений" в поле 'from', если нет информации
    for exc_operation in exc_operations:
        exc_operation['date'] = utils.transform_date(exc_operation['date'])
        if 'from' not in exc_operation:
            exc_operation['from'] = 'нет сведений'

    # Сортируем список по дате, начиная с самой "свежей"
    exc_operations = utils.sorted_exc_operations(exc_operations)

    # Выводим информацию о 5 последних операциях в требуемой форме
    for i in range(0, 5):
        print(f'{utils.convert_date_format(exc_operations[i]["date"])} {exc_operations[i]["description"]}')
        print(f'{utils.transform_and_hide_data(exc_operations[i]["from"])} -> '
              f'{utils.transform_and_hide_data(exc_operations[i]["to"])}')
        print(f'{exc_operations[i]["operationAmount"]["amount"]}\n')


main()
