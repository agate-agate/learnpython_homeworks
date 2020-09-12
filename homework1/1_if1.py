"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

MIN_LIMIT_EMBRYO       = - 9 / 12
MIN_LIMIT_BIRTH        = 0
MIN_LIMIT_NURSERY      = 1.5
MIN_LIMIT_KINDERGARTEN = 3
MIN_LIMIT_SCHOOL       = 7
MIN_LIMIT_UNIVERSITY   = MIN_LIMIT_SCHOOL + 11
MIN_LIMIT_ENLIGHTENED  = MIN_LIMIT_UNIVERSITY + 5

def get_predicted_ocupation_message(age):
    try:
        age = float(str(age))
    except:
        return 'Это не похоже на число! Запустите эту программу заново и '\
            'введите число.'

    if age >= MIN_LIMIT_ENLIGHTENED:
        return 'Скорее всего, вы работаете или являетесь ' \
            'домохозяйкой/домохозяином'

    if age >= MIN_LIMIT_UNIVERSITY:
        return 'Скорее всего, вы учитесь в ВУЗе'

    if age >= MIN_LIMIT_SCHOOL:
        return 'Скорее всего, вы учитесь в школе'

    if age >= MIN_LIMIT_KINDERGARTEN:
        return 'Скорее всего, вы учитесь в детском саду'

    if age >= MIN_LIMIT_NURSERY:
        return 'Скорее всего, вы находитесь в яслях'

    if age >= MIN_LIMIT_BIRTH:
        return 'Скорее всего, вы ещё слишком молоды для яслей'

    if age >= MIN_LIMIT_EMBRYO:
        return 'Скорее всего, вы ещё находитесь в зародыше'

    return 'Скорее всего, вы ещё не были зачаты'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = input('Введите свой возраст: ')
    message = get_predicted_ocupation_message(age)
    print(message)

if __name__ == "__main__":
    main()
