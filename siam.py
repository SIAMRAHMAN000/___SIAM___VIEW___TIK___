from tls_client     import Session
from re             import findall
from PIL            import Image
from io             import BytesIO
from requests       import get
from urllib.parse   import unquote
from base64         import b64decode
from time           import sleep, time
from colorama       import Fore, init; init()
from datetime       import datetime
from json           import load
from hashlib        import sha256
from random         import randrange
import os
import webbrowser
import time
import random
import sys
import time


# color
# Color Value
blueVal = "94m"
redVal = "91m"
greenVal = "32m"
whiteVal = "97m"
yellowVal = "93m"
cyanVal = "96m"
# normal
normal = "\33["
# Bold
bold = "\033[1;"
# italic
italic = "\x1B[3m"
# Color Normal
blue = normal + blueVal  # Blue Color Normal
red = normal + redVal  # Red Color Normal
green = normal + greenVal  # Green Color Normal
white = normal + whiteVal  # white Color Normal
yellow = normal + yellowVal  # yellow Color Normal
cyan = normal + cyanVal  # Cyan Color Normal
# Color Bold
blueBold = bold + blueVal  # Blue Color Bold
redBold = bold + redVal  # Red Color Bold
greenBold = bold + greenVal  # Green Color Bold
whiteBold = bold + whiteVal  # white Color Bold
yellowBold = bold + yellowVal  # yellow Color Bold
cyanBold = bold + cyanVal  # Cyan Color Bold
def printchar(w, t):  # w=word and t =time
    for word in w + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(t)

# LOGO CLR 
ssl = ["\033[1;92m"]
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def fb():
    if os.name == 'nt':
        webbrowser.open('https://www.facebook.com/skillsiam1245/')
    else:
        os.system('xdg-open https://www.facebook.com/skillsiam1245/')
def github():
    if os.name == 'nt':
        webbrowser.open('https://github.com/SIAMRAHMAN000/')
    else:
        os.system('xdg-open https://github.com/SIAMRAHMAN000/')
def chat():
    if os.name == 'nt':
        webbrowser.open('https://m.me/skillsiam1245')
    else:
        os.system('xdg-open https://m.me/skillsiam1245')
def insta():
    if os.name == 'nt':
        webbrowser.open('https://www.instagram.com/skillsiam/')
    else:
        os.system('xdg-open https://www.instagram.comskillsiam/')
# IF YOU CHANGE THIS LOGO TOOL WAS NOT WORKING ANY MORE :D
logo = f'''{green}
  _____   _____              __  __  
 / ____| |_   _|     /\     |  \/  | 
| (___     | |      /  \    | \  / | 
 \___ \    | |     / /\ \   | |\/| | 
 ____) |  _| |_   / ____ \  | |  | | 
|_____/  |_____| /_/    \_\ |_|  |_| 
                                    
                                '''
print(logo)
def fmt(string) -> str:
    return f"{Fore.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {Fore.BLUE}INFO {Fore.MAGENTA}__SIAM__ -> {Fore.RESET}{string}"

class Client:
    def session() -> Session:
        return Session(client_identifier='chrome_108')
    
    def headers(extra: dict = {}) -> dict:
        return {
            **extra,
            "host"              : "zefoy.com",
            "connection"        : "keep-alive",
            "sec-ch-ua"         : "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
            "accept"            : "*/*",
            "x-requested-with"  : "XMLHttpRequest",
            "sec-ch-ua-mobile"  : "?0",
            "user-agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\"",
            "origin"            : "https://zefoy.com",
            "sec-fetch-site"    : "same-origin",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-dest"    : "empty",
            "accept-encoding"   : "gzip, deflate, br",
            "accept-language"   : "en-US,en;q=0.9",
        }

