import telebot

bot = telebot.TeleBot("6055744163:AAFsENny4nPx5q05P2_zu_vUgftlbtI567g")

@bot.message_handler(commands=['start'])
def welcome(message):
    print(message.chat.id)
    bot.send_message(message.chat.id,
                     "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>!".format(message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
