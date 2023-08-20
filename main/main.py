from src.utils import load_data_operations, sort_state_operations, sort_date_operations, get_last_operations, \
    disquise_card, disquise_account, get_amount


def main():
    # Вызов функций для получения последних 5 отсортированных, выполненных операций
    operations = load_data_operations()
    executed_operations = sort_state_operations(operations)
    sort_date_op = sort_date_operations(executed_operations)
    last_operations = get_last_operations(sort_date_op)

    #Основной цикл программы вывода операций
    for operation in last_operations:
        print(f'{".".join(reversed(operation["date"][:10].split("-")))} {operation["description"]}')
        print(f'{disquise_card(operation)}{disquise_account(operation)} \n{get_amount(operation)}\n')

if __name__ == '__main__':
    main()
