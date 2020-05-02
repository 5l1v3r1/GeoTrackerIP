#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#MODULES

#External Modules
import itertools
import time
import os
import sys

#Internal Modules
from modules import logo

#COLORS

#Foreground
black = "\033[0;30m"
gray = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m" 
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

#Background
b_black = "\033[0;40m"
b_gray = "\033[1;40m"
b_red = "\033[1;41m"
b_green = "\033[1;42m"
b_yellow = "\033[1;43m"
b_blue = "\033[1;44m"
b_magenta = "\033[1;45m"
b_cyan = "\033[1;46m"
b_white = "\033[1;47m"

#CLEAN CONSOLE
def clean():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    else:
        pass
        
#PROCESS OF INSTALLING
def install():
    #Logo
    logo.logo()

    bucle = itertools.cycle("/-|-\|")
    for i in range(30):
        print("{}[{}*{}] {}Installing Modules...{}{}".format(cyan, white, cyan, green, next(bucle), white), end='\r')
        time.sleep(0.1) 
    print("")
    print("")
    os.system("python3 -m pip install requests")
    print("")
    print("                     {}>> Installation Complete <<{}".format(blue, white))
    print("")
    time.sleep(1)

#START
clean()
install()
