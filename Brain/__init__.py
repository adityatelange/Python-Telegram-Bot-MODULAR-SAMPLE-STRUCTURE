from telegram.utils.helpers import escape_markdown
from Brain.Modules.strings import *
from Brain.Modules.sample_module import *
from Brain.Modules.help import *


@run_async
def start(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat
    logger.info("into start")
    bot.send_chat_action(chat_id=chat.id, action=ChatAction.TYPING)
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                get_help(bot=bot, update=update, args=[])
        else:
            first_name = update.effective_user.first_name
            reply = PM_START_TEXT.format(
                escape_markdown(first_name),
                escape_markdown(bot.first_name),
                escape_markdown(OWNER_ID))
            update.effective_message.reply_text(
                reply,
                parse_mode=ParseMode.MARKDOWN)

    else:
        update.effective_message.reply_text("Hey, {}!".format(escape_markdown(update.effective_user.first_name)))
