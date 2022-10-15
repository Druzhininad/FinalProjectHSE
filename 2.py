import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Отправь мне сообщение, а то не увидишь что "
                                                                          "я умею!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def low(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_low = ' '.join(context.args).lower()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_low)


if __name__ == '__main__':
    application = ApplicationBuilder().token('5514647661:AAGdRD2u3KH0Slf6ugtPdzNm5TbIiGAZnr4').build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    low_handler = CommandHandler('low', low)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(low_handler)

    application.run_polling()
