print("################################################################################")
print("################################################################################")
print("################################################################################")
print("################################################################################")
import shutil
import glob
import os 
         
a= "C:\\Program Files\\PostgreSQL\\14\\data\\log"
path= a+'\\NCCS_FORWARDER'
print(path)
print("################################################################################")

###################################################################################################################
#E2=========================================Storing all .log files Started=========================================#      
files = glob.glob("*.log")
print(files)
#E2=========================================Storing all .log files COMPLETED=========================================#      
###################################################################################################################
#E3=========================================Renaming all .log files Started=========================================#      
for x in files:
    print(x)
    source = a+"\\"+x
    print("=================================")
    print("=================================")
    print(source)
    target = path+'\Monday_'+x
    print("TARGET", target)
    shutil.copy(source, target)
#E3=========================================Renaming all .log files COMPLETED=========================================#      


src= a+"\postgresql.py"
src1= a+"\SJA_Log.py"
try:
    shutil.move(src, path)
    shutil.move(src1, path)
    print("Try")
    import pyautogui as ppa
    import time
    with ppa.hold('win'):
            ppa.press('r')
    ppa.write('C:\Windows\System32\cmd.exe')
    ppa.press('enter')
    time.sleep(1)
    ppa.write("cd C:\\Program Files\\PostgreSQL\\14\\data\log\\NCCS_FORWARDER")
    ppa.press('enter')
    ppa.write('python SJA_Log.py')
    ppa.press('enter')
    time.sleep(9)
    with ppa.hold('alt'):
        ppa.press('f4')
except:
    print("Except")
    import pyautogui as ppa
    import time
    with ppa.hold('win'):
            ppa.press('r')
    ppa.write('C:\Windows\System32\cmd.exe')
    ppa.press('enter')
    time.sleep(1)
    ppa.write("cd C:\\Program Files\\PostgreSQL\\14\\data\log\\NCCS_FORWARDER")
    ppa.press('enter')
    ppa.write('python SJA_Log.py')
    ppa.press('enter')
    time.sleep(9)
    with ppa.hold('alt'):
        ppa.press('f4')
    
    
