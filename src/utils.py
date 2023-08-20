import json
import os

def load_data_operations(json_path=os.path.join(os.path.dirname(__file__), 'operations.json')):
    """
    Функция строит абослютный путь до файла, открывает и распаковывает его из json.
    :param json_path:
    :return: list
    """
    with open(json_path, encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def sort_state_operations(operations):
    """
    Функция выбирает все операции со статусом EXECUTED.
    Возвращает список операций со статусом EXECUTED.
    :param operations:
    :return: list
    """
    executed_operations = []

    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            executed_operations.append(operation)

    return executed_operations


def sort_date_operations(operations):
    """
    Функция сортирует операции по дате.
    Возвращает отсортированный список операции по дате.
    :param operations:
    :return: list
    """
    operations.sort(key=lambda d: d['date'], reverse=True)

    return operations


def get_last_operations(operations):
    """
    Функция берет 5 последних выполненных операций.
    Вовзращает список из 5 операций
    :param operations:
    :return: list
    """
    last_operation = []
    limit = 5

    for index, operation in enumerate(operations):
        if index == limit:
            break
        last_operation.append(operation)

    return last_operation


def disquise_card(operation):
    """
    Функция маскирут номер карты или счета (если он указан в from).
    Функция возвращает строку с замаскированным номером, или при отсутствии карты, что карта отсутствует.
    :param operation:
    :return: str
    """
    disq_card = ''
    if 'from' in operation and len(operation['from']):
        str_list = operation['from'].split(' ')
        if len(str_list[-1]) == 16:
            disq_card = disq_card + ' '.join(str_list[:-1]) + ' ' + str_list[-1][:4] + ' ' + str_list[-1][4:6] + "**" \
            + ' ' + '****' + ' ' + str_list[-1][-4:] + ' ' + '->' + ' '
            return disq_card
        elif len(str_list[-1]) > 16:
            disq_card = disq_card + ' '.join(str_list[:-1]) + ' ' + '**' + str_list[-1][-4:] + ' ' + '->' + ' '
            return disq_card
    else:
        return 'Номер карты отсутствует -> '


def disquise_account(operation):
    """
    Функция маскирует номер счета.
    Возвращает строку с замаскированным номером счет, где видны только проследние 4 цифры.
    :param operation:
    :return: str
    """
    disc_acc = ''
    if 'to' in operation:
        str_list = operation['to'].split(' ')
        disc_acc += ' '.join(str_list[:-1]) + ' '
        disc_acc += str_list[-1].replace(str_list[-1][:-4], '**')
        return disc_acc


def get_amount(operation):
    """
    Функция возвращает сумму операции с указанием валюты.
    :param operation:
    :return: str
    """
    amount = ''
    amount = amount + operation['operationAmount']['amount'] + ' ' + operation['operationAmount']['currency']['name']

    return amount
