# **Imgur Plus Bot** #

[![Library](https://img.shields.io/badge/Python_Telegram_Bot-latest-af1a97.svg)](https://github.com/python-telegram-bot/python-telegram-bot)
[![Python](https://img.shields.io/badge/Python-3+-blue.svg)](https://www.python.org)
[![Pillow-lib](https://img.shields.io/badge/Pillow-GitHub-green.svg)](https://github.com/python-pillow/Pillow)
[![Request-lib](https://img.shields.io/badge/Requests-GitHub-green.svg)](https://github.com/requests/requests)
[![License](https://img.shields.io/badge/License-GNU%20GPL--3-yellow.svg)](https://github.com/DcSoK/ImgurPlus/blob/master/LICENSE)

# Summary

- Easy to setup, no compilation needed.
- Has many funtions that normal bots are not able to do, e.g., resize images.
- Simple and intuitive usage.
- Compatible with most of recent added telegram additions.
- Really fast and stable.


# Installation

Debian/Ubuntu and derivatives:
```bash
# Tested on Ubuntu 14.04 stable.
sudo apt-get install python3
sudo apt-get install -y python3-pip
sudo pip3 install python-telegram-bot --upgrade
sudo pip3 install requests
sudo pip3 install Pillow

# If you have errors installing Pillow 
sudo apt-get install python3-dev
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```
---------------------------------

Windows :
```bash
# Tested on Windows 10.
Download and install the newest version of python 3.X.X -> https://www.python.org/downloads/
pip install python-telegram-bot --upgrade
pip install requests
pip install Pillow
```
---------------------------------

Configure the bot:
```bash
# Edit config file config/botconfig.py.
# the token of the bot you get from t.me/botfather (type: str)
bot_token = "yourtoken"
# db info (Host, User, Password, Databse name) (type: str)
# not implemented yet
db_host = "your db host"
db_user = "your db user"
db_pass = "your db password" #encrypted password (not implemented)
db_name = "your db name"
# a python list containing the telegram ids of the admins of the bot (type: ids are long?)
admins = [133337, 133338]
# imgur api info (api_key, client_id)
api_imgur = "your api id"
clientid_imgur = "your client id"
```
---------------------------------

After installing the dependencies and editing the config, lets start the bot:
```bash
 #In Ubuntu
 git clone git@github.com:DcSoK/ImgurPlus.git
 cd imgurplus
 chmod +x bot.py
 python3 bot.py
 #In Windows
 git clone git@github.com:DcSoK/ImgurPlus.git
 cd imgurplus
 python bot.py
```
