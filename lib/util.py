import json

from telegram import ParseMode, Message, document, forcereply
#import database
from . import keyboards, imguploader

#process_message util
def process_message(bot, update):
    message = update.message
    if message.photo:
        select_res_msg(update)
    elif message.document:
        if "image" in message.document.mime_type:
            select_res_msg(update)
        else:
            send_img_msg(update)
    else:
        send_img_msg(update)

#querycallback util
def select_res(bot, update):
    query = update.callback_query
    bot.edit_message_text(text="Uploading image with %s as resolution..." % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id)
    if query.data != "custom":
        upload_img(query.message.reply_to_message, query.data, query, bot)

# function to select res
def select_res_msg(update):
    text = "Select your resolution: "
    keyboard = keyboards.defaul_res()
    update.effective_message.reply_text(reply_to_message_id=update.message.message_id, text=text, reply_markup=keyboard)

# function to send img
def send_img_msg(update):
    text = "Please send a photo to de bot"
    update.effective_message.reply_text(text=text)
	
# function to upload img and edit reply with link
def upload_img(file, res, query, bot):
    image = None
    if file.photo:
        image = bot.getFile(file.photo[len(file.photo)-1].file_id)
    else:
        image = bot.getFile(file.document.file_id)
    bot.edit_message_text(text=imguploader.upload_imgur(image, res), chat_id=query.message.chat_id, message_id=query.message.message_id, disable_web_page_preview=bool(True))

        
