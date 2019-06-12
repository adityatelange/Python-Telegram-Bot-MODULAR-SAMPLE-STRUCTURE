import os

OWNER_ID = os.getenv("OWNER_ID")
##################################################
HELP_STRINGS = """
Hii there! My name is *{}*.
I'm a bot .

*Main* commands available:
 - /start: start the bot
 - /help: send you this message.

And the following:
"""
###################################################
PM_START_TEXT = """Hello {}, my name is {}! If you have any questions on how to use me, read /help.
I'm a bot maintained by [this person](tg://user?id={}) ."""
##################################################
HELPER_SCRIPTS = {}
