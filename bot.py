import logging

from telegram import Update, KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Эй, {update.message.chat.first_name}! Где ваша вежливость?"
                                    f"\nНапишите <i>здравствуйте</i>, чтобы запустить меня", parse_mode=ParseMode.HTML)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "здравствуйте" in text.lower():
        await update.message.reply_text(f"И вам не хворать! Что сегодня хотите перевести?")
    else:
        await update.message.reply_text(
            "Ничего не понял... Может попробуете еще раз?")


if __name__ == '__main__':
    application = ApplicationBuilder().token('5514647661:AAGdRD2u3KH0Slf6ugtPdzNm5TbIiGAZnr4').build()
    hello_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), hello)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(hello_handler)

    application.run_polling()

[f[f[[f[]]]]]