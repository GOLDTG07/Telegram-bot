import telebot

TOKEN = '7703469222:AAF0DQExugC7MD6z1T4mzDQ8Q9W74tROizY'
bot = telebot.TeleBot(TOKEN)

channel_id = '@BERLIN_MAFIA'

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.chat.id == channel_id:
        bot.reply_to(message, "👍")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "👍")

bot.polling()
