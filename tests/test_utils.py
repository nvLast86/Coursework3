from utils import utils
def test_transform_date():
    assert utils.transform_date("2019-08-26T10:50:58.294041") == "2019-08-26 10:50:58"

def test_convert_date_format():
    assert utils.convert_date_format("2019-08-26 10:50:58") == '26.08.2019'

def test_transform_and_hide_data():
    assert utils.transform_and_hide_data("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert utils.transform_and_hide_data("Счет 19708645243227258542") == "Счет **8542"
    assert utils.transform_and_hide_data("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"

def test_get_hidden_card_number():
    assert utils.transform_and_hide_data("1596837868705199") == " 1596 83** **** 5199"

def test_sorted_exc_operations():
    assert utils.sorted_exc_operations([{'date': '2023-02-12 20:01:03'}, {'date': '2023-02-11 17:11:15'},
                                        {'date': '2023-02-13 12:01:01'}]) == [{'date': '2023-02-13 12:01:01'},
                                                                              {'date': '2023-02-12 20:01:03'},
                                                                              {'date': '2023-02-11 17:11:15'}]





