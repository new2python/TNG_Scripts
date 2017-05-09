#! python3
#Computac FTP Retrieval
#Created by: Curtis Cholon
#04/05/2017

"""Retrieves Computac print jobs via FTP"""

import ftplib
import os

login = input("Login")
password = input("Password")

ftp = ftplib.FTP("192.168.1.9")
ftp.login(login,password)

#current working directory for Atlanta
#TO DO: add parameter to update for each respective region
ftp.cwd("/work3/wang/VOLPRT/#TB3PRT")

#get list of files avialable
file_list = ftp.nlst()

#download each file
#TO DO: for each file in the list, if it already exists then ignore it
for filename in file_list:
	local_filename = os.path.join("C:\\test\\", filename + ".txt") #writes file with .txt extension
	if os.path.isfile(local_filename): #if the file already exists then ignore
		continue
	else:
		file = open(local_filename, "wb")
		ftp.retrbinary('RETR ' + filename, file.write)
		file.close()
	
ftp.quit()
