import streamlit as st
import os
import shutil
import glob


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('WhatsApp Image 2022-09-15 at 12.49.53 PM.jpeg')  





st.write("""# NCCS LOG FORWARDER
Make it *Simple* and *Easy*""")


ppath = st.text_input('kindly enter the path to PostgreSQl log file')
st.write('The current path to PostgreSQl log folder is : ', ppath)

psql = st.button("PostgreSQL")

if psql:
    src= os.getcwd()+"\postgresql.py"
    src1= os.getcwd()+"\SJA_Log.py"
    src2= os.getcwd()+"\Task2_Renaming.py"
    try:
      print("====================================TRY    START=============================")
      shutil.move(src, ppath)
      shutil.move(src1, ppath)
      shutil.move(src2, ppath)
      print("Try")

      import pyautogui as ppa
      import time
      with ppa.hold('win'):
              ppa.press('r')
      ppa.write('C:\Windows\System32\cmd.exe')
      ppa.press('enter')
      time.sleep(1)
      ppa.write('cd C:\\Program Files\\PostgreSQL\\14\data\\log')
      ppa.press('enter')
      ppa.write('python T2auto.py')
      ppa.press('enter')
      time.sleep(2)


      print("====================================TRY    COMPLETED=============================")

#E=========================================EXCEPT Started=========================================#      
    except:
      print("====================================EXCEPT    START=============================")
#E1=========================================Creation of Directory Started=========================================#
      directory = "NCCS_FORWARDER"
      path = os.path.join(ppath, directory) 
      os.mkdir(path) 
      print("Directory '% s' created" % directory)     
#E1=========================================Creation of Directory COMPLETED=========================================#
      import subprocess
      subprocess.call(ppath+'\T2auto.py', shell=True)
      os.system(ppath+'\T2auto.py')


      print("====================================EXCEPT    COMPLETED=============================")
#E=========================================EXCEPT COMPLETED=========================================#      


print("====================================COMPLETED=============================")
