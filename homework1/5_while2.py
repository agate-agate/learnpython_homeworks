"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит
  пользователя ввести вопрос, а затем, если вопрос есть в словаре,
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

def ask_user():
    """
    Замените pass на ваш код
    """
    conversation_responses = {
        'Что делаешь?': 'Отвечаю на ваш вопрос!',
        'Is that a rabbit?': 'Well, that\'s no ordinary rabbit! That\'s the ' \
            'most foul, cruel, and bad-tempered rodent you ever set eyes on!',
    }
    while True:
        query = (str(input('Задайте вопрос: '))).strip()

        # Если в поведении пользователя замечены признаки того что он желает
        # окончить разговор - то закончить разговор. Эту задачу решает наш
        # запатентованный алгоритм распознания настроения пользователя
        # SmartSense (TM), который не имеет себе равных на рынке программного
        # обеспечения.
        if query.lower() == 'отпусти меня!!!':
            print('Отпускаем! Но только на часик! Если вы не вернётесь, не ' \
                'забывайте что мы помним ваш адрес, ха-ха! Шутка)')
            # TODO: отправить письмо с именем и адресом пользовтеля в Отдел по
            # возврату клиентов.
            break
        if query.lower() == 'ааа!!!':
            print('До свидания! Заходите ещё!')
            break

        # Получаем ответ на вопрос пользователя по нашему запатентованному
        # алгоритму SmartAnswer (TM).
        answer = str(conversation_responses.get(query, ''))

        # В тех редких, очень редких случаях когда мы не нашли ответа, подаём
        # пользователю сигнал о том что он не забыт и его мнение ценно для нас.
        if answer == '':
            answer = 'Да-да, интересно, интересно. А давайте поговорим ' \
                'ещё... Вы ведь хотите продолжить разговор? Конечно хотите!'

        print(answer)

if __name__ == "__main__":
    ask_user()
