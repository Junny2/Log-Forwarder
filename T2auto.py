import pyautogui as ppa
import time



with ppa.hold('win'):
        ppa.press('r')
ppa.write('C:\Windows\System32\cmd.exe')
ppa.press('enter')
time.sleep(1)
ppa.write('cd C:\\Program Files\\PostgreSQL\\14\data\\log')
ppa.press('enter')
ppa.write('python Task2_Renaming.py')
ppa.press('enter')
time.sleep(2)

