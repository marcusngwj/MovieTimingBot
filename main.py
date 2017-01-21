from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

start_message = """ Hello, I'm the Movie Timing Bot! I can give you some usage stats for your stickers. Use these commands to control me:

Movie Timings
/cinema - choose the cinema
/movie - choose the movie
/date - choose the date
/time - choose the time
/ratings - get the ratings for a specific movie

/hello - greetings from me! :)
/help - show the list of commands
/cancel - cancel the current operation """

cinema_message = "Which cinema do you want to watch at?"
movie_message = "Which movie do you want to watch?"
date_message = "Which date do you want to watch the movie?"
time_message = "When do you want to watch the movie?"
ratings_message = "Which movie do you want to check the ratings?"

def button(bot, update):
    query = update.callback_query

    bot.editMessageText(text="Selected option: %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def start(bot, update):
    update.message.reply_text(start_message)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def cinema(bot, update):
    keyboard = [[InlineKeyboardButton("Cathay Cineplexes", callback_data='Cathay Cineplexes')],
                [InlineKeyboardButton("Filmgarde Cineplexes", callback_data='Filmgarde Cineplexes')],
                [InlineKeyboardButton("Golden Village", callback_data='Golden Village')],
                [InlineKeyboardButton("Shaw Theatres", callback_data='Shaw Theatres')],
                [InlineKeyboardButton("Any", callback_data='Any')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(cinema_message, reply_markup=reply_markup)

def movie(bot, update):
    update.message.reply_text(movie_message)

def date(bot, update):
    update.message.reply_text(date_message)

def time(bot, update):
    keyboard = [[InlineKeyboardButton("Morning", callback_data='Morning')],
                [InlineKeyboardButton("Afternoon", callback_data='Afternoon')],
                [InlineKeyboardButton("Night", callback_data='Night')],
                [InlineKeyboardButton("Midnight", callback_data='Midnight')],
                [InlineKeyboardButton("Any", callback_data='Any')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(time_message, reply_markup=reply_markup)

def ratings(bot, update):
    update.message.reply_text(ratings_message)

def cancel(bot, update):
    update.message.reply_text(
        'Bye {}'.format(update.message.from_user.first_name))

updater = Updater('321039232:AAH36i7fC0h3W2k9or7-IXDiR9Lp3BmhQZg')

updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('cinema', cinema))
updater.dispatcher.add_handler(CommandHandler('movie', movie))
updater.dispatcher.add_handler(CommandHandler('date', date))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('ratings', ratings))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel))

updater.start_polling()
updater.idle()