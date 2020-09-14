"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def compare_strings(a, b):
    if not isinstance(a, str):
        return 0
    if not isinstance(b, str):
        return 0
    if a == b:
        return 1
    if len(a) > len(b):
        return 2
    if b == 'learn':
        return 3

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(compare_strings(123, 0))
    print(compare_strings('ёж', 7))
    print(compare_strings(7, 'сопит'))
    print(compare_strings({}, []))
    print(compare_strings('ёж', []))
    print(compare_strings({}, 'сопит'))
    print(compare_strings('зловеще', 'зловеще'))
    print(compare_strings('зловеще', 'под'))
    print(compare_strings('зловеще', 'learn'))
    print(compare_strings('под', 'learn'))
    print(compare_strings('под', 'ёлкой'))

if __name__ == "__main__":
    main()
