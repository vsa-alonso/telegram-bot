# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:34:17 2019

@author: valonso.iphac
"""
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def woof(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id = chat_id, text = 'woof woof')
    bot.sendMessage(chat_id = chat_id, text = 'Im a good boy')


def main():
    # Crio uma variável da classe Updater
    updater = Updater('947357624:AAFI-ViIJ3G6E6m6600CnLOt83Yi0WSsvfA')
    updater.dispatcher.add_handler(CommandHandler('bop',bop))
    updater.dispatcher.add_handler(CommandHandler('auuu', woof))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()