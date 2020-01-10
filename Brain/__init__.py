from telegram import ParseMode, ChatAction
from telegram.utils.helpers import escape_markdown

from Brain.Modules.help import get_help
from Brain.Modules.sample_module import sample_module
from Brain.Modules.strings import PM_START_TEXT, OWNER_ID


def start(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    if update.effective_chat.type == "private":
        if len(context.args) >= 1:
            if context.args[0].lower() == "help":
                get_help(update, context)
        else:
            first_name = update.effective_user.first_name
            reply = PM_START_TEXT.format(
                escape_markdown(first_name),
                escape_markdown(context.bot.first_name),
                escape_markdown(OWNER_ID))
            update.effective_message.reply_text(
                reply,
                parse_mode=ParseMode.MARKDOWN)

    else:
        update.effective_message.reply_text("Hey, {}!".format(escape_markdown(update.effective_user.first_name)))
