from pywinauto.application import Application
import time

stp = "/stp=marcatl.stp"
app = Application().start("C:\\bluvista\\bluvista.exe %s" %stp)

app.windows()
app_window = app.Bluvista
app_window.wait('ready')

app_window.minimize()

app_window.print_control_identifiers()

app.kill()