from src.widget import check_bill, change_date


def test_check_bill():
    assert check_bill('Счет 64686473678894779589') == 'Счет **9589'
    assert check_bill('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'


def test_change_date():
    assert change_date("2018-07-11T02:26:18.671407") == '11.07.2018'
