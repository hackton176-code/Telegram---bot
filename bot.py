from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = [
        [InlineKeyboardButton("🔥 JOIN NOW TO WATCH 🔥", url="https://t.me/hindidub_anime_crunchrolly")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    await update.message.reply_text("Click below 👇", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
