import logging

from googletrans import Translator
from telegram import Update
from telegram.ext import CommandHandler, Updater, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
TOKEN = '5514647661:AAHKRnXMae36RLPO80G5zylR4QIjMod3MRI'


def start(update, _):
    update.message.reply_text(f"Здравствуйте! Напишите язык, на который нужно перевести.\n"
                              f"Доступные языки:\n"
                              f"en - английский\n"
                              f"fr - французский\n"
                              f"de - немецкий\n"
                              f"it - итальянский\n"
                              f"ru - русский\n"
                              f"es - испанский\n"
                              f"tr - турецкий\n"
                              f"Формат: /rem en")


def rem(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        update.message.reply_text('Укажите, пожалуйста, язык единственным параметром')
    else:
        value = context.args[0]
        context.user_data['language'] = value
        update.message.reply_text(f'Отлично! Выбранный язык: {value}\n'
                                  f'Теперь напишите фразу\n'
                                  f'Пример: /translate text')


def trans(update: Update, context: CallbackContext):
    translator = Translator()
    res = translator.translate(''.join(context.args), dest=context.user_data['language'])
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Перевод: {res.text}')


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    trans_handler = CommandHandler('translate', trans)
    rem_handler = CommandHandler('rem', rem)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(trans_handler)
    dispatcher.add_handler(rem_handler)

    updater.start_polling()
    updater.idle()
