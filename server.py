import logging
import os
import sys
import threading

from telegram.ext import (CommandHandler, Updater, CallbackQueryHandler)

import Brain
import Brain.Modules.help
from Brain.Utils.logger import initialize_logger

logger = logging.getLogger(__name__)


class Main:
    def __init__(self):
        threading.Thread(name='background', target=self.background).start()
        logger.info("Starting bot")
        self.mode = os.getenv("MODE")
        self.TOKEN = os.getenv("TOKEN")
        self.APP_NAME = os.environ.get("APP_NAME")
        self.domain = os.getenv("DOMAIN")
        self.PORT = int(os.environ.get("PORT", "8443"))

        self.updater = Updater(token=self.TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

        threading.Thread(name='background', target=self.background).start()
        self.handlers()  # set handlers
        self.run(updater=self.updater)

    @staticmethod
    def background():
        # Initialize Logger
        initialize_logger(r'.data')

    def handlers(self):
        # define handlers

        # simple handlers
        start_handler = CommandHandler("start", callback=Brain.start, pass_args=True)
        help_handler = CommandHandler("help", callback=Brain.get_help, pass_args=True)
        sample_module_handler = CommandHandler("sample", callback=Brain.sample_module, pass_args=False)

        # callback handlers
        help_callback_handler = CallbackQueryHandler(callback=Brain.Modules.help.help_button, pattern=r"help_")

        # set dispatchers
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(sample_module_handler)
        self.dispatcher.add_handler(help_callback_handler)

    def run(self, updater):
        if self.mode == "dev":
            logger.info("Starting Polling Method.")
            updater.start_polling(timeout=15, read_latency=4)
        elif self.mode == "prod":
            webhook_url = "https://{}.{}/{}".format(self.APP_NAME, self.domain, self.TOKEN)
            self.updater.start_webhook(listen="0.0.0.0", port=self.PORT, url_path=self.TOKEN)
            self.updater.bot.set_webhook(webhook_url)

            logger.info("Webhook set on {}".format(webhook_url))
        else:
            logger.error("No MODE specified!")
            sys.exit(1)
        updater.idle()


if __name__ == '__main__':
    Main()
