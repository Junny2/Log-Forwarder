import pyautogui as ppa
import time



with ppa.hold('win'):
        ppa.press('r')
ppa.write('C:\Windows\System32\cmd.exe')
ppa.press('enter')
time.sleep(1)
ppa.write('cd C:\\Program Files\\PostgreSQL\\14\data\\log\\NCCS_FORWARDER')
ppa.press('enter')
ppa.write('python postgresql.py')
ppa.press('enter')
time.sleep(1)
ppa.write('shummi')
ppa.press('enter')
time.sleep(5)
with ppa.hold('alt'):
        ppa.press('f4')
