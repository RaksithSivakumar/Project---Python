from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'USER_CHAT_ID'
MESSAGE = 'Hello from my Telegram bot!'

def send_message(bot_token, chat_id, message):
    """Send a message to a specified chat ID."""
    try:
        bot = Bot(token=bot_token)
        bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully!")
    except TelegramError as e:
        print(f"An error occurred: {e}")

def get_chat_id(bot_token):
    """Fetch updates to find chat IDs."""
    try:
        bot = Bot(token=bot_token)
        updates = bot.get_updates()
        for update in updates:
            print(f'Chat ID: {update.message.chat_id}')
    except TelegramError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_message(BOT_TOKEN, CHAT_ID, MESSAGE)
    
    
