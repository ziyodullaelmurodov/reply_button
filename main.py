import requests
import json


TOKEN = '7794338117:AAFD94DHCZatfpH6wFJToH48m0ve7s_W3TU'
CHAT_ID = '6521343766'

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    keyboard_buttons = [
        [{'text': 'Tugma 1'}, {'text': 'Tugma 2'}, ],  
        [{'text': 'Tugma 7'}]   
    ]


    reply_keyboard_markup = {
        'keyboard': keyboard_buttons,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': json.dumps(reply_keyboard_markup), 
    }
    
    r = requests.get(url, params=params)
    return r.json()

TEXT = """
Simple TEXT\\n
*Bold TEXT*\\n
_Italic TEXT_\\n
__underline TEXT__\\n
||spoiler Heading Text||
"""

send_message(TEXT, CHAT_ID)
