import pytest

from src.utils import sort_state_operations, sort_date_operations, load_data_operations, get_last_operations, \
    disquise_account, disquise_card

@pytest.mark.parametrize('expected', [True])
def test_load_data(expected):
    assert isinstance(load_data_operations(), list) == expected


@pytest.mark.parametrize('operation, state, expected', [
    (sort_state_operations(load_data_operations())[1].values(), 'EXECUTED', True),
    (sort_state_operations(load_data_operations())[-1].values(), 'CANCELED', False)
])
def test_sort_state_op(operation, state, expected):
    entrance = state in operation
    assert entrance == expected


@pytest.mark.parametrize('list, expected', [
    ([{'date': '2005'}, {'date': '2020'}, {'date': '2001'}], [{'date': '2020'}, {'date': '2005'}, {'date': '2001'}])
])
def test_sort_date_op(list, expected):
    assert sort_date_operations(list) == expected


def test_get_last_op():
    assert len(get_last_operations(load_data_operations())) == 5


@pytest.mark.parametrize('account_number, expected', [
    ({'to': 'Счет 12345678901234567890'}, 'Счет **7890')
])
def test_disquise_account(account_number, expected):
    assert disquise_account(account_number) == expected


@pytest.mark.parametrize('card_number, expected', [
    ({"from": "Test 1234567890123456"}, 'Test 1234 56** **** 3456 -> '),
    ({'from': 'Счет 12345678901234567890'}, 'Счет **7890 -> ')
])
def test_disquise_card(card_number, expected):
    assert disquise_card(card_number) == expected


def test_disquise_card2():
    assert disquise_card([]) == 'Номер карты отсутствует -> '




