"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list = [
        {
            'name': 'Мумми Тролль',
            'age': 12,
            'job': 'Домохозяин',
        },
        {
            'name': 'Снуснумрик',
            'age': 16,
            'job': 'Турист',
        },
        {
            'name': 'Крошка Мю',
            'age': 12,
            'job': 'Троллинг (высококачественный)',
        },
        {
            'name': 'Морра',
            'age': 'неизвестно',
            'job': 'Жуткий хтонизм',
        },
    ]
    with open('3_dict_to_csv__result__export.csv', 'w', encoding='utf-8') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=':')
        # writer.writeheader()
        for row in list:
            writer.writerow(row)

if __name__ == "__main__":
    main()
