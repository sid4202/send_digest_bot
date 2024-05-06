import telebot
import os
import dotenv
import json
from Models import User
from sqlalchemy import insert
from sqlalchemy.orm import Session


def main():
    dotenv.load_dotenv()

    API_TOKEN = os.getenv('TELEGRAM_BOT_API_KEY')

    bot = telebot.TeleBot(API_TOKEN)

    # Handle '/start' and '/help'
    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton(text='Начать работу',
                                                    callback_data=json.JSONEncoder.encode({'name': 'startOperating',
                                                                                           'username': message.from_user}))

        markup.add(button)

        bot.send_message(chat_id=message.chat.id, text="Welcome to the digest bot", reply_markup=markup)

    # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(callback):
        callback_data = json.JSONDecoder.decode(callback.data)

        if callback_data['name'] == "startOperating":
            stmt = insert(User)
            data = {'username': callback_data['username']}

            Session.execute(statement=stmt, params=[data])

            markup = telebot.types.InlineKeyboardMarkup()

            button_construction = telebot.types.InlineKeyboardButton(text='Строительство',
                                                                     callback_data=json.JSONEncoder.encode(
                                                                         {'name': 'chooseTheme',
                                                                          'data': 'construction'}))

            button_stock = telebot.types.InlineKeyboardButton(text='Фондовый рынок',
                                                              callback_data=json.JSONEncoder.encode(
                                                                  {'name': 'chooseTheme',
                                                                   'data': 'stock_market'}))

            button_trade = telebot.types.InlineKeyboardButton(text='Розничная торговля',
                                                              callback_data=json.JSONEncoder.encode(
                                                                  {'name': 'chooseTheme',
                                                                   'data': 'trade'}))

            button_development = telebot.types.InlineKeyboardButton(text='Устойчивое развитие',
                                                                    callback_data=json.JSONEncoder.encode(
                                                                        {'name': 'chooseTheme',
                                                                         'data': 'development'}))

            button_HR = telebot.types.InlineKeyboardButton(text='Human Resources(HR)',
                                                           callback_data=json.JSONEncoder.encode({'name': 'chooseTheme',
                                                                                                  'data': 'hr'}))

            button_AD = telebot.types.InlineKeyboardButton(text='Реклама',
                                                       callback_data=json.JSONEncoder.encode({'name': 'chooseTheme',
                                                                                              'data': 'ad'}))
            markup.add(button_construction,
                   button_stock,
                   button_development,
                   button_AD,
                   button_HR,
                   button_trade)

            bot.send_message(chat_id=callback.message.chat.id, text="Выберите тематику дайджеста", reply_markup=markup)

        if callback_data['name'] == 'chooseTheme':


bot.infinity_polling()

main()
