#---==== Horder ====---

#creator: snxx (snxx-lppxx)
#blog: https://t.me/BlogSelfMade
#git: https://github.com/snxx-lppxx

#----====----====----====----====----


#----===Import mudules===----

from telegram import Update		
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import asyncio

#----===----===----===----===


#====---==== Modules ====---====

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#---====---====---====---====---

updater = Updater(
		token = 'TOKEN',
		use_context = True
	)

dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text='i++')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()