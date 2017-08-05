import json

from telegram import ParseMode, Message, document, forcereply
#import database
from . import keyboards, imguploader

#process_message util
def process_message(bot, update):
    message = update.message
    if message.photo or message.sticker or "image" in message.document.mime_type or "video/mp4" in message.document.mime_type:
        upload_with_msg(bot, update, message)
    #else:
        #send_img_msg(update)
 

 #querycallback util
def upload_with_msg(bot, update, message):
    text = "Image is uploading..."
    msg_reply =  update.effective_message.reply_text(reply_to_message_id=message.message_id, text=text)
    upload_img(message, bot, msg_reply)

# function to upload img and edit reply with link
def upload_img(file, bot, reply):
    image = link = None
    if file.photo:
        image = bot.getFile(file.photo[len(file.photo)-1].file_id)
    elif file.sticker: 
        image = bot.getFile(file.sticker.file_id)
    else:
        image = bot.getFile(file.document.file_id)
    bot.edit_message_text(text=imguploader.upload_imgur(image), chat_id=reply.chat_id, message_id=reply.message_id, disable_web_page_preview=bool(True))
