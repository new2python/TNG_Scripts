#! python3
#Refresh data connection in Excel workbook
#Created by Curtis Cholon
#04/19/2017

"""Opens and updates any data connections contained within a specified workbook"""

import win32com.client
import os

def close_excel_by_force(xl):
	import win32process
	import win32gui
	import win32api
	import win32con
	import time
	
	#Get the window's process id's
	hwnd = xl.Hwnd
	t,p = win32process.GetWindowThreadProcessId(hwnd)
	#Ask window nicely to close
	win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
	#Allow some time for the app to close
	time.sleep(3)
	#If the application didn't close, force close
	try:
		handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p)
		if handle:
			win32api.TerminateProcess(handle,0)
			win32api.CloseHandle(handle)
	except:
		pass


filename = "L:\\Rite_Aid_Credit_Circulation\\Rite_Aid_Store_List.xlsx"
xl = win32com.client.DispatchEx("Excel.Application")
wb = xl.workbooks.open(filename)

#makes workbook visible, currently disabeled because we're not 
#editing any information in the workbook
xl.Visible = False
xl.DisplayAlerts = False

wb.RefreshAll()
wb.Save()
xl.Quit()
xl.Application.Quit()
close_excel_by_force(xl)