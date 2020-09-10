"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def ask_user():
    """
    Замените pass на ваш код
    """
    conversation_responses = {
        '2 + 2?': '5',
        'spam?': ('Vikings approve. ' * 8).strip(),
        'wound?': 'But a flesh one!',
        'rabbit?': 'Well, that\'s no ordinary rabbit! That\'s the most ' \
            'foul, cruel, and bad-tempered rodent you ever set eyes on!',
    }
    while True:
        try:
            query = (str(input('\nЗадайте вопрос: '))).strip()

            # Способ прекрарить диалог преждевременно.
            if query.lower() == 'goodbye':
                print('Пока!')
                break

            answer = str(conversation_responses.get(query, ''))

            if (answer != ''):
                print('Ответ: ' + answer)
        except KeyboardInterrupt:
            print('\nПока!')
            break

if __name__ == "__main__":
    ask_user()
