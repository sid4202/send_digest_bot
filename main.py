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
        button = telebot.types.InlineKeyboardButton(text='Начать работу', callback_data='startOperating')

        markup.add(button)

        bot.send_message(chat_id=message.chat.id, text="Welcome to the digest bot", reply_markup=markup)

    # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(callback):
        if callback.data == "startOperating":
            bot.send_message(chat_id=callback.message.chat.id, text="Давайте начнем регистрацию")

    bot.infinity_polling()


main()
