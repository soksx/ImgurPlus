__autor__ = "sokk"

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  
import logging

#files
from config import botconfig
from lib import util, commands 
#from lib import database 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def main():
    #  define the updater
    updater = Updater(token=botconfig.bot_token)
    
    # define the dispatcher
    dp = updater.dispatcher

    # messages
    dp.add_handler(MessageHandler(~Filters.command, util.process_message, edited_updates=True))
    dp.add_handler(CommandHandler(('start'), commands.help_command))
    dp.add_handler(CommandHandler(('stats'), commands.stats_command))
    # handle errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()