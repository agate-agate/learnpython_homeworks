"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def ask_user():
    """
    Замените pass на ваш код
    """
    is_further_trolling_necessary = True
    while is_further_trolling_necessary:
        answer = str(input('Как дела? '))
        if (answer == 'Хорошо'):
            is_further_trolling_necessary = False


if __name__ == "__main__":
    ask_user()
