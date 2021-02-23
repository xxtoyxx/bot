import telebot;
bot = telebot.TeleBot('1497292635:AAFSSB9lte78PaOgVF1xPGkGupJAy7VhthQ');
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
bot.polling(none_stop=True, interval=0)