class Captcha:
    def __init__(this, client: Session) -> None:
        this.client = client
    
    def solve(this) -> None:
        try:
            html           = str(this.client.get('https://zefoy.com', headers = Client.headers()).text).replace('&amp;', '&')
            captcha_token  = findall(r'<input type="hidden" name="(.*)">', html)[0]
            captcha_url    = findall(r'img src="([^"]*)"', html)[0]
            banner()
            print(fmt(f'captcha_token: {captcha_token}'))
            print(fmt(f'captcha_url: {captcha_url}'))
            
            captcha_image  = get('https://zefoy.com' + captcha_url, headers = Client.headers(), cookies=this.client.cookies.get_dict()).content;
            image          = Image.open(BytesIO(captcha_image));image.show()
            
            captcha_answer = input('solve captcha: ')
            
            response = this.client.post('https://zefoy.com', headers = Client.headers({"content-type": "application/x-www-form-urlencoded"}), data = {
                    "captcha_secure": captcha_answer,
                    captcha_token   : ""
            })
            
            key_1 = findall('(?<=")[a-z0-9]{16}', response.text)[0]
            
            print(fmt(f'key_1: {key_1}'))
            
            return key_1
            
        except Exception as e:
            print(fmt(f'Failed to solve captcha You may have blocked you) [{e}]'))
            return
if sha256(logo.encode("utf-8")).hexdigest() != "09c46b57153429172097eb7810d33e2fdb86da6d3cd9edf8636c195a83318d18":
    printchar(f'    {redBold}[!] YOU HAVE BEEN MODIFYED MY LOGO. {greenBold}PLEASE CONNECT WITH {cyanBold}SIAM', 0.1)
    insta()
    exit()
class SIAM:
    def __init__(this, client: Session) -> None:
        this.client = client
        this.key = Captcha(client).solve()
        this.config = load(open('config.json', 'r'))

    def decode(this, text: str) -> str:
        return b64decode(unquote(text[::-1])).decode()
    
    def send(this, token: str, aweme_id: str) -> None:
        try:
            payload = f"--siam\r\nContent-Disposition: form-data; name=\"{token}\"\r\n\r\n{aweme_id}\r\n--siam--\r\n"
            response = this.decode(this.client.post("https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V", 
                data = payload, headers = Client.headers({"content-type": "multipart/form-data; boundary=siam",})).text.encode())
            
            if 'views sent' in response: 
                print(fmt(f'views sent to {aweme_id}'))
            elif '100 views sent' in response: 
                print(fmt(f'views sent to {aweme_id}'))
            elif '500 views sent' in response: 
                print(fmt(f'views sent to {aweme_id}'))
            elif '1000 views sent' in response: 
                print(fmt(f'views sent to {aweme_id}'))
            elif '1100 views sent' in response: 
                print(fmt(f'views sent to {aweme_id}'))
                
            else:
                print(fmt(f'Failed to send views to {aweme_id}'))

        except Exception as e:
            print(fmt(f'Failed to send views [{e}]'))
    
    def search(this, link: str) -> None:
        try:

            payload = f"--siam\r\nContent-Disposition: form-data; name=\"{this.key}\"\r\n\r\n{link}\r\n--siam--\r\n"
            response = this.decode(this.client.post("https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V", 
                data = payload, headers = Client.headers({"content-type": "multipart/form-data; boundary=siam",})).text.encode())
            
            if 'comviews' in response:
                token, aweme_id = findall(r'name="(.*)" value="(.*)" hidden', response)[0]
                print(fmt(f'sending to: {aweme_id} | key_2: {token}'))
    
                sleep(3); this.send(token, aweme_id)
                
            else:

                timer = findall(r'ltm=(\d*);', response)[0]
                if int(timer) == 0:
                    return

                print(fmt(f'time to sleep: {timer}   '),  end="\r")

                start = time()
                while time() < start + int(timer):

                    print(fmt(f'time to sleep: {round((start + int(timer)) - time())}   '),  end="\r")
                    sleep(1)
                    
                print(fmt(f'sending views...                '),  end="\r")

        except Exception as e:
            print(fmt(f'Failed to search link [{e}]'))
            print(fmt(response))
            return
    
    def mainloop(this) -> None:
        while True:
            this.search(this.config['link'])
            sleep(5)

if __name__ == '__main__':
    client = Client.session()
    siam  = SIAM(client).mainloop()
