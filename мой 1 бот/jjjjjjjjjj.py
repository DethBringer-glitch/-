import telebot

# токен бота
bot = telebot.TeleBot("7200079765:AAHVuz4tXoNQdK4NwlepkD39NTI9KnnpnSo")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я не знаю такой команды. Напиши /help.")

bot.polling(none_stop=True, interval=0)