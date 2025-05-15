mport telebot

API_KEY = "7578653757:AAGyM99MMy_ffcP7FRLpvw6cL5zMiscACm8"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Gold signals bot is running.")

bot.polling()
