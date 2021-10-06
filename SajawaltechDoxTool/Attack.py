'''
==========SAJAWAL TECH CHANNEL==========
This script is only for educational purposes
I won't be responsible for any misuse of the tool
---Code With Credits---
For any issues visit MY YOUTUBE CHANNEL : https://www.youtube.com/channel/UCG7N0eluangTt81H5-73v1A
|Author: SAJAWAL TECH CHANNEL: https://www.youtube.com/channel/UCG7N0eluangTt81H5-73v1A ]
====================================================
'''

from colorama import Fore, Style, init
import os
import sys
from OXlib import NameDox, PhoneDox, Ipdox, Maildox, UserDox, g_search, Shodan_search
# import shodan
b = Style.BRIGHT
g = b + Fore.GREEN
r = b + Fore.RED
w = b + Fore.WHITE
cy = b + Fore.CYAN
ncy = Fore.CYAN
dcy = Style.DIM + Fore.CYAN
#o = '\033[1;33m'
rs = Style.RESET_ALL
init()
plus = g + '[' + w + '+' + g + ']'
warn = g + '[' + r + '!' + g + ']'
info = g + '[' + w + 'i' + g + ']'
inp = g + '[' + w + '~' + g + ']'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print(f'''
{r}██████{w}██████{g}█████{g}{r}██████{w}██████{g}   SAJAWAL TECH CHANNEL   {r}██████{w}██████{g}█████{g}{r}██████{w}██████{g}{rs}

Coded By: {w}Sajawal Tech Channel : https://www.youtube.com/channel/UCG7N0eluangTt81H5-73v1A 
{rs} and Works on Android[Termux] | Linux | Windows
    Warning : This tool is for educational purposes only. Developer will not be reponsible for any misuse of the tool or any illegal activity by this Tool :) ''')



def helpMenu():
    #displays the help menu
    print(f'''
{g}Join our YOUTUBE Channel {w} Sajawal Tech Channel : https://www.youtube.com/channel/UCG7N0eluangTt81H5-73v1A
{g}Latest tech news, hacking, cracking, etc. 
{g}Problems/Suggestions: 
{g}Visit MY YOUTUBE CHANNEL ( Sajawal Tech Channel : https://www.youtube.com/channel/UCG7N0eluangTt81H5-73v1A )

{w}Usage:

    {g}python garuda.py [--help][--name][--ip]
                {g}[--mail][--phone][--user][--shodan]

{w}Arguments:
    
    {g}--help     : {cy}Display this menu
    {g}--mail     : {cy}E-Mail Doxing
    {g}--phone    : {cy}Phone number Doxing
    {g}--user     : {cy}Username Doxing
    {g}--shodan   : {cy}Fetches Shodan search results
    {g}--google   : {cy}Perform Google search{rs}
    {g}--name     : {cy}Name Doxing
    {g}--ip       : {cy}IP Doxing
    
    ''')
'''
Code Improvements/Suggestions are welcome
Open an issue YOUTUBE COMMENT for suggestions/issues 
Sajawal Tech Channel : https://www.youtube.com/channel/UCG7N0eluangTt81H5-73v1A
'''
if len(sys.argv) != 2:
    print(f'{warn}{r} Error: Missing argument{rs}')
    helpMenu()
    sys.exit()
arg = str(sys.argv[1])
if arg == '--help':
    helpMenu()
elif arg == '--name':
    first_name = str(input(f'{inp}{cy} Enter First Name: {r}'))
    last_name = str(input(f'{inp}{cy} Enter Last Name[If none press enter to skip]: {r}'))
    if last_name == '':
        namedoxer = NameDox(first_name)
        namedoxer.doxname()
    else:
        namedoxer = NameDox(first_name, last_name)
        namedoxer.doxname()
elif arg == '--ip':
    ip_addr = str(input(f'{inp}{cy} Enter IP Address: {r}'))
    ipdoxer = Ipdox(ip_addr)
    ipdoxer.start_Ip_doxing()
    print(f'{plus} Scan Complete')
elif arg == '--mail':
    mail = str(input(f'{inp}{cy} Enter E-Mail Address: {r}'))
    maildoxer = Maildox(mail)
    maildoxer.start_mail_dox()
    print(f'{plus} Scan Complete')
elif arg == '--phone':
    print(f'{info}{cy} Format: Country Code + Number')
    print(f'{info}{cy} Example: +19087654321')
    phone_number = str(input(f'{inp}{cy} Enter Phone Number: {r}'))
    phone_number = ''.join(phone_number.split())
    phonedox = PhoneDox(phone_number)
    print(f'{info}{cy} Fetching information for {w}{phone_number}')
    phonedox.simple_scan()
    phonedox.db_scan()
    print(f'{plus} Scan Complete')
elif arg ==  '--user':
    username = str(input(f'{inp}{cy} Enter Username{g}[Without @]{cy}: {r}'))
    username_doxxer = UserDox(username)
    username_doxxer.web_search()
    print(f'{plus} Scan Complete')
elif arg == '--shodan':
    prompt = str(input(f'{inp}{cy} Enter a query to search Shodan: {r}'))
    searcher = Shodan_search(prompt)
    searcher.start()
elif arg == '--google':
    q = str(input(f'{inp}{cy} Enter query to search{g}[Google]: {r}'))
    g_search(q)
else:
    print(f'{warn}{r} Error: Invalid argument')
    helpMenu()
