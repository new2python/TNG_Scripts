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

#time.sleep(2)
print(ctac.WindowText())

#copy screen contents to clipboard
menu_item = ctac.MenuItem(u'&Edit->Copy &All')
menu_item.Click()

#print clipboard contents

print(pyperclip.paste())


ctac.minimize()


#app.kill()