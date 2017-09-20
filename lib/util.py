import json

from telegram import ParseMode, Message
from functools import wraps
from . import imguploader, database
from config import botconfig

#process_message util
def process_message(bot, update):
    message = update.message
    try:
        if message.photo or message.sticker or "image" in message.document.mime_type or "video/mp4" in message.document.mime_type:
            upload_with_msg(bot, update, message)
    except:
        update.effective_message.reply_text(reply_to_message_id=message.message_id, text="An error has occurred")
    #else:
        #send_img_msg(update)
 

# function to upload img and edit reply with link
def upload_with_msg(bot, update, message):
    try:
        file = image = link = None
        limit = False
        text = "Image is uploading..."
        file = message
        if file.photo:
            image = bot.getFile(file.photo[len(file.photo)-1].file_id)
            if file.photo[len(file.photo)-1].file_size > 10000000:
                text = "File size is more than 10MB"
                limit = True
        elif file.sticker: 
            image = bot.getFile(file.sticker.file_id)
            if file.sticker.file_size > 10000000:
                text = "File size is more than 10MB"
                limit = True
        else:
            image = bot.getFile(file.document.file_id)
            if file.document.file_size > 10000000:
                text = "File size is more than 10MB"
                limit = True
        reply =  update.effective_message.reply_text(reply_to_message_id=message.message_id, text=text)
        if not limit:
            link = imguploader.upload_imgur(image)
            bot.edit_message_text(text=link, chat_id=reply.chat_id, message_id=reply.message_id, disable_web_page_preview=bool(True))
            database.insert_stats(file.chat.id, file.chat.username, image.file_id, image.file_path, link)
    except:
        update.effective_message.reply_text(reply_to_message_id=message.message_id, text="An error has occurred")


# funtion that declare invalid command
def invalid_command(bot, update):
    text = "This command is only for admins"
    update.message.reply_text(text=text, quote=True)

# function to define if command is only for admins
def only_admin(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        if update.message.from_user.id not in botconfig.admins:
            invalid_command(bot, update, *args, **kwargs)
            return
        return func(bot, update, *args, **kwargs)
    return wrapped
