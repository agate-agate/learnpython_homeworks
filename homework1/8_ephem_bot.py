"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import easy_planets
import bot_settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': bot_settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': bot_settings.PROXY_USERNAME,
        'password': bot_settings.PROXY_PASSWORD,
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def tell_user_about_planet(update, context):
    print('Вызван /planet')

    print('update:')
    print(update)
    print('context:')
    print(context)
    print('update.message.text:')
    print(update.message.text)

    user_text = str(update.message.text)
    text_pieces = user_text.split()

    try:
        _ = str(text_pieces[1])
    except:
        _ = ''
    raw_planet_name = _

    planet_name = easy_planets.normalize_planet_name(raw_planet_name)

    constellation_label = easy_planets.get_constellation_label_for_planet(raw_planet_name)

    message_lines = [
        'Вызван /planet',
        'Ты хочешь узнать про планету: ' + raw_planet_name,
        'Которая распозналась как: '     + planet_name,
        'Она находится в созвездии: '    + constellation_label,
    ]
    update.message.reply_text('\n'.join(message_lines))

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(bot_settings.API_KEY,
                    use_context=True,
                    request_kwargs=PROXY
    )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', tell_user_about_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
