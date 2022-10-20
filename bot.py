import logging

from googletrans import Translator
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

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
    if len(context.args) != 1:
        await update.message.reply_text('Укажите, пожалуйста, язык единственным параметром')
    else:
        value = context.args[0]
        context.user_data['language'] = value
        await update.message.reply_text(f'Отлично! Выбранный язык: {value}\n'
                                        f'Теперь напишите фразу\n'
                                        f'Пример: /translate text')


async def trans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    translator = Translator()
    res = translator.translate(f'{context.args}', dest=context.user_data['language'])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Перевод: {res.text}')


if __name__ == '__main__':
    application = ApplicationBuilder().token('5514647661:AAHKRnXMae36RLPO80G5zylR4QIjMod3MRI').build()
    start_handler = CommandHandler('start', start)
    trans_handler = CommandHandler('translate', trans)
    rem_handler = CommandHandler('rem', rem)
    application.add_handler(start_handler)
    application.add_handler(trans_handler)
    application.add_handler(rem_handler)

    application.run_polling()
