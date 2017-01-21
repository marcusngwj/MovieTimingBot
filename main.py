from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('321039232:AAH36i7fC0h3W2k9or7-IXDiR9Lp3BmhQZg')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()