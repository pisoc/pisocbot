import os
import telegram.ext as ext

TELEGRAM_API_TOKEN = os.getenv('PISOCBOT_TOKEN')


def hello_handler(update, context):
    print(dir(update))
    print(dir(context))
    # update.message.reply_text('Hello there!')


def run_production(updater):
    """Start the bot and use webhooks to receive updates

    This is more suitable for a production environment as it's much faster,
    but requires the machine running the bot to be exposed to the internet.
    """
    updater.start_webhook(
        listen='0.0.0.0',
        port=int(os.getenv('PORT')),
        url_path=TELEGRAM_API_TOKEN)
    updater.bot.setWebhook(
        'https://pisocbot.herokuapp.com/' + TELEGRAM_API_TOKEN)
    updater.idle()


def run_develop(updater):
    """Start the bot and use polling to receive updates

    This is more suitable for a development environment because it doesn't
    require an externally exposed machine, but it is MUCH slower.
    """
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    updater = ext.Updater(token=TELEGRAM_API_TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(ext.CommandHandler('hello', hello_handler))

    environment = os.getenv('PISOCBOT_ENVIRONMENT')
    if environment == 'prod':
        run_production(updater)
    elif environment == 'dev':
        run_develop(updater)
    else:
        raise ValueError(
            f'Environment variable not set correctly - "{environment}"')
