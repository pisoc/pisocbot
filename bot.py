import os
import telegram.ext as ext

TELEGRAM_API_TOKEN = os.getenv('PISOCBOT_TOKEN')
PORT = int(os.getenv('PISOCBOT_PORT'))


def hello_handler(update, context):
    update.message.reply_text('Hello there!')


if __name__ == '__main__':
    updater = ext.Updater(
        token=TELEGRAM_API_TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(ext.CommandHandler('hello', hello_handler))

    updater.start_webhook(
        listen='0.0.0.0', port=PORT, url_path=TELEGRAM_API_TOKEN)
    updater.bot.setWebhook(
        'https://pisocbot.herokuapp.com/' + TELEGRAM_API_TOKEN)

    updater.idle()

