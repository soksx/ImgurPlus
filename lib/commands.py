from telegram import ParseMode
from telegram import MessageEntity
from telegram import ParseMode
from . import database
from . import keyboards
from . import util

def help_command(bot, update):
    keyboard = keyboards.github_link_kb()
    text = "<b>Welcome!</b>\n\nUse this bot to upload images, stickers and gifs directly to Imgur.\n\n<b>•</b> Send any image as documment or just as simple image and the bot will upload it to imgur, giving the direct link to the image. <i>The format of the image depends from the original file.</i>\n\n<b>•</b> Send any Telegram gif and the bot will convert it and upload to imgur, giving the direct link. <i>The gif format always will be .gif.</i>\n\n<b>•</b> Send any Telegram Sticker and the bot will upload it to imgur, giving the direct link. <i>The sticker format will be .png.</i>\n\n<b>•</b> <b>Important: the file limit is about 10 MB</b>"
    update.message.reply_text(text=text, parse_mode=ParseMode.HTML, reply_markup=keyboard)

def stats_command(bot, update):
    msgs = database.get_stats(update.message.chat_id)
    text = "<b>User Stats:</b>\n\n<b>•</b> Total uploads: " + str(msgs[0]) + "\n<b>•</b> Succesfully uploads: " + str(msgs[1])
    update.message.reply_text(text=text, parse_mode=ParseMode.HTML)

@util.only_admin
def global_stats_command(bot, update):
    msgs = database.get_global_stats(update.message.chat_id)
    text = "<b>Global Stats:</b>\n\n<b>•</b> Total uploads: " + str(msgs[0]) + "\n<b>•</b> Succesfully uploads: " + str(msgs[1])
    update.message.reply_text(text=text, parse_mode=ParseMode.HTML)