import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.error import BadRequest

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

PHOTO_URL = "https://files.fm/u/d2je9sfxfy"

CAPTION = (
    "👋 Welcome! Join our channel and visit our website\n\n"
    "💰 Free 38,888 Kyat 💰\n"
)

def build_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Join Channel", url="https://t.me/cryptotop1994"),
            InlineKeyboardButton("Visit Website", url="https://burmaking88.com/RF150370311"),
        ],
        [
            InlineKeyboardButton("🔁 Start Again", callback_data="start_again"),
        ]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=CAPTION,
        reply_markup=build_keyboard()
    )

async def start_again_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except BadRequest:
        pass
    await query.message.reply_photo(
        photo=PHOTO_URL,
        caption=CAPTION,
        reply_markup=build_keyboard()
    )

async def error_handler(update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Error: {context.error}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(start_again_callback, pattern="^start_again$"))
    app.add_error_handler(error_handler)

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
