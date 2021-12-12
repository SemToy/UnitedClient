import subprocess
import os
import getpass
import sys
from threading import Thread
import threading
import time
from colorama import Fore, Back

 #Функция экрана ввода номера телефона 
def main():
    os.chdir(UP)
    print('ver 0.1\n')
    #стоит создать переменные кода региона, номер без региона и полный номер(разные бомберы юзают разный формат ввода номера)
    num = input(Fore.BLACK + Back.GREEN + 'Введите номер -->' + Back.RESET + Fore.RESET)

def logo():
    os.system('CLS')
    print(" ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      ▄████▄   ██▓     ██▓▓█████  ███▄    █ ▄▄▄█████▓")
    print("▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ▀█  ▓██▒    ▓██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒")
    print("▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒   ▒▓█    ▄ ▒██░    ▒██▒▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░")
    print("▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     ▒▓▓▄ ▄██▒▒██░    ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ")
    print("░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒   ▒ ▓███▀ ░░██████▒░██░░▒████▒▒██░   ▓██░  ▒██▒ ░ ")
    print("░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ")
    print("▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░     ░  ▒   ░ ░ ▒  ░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░    ░    ")
    print(" ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░    ░          ░ ░    ▒ ░   ░      ░   ░ ░   ░      ")
    print(" ░          ░ ░         ░    ░         ░  ░   ░        ░ ░          ░  ░ ░     ░  ░         ░          ")
    print("      ░                           ░                    ░                                               ")


logo()
print(Fore.RED + 'Download Mode' + Fore.RESET)
time.sleep(2)
name = getpass.getuser()
#для windows установка проходит в корень D:\, с установкой на С:\ проблемы ввиде permission denied
if sys.platform == 'win32':
    UP = 'D:\\BomberClient/'
elif sys.platform == 'linux': 
    UP = '/home/'+ name +'/BomberClient'
if os.path.isdir(UP):
    logo()
    main()
    def bomb3r():
        #Функция запуска tbomb
        os.chdir(UP + 'tbomb')
        subprocess.call(f'', shell=True)

     
else:
    print('  \nПапки клиента не существует, создание папки и установка бомберов')
    time.sleep(5)
    os.mkdir(UP)
    os.chdir(UP)
    print('  \nЗагрузка бомберов...')
    subprocess.call('pip install tbomb', shell=True)
    print('Установлен tbomb')
    subprocess.call(f'git clone https://github.com/LimerBoy/Impulse', shell=True)
    os.chdir(UP + 'Impulse')
    subprocess.call(f'pip install -r requirements.txt', shell=True)
    print('Установлен Impulse')
    os.chdir(UP)
    subprocess.call(f'git clone https://github.com/Ivan-Hacker-700/SMS-Bomber-300-Free', shell=True)
    os.chdir(UP + 'SMS-Bomber-300-Free')
    subprocess.call(f'pip install -r requirements.txt', shell=True)
    os.chdir(UP)
    logo()
    main()










#ссылки на бомберы
    # subprocess.call(f'', shell=True)
    # https://github.com/yyasha/smsbomb
    # https://github.com/K1ngSoul/Parad1seBomb