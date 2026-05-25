import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот для записи на танцы работает! 🕺")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
