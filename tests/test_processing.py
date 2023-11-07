from src.processing import state_into, sort_date


def test_state_into():
    assert (state_into([{'state': 'CANCELED'},
                        {'state': 'EXECUTED'}])) == [{'state': 'EXECUTED'}]


def test_sort_date():
    assert (sort_date([{'date': '2021-01-01'},
                        {'date': '2020-01-01'},
                        {'date': '2019-01-01'}]) ==
            [{'date': '2019-01-01'}, {'date': '2020-01-01'}, {'date': '2021-01-01'}])
