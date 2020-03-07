from dotenv import load_dotenv
load_dotenv()

import os
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.kogan.com/nz/'
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

items = [
    'buy/kogan-35-curved-219-ultrawide-75hz-freesync-gaming-monitor-b/',
    'buy/kogan-full-rgb-mechanical-keyboard-brown-switch/'
]

def main(event={}, context={}):
    for item in items:
        url = BASE_URL + item
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        name = soup.select_one('h1[itemprop="name"]').get_text()
        price = soup.select_one('h3[itemprop="price"]')['content']

        data = {
            'chat_id': CHAT_ID,
            'text': f'*${price}*\n[{name}]({url})',
            'parse_mode': 'Markdown'
        }
        r = requests.post(TELEGRAM_API_SEND_MSG, data=data)

if __name__ == '__main__':
    main()