def check_bill(data: str) -> str:
    """"""
    if data.startswith('Счет'):
        return "Счет **" + data[-4:]
    return data[:-16] + data[-16:-12] + " " + data[-12:-10] + "** **** " + data[-4:]


a = ['Maestro 1596837868705199',
     'Счет 64686473678894779589',
     'MasterCard 7158300734726758',
     'Счет 35383033474447895560',
     'Visa Classic 6831982476737658',
     'Visa Platinum 8990922113665229',
     'Visa Gold 5999414228426353',
     'Счет 73654108430135874305', ]

for i in a:
    print(check_bill(i))

