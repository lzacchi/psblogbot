"""A script that fetches and displays Playstation Blog's latest news."""
import config
from digrss import Digrss
import logging
from telegram import Bot


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = Bot(config.TOKEN)

with Digrss(feeds_file_path='feeds.json', interval=config.INTERVAL,
            fetch_old=True) as file:
    for entry in file:
        msg = (f'<b>{entry.title}</b>\n\n{entry.summary}\n'
               f'<a href="{entry.link}">{config.MORE}</a>')
        msg = msg.replace('<br>', '\n')

        bot.sendMessage(chat_id='@psblog_channel', text=msg, parse_mode="HTML",
                        disable_web_page_preview=True)
