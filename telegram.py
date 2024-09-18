from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 'YOUR_API_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I am your bot.')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
