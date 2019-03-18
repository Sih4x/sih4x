#!/user/bin/env python
import telebot


token = '755294274:AAE9jBEwGon-_qf8cJj9IIKfdJyJ069_sLA' # Тестовый бот MainInvest
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет!', parse_mode="Html")




if __name__ == '__main__':
    bot.polling(none_stop=True)