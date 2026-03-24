{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
import logging\
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup\
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes\
from telegram.error import BadRequest\
from keep_alive import keep_alive\
\
logging.basicConfig(\
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
    level=logging.INFO\
)\
\
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")\
\
PHOTO_URL = "https://files.fm/u/d2je9sfxfy"\
\
CAPTION = (\
    "\uc0\u55356 \u57225  Welcome! Join our channel and visit our website\\n\\n"\
    "\uc0\u55357 \u56496  Free 38,888 Kyat \u55357 \u56496 \\n"\
    "\uc0\u55356 \u57217 \u55357 \u56613 \u55356 \u57226 "\
)\
\
\
def build_keyboard():\
    return InlineKeyboardMarkup([\
        [\
            InlineKeyboardButton("Join Channel", url="https://t.me/cryptotop1994"),\
            InlineKeyboardButton("\uc0\u4129 \u4096 \u4145 \u4140 \u4100 \u4151 \u4154 \u4118 \u4157 \u4100 \u4151 \u4154 \u4123 \u4116 \u4154 \u4124 \u4100 \u4151 \u4154 ", url="https://burmaking88.com/RF150370311"),\
        ],\
        [\
            InlineKeyboardButton("\uc0\u55357 \u56580  Start Again", callback_data="start_again"),\
        ]\
    ])\
\
\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    await update.message.reply_photo(\
        photo=PHOTO_URL,\
        caption=CAPTION,\
        reply_markup=build_keyboard()\
    )\
\
\
async def start_again_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    query = update.callback_query\
    try:\
        await query.answer()\
    except BadRequest:\
        pass\
    await query.message.reply_photo(\
        photo=PHOTO_URL,\
        caption=CAPTION,\
        reply_markup=build_keyboard()\
    )\
\
\
async def error_handler(update, context: ContextTypes.DEFAULT_TYPE):\
    logging.error(f"Error: \{context.error\}")\
\
\
def main():\
    keep_alive()\
\
    app = ApplicationBuilder().token(BOT_TOKEN).build()\
    app.add_handler(CommandHandler("start", start))\
    app.add_handler(CallbackQueryHandler(start_again_callback, pattern="^start_again$"))\
    app.add_error_handler(error_handler)\
\
    print("Bot is running...")\
    app.run_polling(drop_pending_updates=True)\
\
\
if __name__ == "__main__":\
    main()}