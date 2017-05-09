#! python3
#Computac GUI Testing
#Created by Curtis Cholon
#03/31/2017
#C:\Users\svc_aadevbot2\Documents\Python\Computac_GUI_Testing.py


"""GUI Testing - Computac navigation"""

from pywinauto.application import Application
import pyautogui
import time
import os

#open instance of Bluvista - Specialty
app = Application().start("C:\\Bluvista\\bluvista.exe /stp=specialty_550.stp")

time.sleep(5)

#login
login = input("Login")
password = input("Password")
pyautogui.typewrite(login,0.25)
pyautogui.typewrite('\n')
time.sleep(2)
pyautogui.typewrite(password,0.25)
pyautogui.typewrite('\n')
time.sleep(2)

#confirm login status'
welcome = ("C:\\Users\\svc_aadevbot2\\Documents\\Python\\Welcome_Taskbot3.png")
print(pyautogui.locateOnScreen(welcome))



