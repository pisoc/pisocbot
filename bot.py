import os
import telegram.ext as ext


def hello_handler(update, context):
    update.message.reply_text('Hello there!')


if __name__ == '__main__':
    updater = ext.Updater(
        token=os.getenv('PISOCBOT_TOKEN'),
        use_context=True
    )
    dispatcher = updater.dispatcher

    dispatcher.add_handler(ext.CommandHandler('hello', hello_handler))
    updater.start_polling()
