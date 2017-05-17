from pywinauto.application import Application
import time
import subprocess
import pyperclip

#computac session file
stp = "/stp=marcatl.stp"

#open computac session
subprocess.Popen('C:\\bluvista\\bluvista.exe %s' %stp)
time.sleep(4)

#connect to active session
app = Application().Connect(title=u'BluVista: - [IBM3151A - MarcAtl.stp]', class_name='MDIframeCLBV')
ctac = app.MDIframeCLBV
#app = Application().start("C:\\bluvista\\bluvista.exe %s" %stp)

app.windows()
ctac.wait('ready')

#copy screen contents to clipboard
menu_item = ctac.MenuItem(u'&Edit->Copy &All')
menu_item.Click()

#print clipboard contents
#print(pyperclip.paste())

screen_txt = pyperclip.paste()

while "login" not in screen_txt.lower():
	time.sleep(1)
	menu_item = ctac.MenuItem(u'&Edit->Copy &All')
	menu_item.Click()
	
ctac.type_keys("taskbot3")
ctac.type_keys("{ENTER}")
time.sleep(1)
ctac.type_keys("alsbridge")
ctac.type_keys("{ENTER}")



#ctac.minimize()


#app.kill()