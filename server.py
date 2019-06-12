import logging
import os
import sys
import threading

from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

import Brain
from Brain.Utils.logger import initialize_logger

logger = logging.getLogger(__name__)


class Main:
    def __init__(self):
        threading.Thread(name='background', target=self.background).start()
        logger.info("Starting bot")
        self.mode = os.getenv("MODE")
        self.TOKEN = os.getenv("TOKEN")
        self.domain = os.getenv("DOMAIN")
        self.PORT = int(os.environ.get("PORT", "8443"))
        self.APP_NAME = os.environ.get("APP_NAME")
        self.updater = Updater(token=self.TOKEN)

        self.dispatcher = self.updater.dispatcher
        # run(updater)
        self.command()
        self.run(self.updater)

    @staticmethod
    def background():
        # Initialize Logger
        initialize_logger(r'.data')

    def run(self, updater):
        if self.mode == "dev":
            logger.info("Starting Polling Method.")
            updater.start_polling(timeout=15, read_latency=4)
        elif self.mode == "prod":
            logger.info("Starting Webhook")

            updater.start_webhook(listen="0.0.0.0",
                                  port=self.PORT,
                                  url_path=self.TOKEN)
            updater.bot.set_webhook("https://{}.{}/{}".format(self.APP_NAME, self.domain, self.TOKEN))

            logger.info("Webhook set on https://{}.{}/{}".format(self.APP_NAME, self.domain, self.TOKEN))
        else:
            logger.error("No MODE specified!")
            sys.exit(1)
        updater.idle()

    def command(self):
        # define handlers

        # simple handlers
        start_handler = CommandHandler("start", callback=Brain.start, pass_args=True)
        help_handler = CommandHandler("help", callback=Brain.get_help, pass_args=True)
        sample_module_handler = CommandHandler("sample", callback=Brain.sample_module, pass_args=False)

        # callback handlers
        help_callback_handler = CallbackQueryHandler(callback=Brain.help_button, pattern=r"help_")

        # set dispatchers
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(sample_module_handler)
        self.dispatcher.add_handler(help_callback_handler)


if __name__ == '__main__':
    Main()
