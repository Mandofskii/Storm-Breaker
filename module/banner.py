import os
from subprocess import Popen
from colorama import Fore
import time


def banner():
    os.system("clear")
    print("")
    Popen('neofetch')
    time.sleep(2)

def print_and_sleep(*objects, seconds=0.1):
    time.sleep(seconds)
    print(objects)
   
def show_menu():
    print_and_sleep(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
    print_and_sleep(Fore.RED+" [0]"+Fore.WHITE+" Get Normal Data "+Fore.YELLOW+"[Without Any Permissions]\n")
    print_and_sleep(Fore.RED+" [1]"+Fore.WHITE+" Get Location "+Fore.GREEN+"[SMARTPHONES]\n")
    print_and_sleep(Fore.RED+" [2]"+Fore.WHITE+" Access Webcam\n") 
    print_and_sleep(Fore.RED+" [3]"+Fore.WHITE+" Access Microphone \n")
    print_and_sleep(Fore.RED+" [4]"+Fore.WHITE+" Exit . . .\n")
