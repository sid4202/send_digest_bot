import telebot
import os
import dotenv


def main():
    dotenv.load_dotenv()

    API_TOKEN = os.getenv('TELEGRAM_BOT_API_KEY')

    bot = telebot.TeleBot(API_TOKEN)

    # Handle '/start' and '/help'
    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton(text='Начать работу', callback='startOperating')

        markup.add(button)

        bot.send_message(chat_id=message.chat.id, text="Welcome to the digest bot", reply_markup=markup)

    # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(callback):
        if callback. == "startOperating":
            markup = telebot.types.InlineKeyboardMarkup()

            button_construction = telebot.types.InlineKeyboardButton(text='Строительство',
                                                                     callback='chooseTheme',
                                                                     callback_data='construction')

            button_stock = telebot.types.InlineKeyboardButton(text='Фондовый рынок',
                                                                     callback='chooseTheme',
                                                                     callback_data='stock_market'
                                                                     )

            button_trade = telebot.types.InlineKeyboardButton(text='Розничная торговля',
                                                                     callback='chooseTheme',
                                                                     callback_data='stock_market')

            button_development = telebot.types.InlineKeyboardButton(text='Устойчивое развитие',
                                                                     callback='chooseTheme',
                                                                     callback_data='stock_market')

            button_HR = telebot.types.InlineKeyboardButton(text='Human Resources(HR)',
                                                                     callback='chooseTheme',
                                                                     callback_data='stock_market')

            button_AD = telebot.types.InlineKeyboardButton(text='Реклама',
                                                                     callback='chooseTheme',
                                                                     callback_data='stock_market')
            markup.add(button_construction,
                       button_stock,
                       button_development,
                       button_AD,
                       button_HR,
                       button_trade)

            bot.send_message(chat_id=callback.message.chat.id, text="Выберите тематику дайджеста", reply_markup=markup)



    bot.infinity_polling()


main()
