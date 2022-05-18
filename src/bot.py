import os

import telebot
from loguru import logger
from telebot import types
import emoji

from src.constants import keyboards
from src.utils.io import write_json


class Bot:
    """ 
    
    """
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(os.environ['mbot_token'])
        self.echo_all = self.bot.message_handler(
            func=lambda message: True, content_types=['text'])(self.echo_all)
        
    def run(self) -> None:
        logger.info("Bot is running...")
        self.bot.infinity_polling()
      
    
    def echo_all(self, message):
        # write_json(message.json, 'message.json')
        # self.bot.reply_to(message, message.text)
        print(emoji.demojize(message.text))
        self.bot.send_message(
            message.chat.id, message.text, reply_markup=keyboards.main)
    
    
if __name__=='__main__':
    logger.info('bot started')
    bot = Bot()
    bot.run()
