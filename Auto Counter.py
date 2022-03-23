import os
import pyperclip
import discord
import random
import re
from discord.ext import commands
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
from requests import get as r

def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
clear()

def main():
    token = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA+"ihebman" +
              Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+"Enter Token: " + Fore.WHITE+" ")

    headers = {'Authorization': token}
    y = r('https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers).json()
    try:
        if 'verify' in y['message'].lower():
            print(f'{Fore.MAGENTA}[{Fore.WHITE}Error{Fore.MAGENTA}]{Fore.WHITE}: Your account requires verification. Please try a different token.')
            sleep(4)
            main()

        if '401: Unauthorized' == y['message']:
            print(f'{Fore.MAGENTA} [{Fore.WHITE}Error{Fore.MAGENTA}]{Fore.WHITE}: Invalid token. Please try again')
            sleep(4)
            main()
    except:
        pass

    
    class bot(discord.Client):
        async def on_ready(self):
            os.system(
                f'title [AFK-CHECKER] │ Connected As: {self.user}')
            print(f"""
{Fore.MAGENTA}
{Fore.WHITE}                ██╗██╗  ██╗███████╗██████╗ 
{Fore.MAGENTA}                ██║██║  ██║██╔════╝██╔══██╗
{Fore.WHITE}                ██║███████║█████╗  ██████╔╝
{Fore.MAGENTA}                ██║██╔══██║██╔══╝  ██╔══██╗
{Fore.WHITE}                ██║██║  ██║███████╗██████╔╝
{Fore.MAGENTA}                ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝
{Fore.MAGENTA}              ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
{Fore.WHITE}              Dev: {Fore.MAGENTA}GodJustice/Iheb
{Fore.WHITE}                       Loading....
{Fore.MAGENTA}              ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
""")
            print(f"{Fore.MAGENTA}")
            progressbar = tqdm([2, 4, 6, 8, 10])
            for item in progressbar:
                sleep(0.1)
                progressbar.set_description(' Loading: ')

            clear()
            print(f"""
{Fore.MAGENTA}
{Fore.WHITE}                ██╗██╗  ██╗███████╗██████╗ 
{Fore.MAGENTA}                ██║██║  ██║██╔════╝██╔══██╗
{Fore.WHITE}                ██║███████║█████╗  ██████╔╝
{Fore.MAGENTA}                ██║██╔══██║██╔══╝  ██╔══██╗
{Fore.WHITE}                ██║██║  ██║███████╗██████╔╝
{Fore.MAGENTA}                ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝
{Fore.MAGENTA}              ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
{Fore.WHITE}                Dev: {Fore.MAGENTA}GodJustice/Iheb
{Fore.WHITE}               Trigger Word:{Fore.MAGENTA}['{Fore.WHITE}AFK{Fore.WHITE} CHECK{Fore.WHITE}{Fore.MAGENTA} @user{Fore.WHITE}{Fore.MAGENTA}']
{Fore.MAGENTA}              ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙

""")

        async def on_message(self, x):
            regex = re.findall(r'<@!?([0-9]+)>', x.content)
            if regex and 'afk check' in x.content.lower() and x.author == self.user:
                for i in range(1, 100001):
                    async with x.channel.typing():
                        await x.channel.send(i)


    bot = bot()
    bot.run(token, bot=False)

if __name__ == '__main__':
    main()