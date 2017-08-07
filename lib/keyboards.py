from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def defaul_res():
    button0 = InlineKeyboardButton(text="48x48", callback_data="48x48")
    button1 = InlineKeyboardButton(text="72x72", callback_data="72x72")
    button2 = InlineKeyboardButton(text="96x96", callback_data="96x96")
    button3 = InlineKeyboardButton(text="144x144", callback_data="144x144")
    button4 = InlineKeyboardButton(text="Custom resolution", callback_data="custom")
    button5 = InlineKeyboardButton(text="Default resolution", callback_data="default")
    buttons_list = [[button0, button1, button2, button3], [button5]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard

def github_link_kb():
    button0 = InlineKeyboardButton(text="Source code", url="https://github.com/DcSoK/ImgurPlus")
    buttons_list = [[button0]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard
