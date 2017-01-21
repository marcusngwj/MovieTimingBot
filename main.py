from telegram.ext import Updater, CommandHandler

start_message = """ Hello, I'm the Movie Timing Bot! I can give you some usage stats for your stickers. Use these commands to control me:

Movie Timings
/cinema - choose the cinema
/movie - choose the movie
/date - choose the date
/time - choose the time
/ratings - get the ratings for a specific movie

/hello - greetings from me! :)
/cancel - cancel the current operation """

def start(bot, update):
    update.message.reply_text(start_message)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def cinema(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def movie(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def date(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def time(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def ratings(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def cancel(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('321039232:AAH36i7fC0h3W2k9or7-IXDiR9Lp3BmhQZg')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('cinema', cinema))
updater.dispatcher.add_handler(CommandHandler('movie', movie))
updater.dispatcher.add_handler(CommandHandler('date', date))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('ratings', ratings))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel))

updater.start_polling()
updater.idle()