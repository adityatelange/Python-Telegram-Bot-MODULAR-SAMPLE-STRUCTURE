import re
from typing import List

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Update, Bot
from telegram.error import BadRequest
from telegram.ext.dispatcher import run_async
from telegram.chataction import ChatAction
from Brain import Utils
from Brain.Modules.strings import *
from server import logger


@run_async
def help_button(bot: Bot, update: Update):
    query = update.callback_query
    suggestion_match = re.match(r"help_action=(.+?)", query.data)
    back_button = re.match(r"help_back", query.data)
    try:
        if suggestion_match:
            text = query.data.split('=', 1)[1]
            text = text.split(' ')
            get_help(bot, update, args=text)
        elif back_button:
            get_help(bot, update, args=[])

        # ensure no spinning white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as e:
        if e.message == "Message is not modified":
            pass
        elif e.message == "Query_id_invalid":
            pass
        elif e.message == "Message can't be deleted":
            pass
        else:
            logger.exception("Exception in help buttons. %s", str(query.data))


# do not async
def send_help(update, text, keyboard=None):
    logger.info("into send_help")
    if not keyboard:
        # add keyboard here
        # keyboard = None
        pass
    update.effective_message.reply_text(text=text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)


@run_async
def get_help(bot: Bot, update: Update, args: List[str]):
    logger.info("into get_help")
    chat = update.effective_chat

    logger.info(args)
    bot.send_chat_action(chat_id=chat.id, action=ChatAction.TYPING)
    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        send_help(update, "Contact me in PM to get the list of possible commands.", InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text="Help",
                                                                       url="t.me/{}?start=help".format(
                                                                           bot.username))]]))
        return
    elif len(args) >= 1 and any(args[0].lower() == x for x in HELPER_SCRIPTS):
        print(args)
        print(HELPER_SCRIPTS)
        module = args[0].lower()
        text = "Here is the available help for the *{}* module:\n{}".format(module,HELPER_SCRIPTS[module])
        send_help(update, text, InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="help_back")]]))

    else:
        button_list = []
        for module in HELPER_SCRIPTS:
            button_list.append(
                InlineKeyboardButton(text="/{}".format(module),
                                     callback_data="help_action={}".format(module), ))

        reply_markup_keyboard = InlineKeyboardMarkup(Utils.build_menu(button_list, n_cols=2))

        send_help(
            update=update,
            text=HELP_STRINGS.format(
                bot.first_name, ),
            keyboard=reply_markup_keyboard
        )
