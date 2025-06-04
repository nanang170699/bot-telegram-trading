import os
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ Bot aktif dan siap kirim sinyal!")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
