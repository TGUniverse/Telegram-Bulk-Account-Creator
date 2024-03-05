import configparser
import sys
import csv
import colorama
import subprocess, requests, time, os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

bluec = Style.BRIGHT + Fore.BLUE
redc = Style.BRIGHT + Fore.RED
greenc = Style.BRIGHT + Fore.GREEN
yellowc = Style.BRIGHT + Fore.YELLOW
whitec = Style.BRIGHT + Fore.WHITE
magentac = Style.BRIGHT + Fore.MAGENTA
cyanc = Style.BRIGHT + Fore.CYAN


print()
print(f"{bluec}[*] Telegram bulk account creator ")
print()
print(f"{greenc}[*] www.HamzaXpro.com")
print()
print(f"{cyanc}[*] Contact : https://www.hamzaxpro.com/contact")
print()
a=input("[*] Press any key to exit...")
