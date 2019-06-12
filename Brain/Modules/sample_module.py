from telegram import ParseMode
from telegram import Update, Bot
from telegram.chataction import ChatAction

from Brain.Modules.strings import *
from server import logger

sample_module_help = \
    """
        - /sample
    """
HELPER_SCRIPTS['sample'] = sample_module_help


def sample_module(bot: Bot, update: Update, ):
    chat = update.effective_chat

    bot.send_chat_action(chat_id=chat.id, action=ChatAction.TYPING)
    try:
        response = "This is a Sample module"

        update.effective_message.reply_text(text=response, parse_mode=ParseMode.MARKDOWN, reply_markup=None)
    except Exception as e:
        logger.exception(e)
