import telebot

bot = telebot.TeleBot('6988921683:AAFmYYOH1mEcPHpay5GYNhWSgAPrQfWYdkw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, ' Привет!')

@bot.message_handler(commands=['one'])
def main(message):
    bot.send_message(message.chat.id, ' Вас приветствует первый бот создателя')

@bot.message_handler(commands=['one-day'])
def main(message):
    bot.send_message(message.chat.id, ' Первый день вебенара прошел интересно ')

@bot.message_handler(commands=['the-end'])
def main(message):
    bot.send_message(message.chat.id, ' Надеюсь я справился ')


bot.infinity_polling()