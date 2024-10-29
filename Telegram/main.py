import telebot
import os
import dotenv
import json
from Models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    dotenv.load_dotenv()

    API_TOKEN = os.getenv('TELEGRAM_BOT_API_KEY')

    bot = telebot.TeleBot(API_TOKEN)

    # Handle '/start' and '/help'
    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton(text='Начать работу',
                                                    callback_data=json.dumps({'name': 'startOperating',
                                                                                           'username': message.from_user.username}))

        markup.add(button)

        bot.send_message(chat_id=message.chat.id, text="Welcome to the digest bot", reply_markup=markup)

    # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(callback):
        callback_data = json.loads(callback.data)
        engine = create_engine('postgresql://postgres:CrashLoyale@localhost/digest')

        session_maker = sessionmaker(bind=engine)
        session = session_maker()

        if callback_data['name'] == "startOperating":
            session.add

            markup = telebot.types.InlineKeyboardMarkup()

            button_construction = telebot.types.InlineKeyboardButton(text='Строительство',
                                                                     callback_data=json.dumps(
                                                                         {'name': 'chooseTheme',
                                                                          'data': 'construction'}))

            button_stock = telebot.types.InlineKeyboardButton(text='Фондовый рынок',
                                                              callback_data=json.dumps(
                                                                  {'name': 'chooseTheme',
                                                                   'data': 'stock_market'}))

            button_trade = telebot.types.InlineKeyboardButton(text='Розничная торговля',
                                                              callback_data=json.dumps(
                                                                  {'name': 'chooseTheme',
                                                                   'data': 'trade'}))

            button_development = telebot.types.InlineKeyboardButton(text='Устойчивое развитие',
                                                                    callback_data=json.dumps(
                                                                        {'name': 'chooseTheme',
                                                                         'data': 'development'}))

            button_HR = telebot.types.InlineKeyboardButton(text='Human Resources(HR)',
                                                           callback_data=json.dumps({'name': 'chooseTheme',
                                                                                                  'data': 'hr'}))

            button_AD = telebot.types.InlineKeyboardButton(text='Реклама',
                                                           callback_data=json.dumps({'name': 'chooseTheme',
                                                                                                  'data': 'ad'}))
            markup.add(button_construction,
                       button_stock,
                       button_development,
                       button_AD,
                       button_HR,
                       button_trade)

            bot.send_message(chat_id=callback.from_user.id, text="Выберите тематику дайджеста", reply_markup=markup)

        if callback_data['name'] == 'chooseTheme':
            markup = telebot.types.InlineKeyboardMarkup()

            button_individual = telebot.types.InlineKeyboardButton(text='Индивидуальная',
                                                                   callback_data=json.dumps(
                                                                       {
                                                                           'name': 'chooseTypeLicense',
                                                                           'data': 'individual'
                                                                       }
                                                                   ))

            button_corporate = telebot.types.InlineKeyboardButton(text='Корпоративная',
                                                                  callback_data=json.dumps(
                                                                      {
                                                                          'name': 'chooseTypeLicense',
                                                                          'data': 'corporate'
                                                                      }
                                                                  ))

            markup.add(button_individual,
                       button_corporate)

            bot.send_message(chat_id=callback.message.chat.id, text='Выберите тип подписки', reply_markup=markup)
        if callback_data['name'] == 'chooseTypeLicense':

            if callback_data['data'] == 'individual':
                # stmt = update(User).where(User.id == callback.from_user).values(User.)
                # Session.execute(statement=stmt, params=[data])
                markup = telebot.types.InlineKeyboardMarkup()

                button_everyday = telebot.types.InlineKeyboardButton(text='Каждый день',
                                                                     callback_data=json.dumps(
                                                                         {'name': 'chooseSchedule',
                                                                          'data': 'everyday'}))

                button_weekdays = telebot.types.InlineKeyboardButton(text='Будние дни',
                                                                     callback_data=json.dumps(
                                                                         {'name': 'chooseSchedule',
                                                                          'data': 'weekdays'}))

                button_monday = telebot.types.InlineKeyboardButton(text='Один день, в понедельник',
                                                                   callback_data=json.dumps(
                                                                       {'name': 'chooseSchedule',
                                                                        'data': 'monday'}))

                button_friday = telebot.types.InlineKeyboardButton(text='Один день, в пятницу',
                                                                   callback_data=json.dumps(
                                                                       {'name': 'chooseTheme',
                                                                        'data': 'friday'}))

                button_monday_2_weeks = telebot.types.InlineKeyboardButton(text='Раз в две недели, в понедельник',
                                                                           callback_data=json.dumps(
                                                                               {'name': 'chooseSchedule',
                                                                                'data': 'monday_2_weeks'}))

                button_friday_2_weeks = telebot.types.InlineKeyboardButton(text='Раз в две недели, в пятницу',
                                                                           callback_data=json.dumps(
                                                                               {'name': 'chooseSchedule',
                                                                                'data': 'friday_2_weeks'}))

                button_first_day_of_month = telebot.types.InlineKeyboardButton(text='1-е число каждого месяца',
                                                                               callback_data=json.dumps(
                                                                                   {'name': 'chooseSchedule',
                                                                                    'data': 'every_month'}))
                markup.add(button_everyday,
                           button_monday,
                           button_friday,
                           button_monday_2_weeks,
                           button_monday_2_weeks,
                           button_first_day_of_month)

                bot.send_message(chat_id=callback.message.chat.id, text="Выберите день получения",
                                 reply_markup=markup)

        if callback_data['name'] == 'chooseSchedule':
            markup = telebot.types.InlineKeyboardMarkup()

            button_9 = telebot.types.InlineKeyboardButton(text='9:00',
                                                          callback_data=json.dumps(
                                                              {'name': 'choose_time',
                                                               'data': '9am'}
                                                          ))

            button_18 = telebot.types.InlineKeyboardButton(text='18:00',
                                                           callback_data=json.dumps(
                                                               {
                                                                   "name": "choose_time",
                                                                   'data': '6pm'
                                                               }
                                                           ))

            markup.add(button_9,
                       button_18)

            bot.send_message(chat_id=callback.message.chat.id, text="Выберите время получения", reply_markup=markup)

    bot.infinity_polling()


main()
