# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
██╗ ██████╗     ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗    ██████╗  ██████╗ ████████╗
██║██╔════╝     ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██║██║  ███╗    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║       ██████╔╝██║   ██║   ██║   
██║██║   ██║    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║       ██╔══██╗██║   ██║   ██║   
██║╚██████╔╝    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║       ██████╔╝╚██████╔╝   ██║   
╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   """



def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.YELLOW + "      TheDbSearcher Project: https://discord.gg/JCsHZ43"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
