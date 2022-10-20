import logging

from telegram import Update, KeyboardButton
from googletrans import Translator
from telegram import ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update, _):
    await update.message.reply_text(f"Здравствуйте! Напишите язык, на который нужно перевести.\n"
                                    f"Доступные языки:\n"
                                    f"en - английский\n"
                                    f"fr - французский\n"
                                    f"de - немецкий\n"
                                    f"it - итальянский\n"
                                    f"ru - русский\n"
                                    f"es - испанский\n"
                                    f"tr - турецкий\n"
                                    f"Формат: /rem en")


async def rem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = context.args
    context.user_data['language'] = value
    await update.message.reply_text(f'Отлично! Выбранный язык: {value}\n'
                                    f'Теперь напишите фразу\n'
                                    f'Пример: /translate text')


if name == 'main':
    application = ApplicationBuilder().token('5514647661:AAHKRnXMae36RLPO80G5zylR4QIjMod3MRI').build()
    start_handler = CommandHandler('start', start)
    rem_handler = CommandHandler('rem', rem)
    application.add_handler(start_handler)
    application.add_handler(rem_handler)

    application.run_polling()
