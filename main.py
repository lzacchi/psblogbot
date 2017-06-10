"""A script that fetches and displays Playstation Blog's latest news."""
from bs4 import BeautifulSoup
import config
import logging
import requests
from telegram import Bot
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = Bot(config.TOKEN)

r = requests.get("https://blog.us.playstation.com/")

data = r.text

soup = BeautifulSoup(data, "lxml")

featured_post = soup.find('div', {"class": "wrap-entry"})

bot.sendMessage(chat_id='@psblog_channel',
                text=featured_post.a.get('href'))

while True:
    candidate = requests.get('https://blog.us.playstation.com/')
    cnd_data = r.text
    cnd_soup = BeautifulSoup(cnd_data, "lxml")
    cnd_featured = cnd_soup.find('div', {"class": "wrap-entry"})
    if featured_post != cnd_featured:
        featured_post = cnd_featured
        bot.sendMessage(chat_id='@psblog_channel',
                        text=featured_post.a.get('href'))
    if candidate.status_code != 200:
        time.sleep(3600)
