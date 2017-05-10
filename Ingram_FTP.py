#! python3
#Ingram FTP File Distribution
#Created by Curtis Cholon
#05/10/2017

"""
	Periodically check Ingram FTP site for new files and 
	deposit the respective directory according to filename.
"""

import ftplib
import os

#setup login credentials
login = 'jsparrow'
passw = 'cabsauv69'
host = 'secure-transfer.tng.com'

#open FTP session
ftp = ftplib.FTP(host)
ftp.login(login, passw)

#get file listing
file_list = ftp.nlst()
print(file_list)

for file in file_list:
	filename, file_extension = os.path.splitext(file)
	if file_extension:
		print(file)



#############################################
#          AR Transaction Directory         #
#############################################

		
#check the AR Transaction directory
ftp.cwd('/TNG Uploads/Accounts Receivable/AR Files/Transactions')
file_list = ftp.nlst()
print(file_list)


#############################################
#             3PL Fee Files                 #
#############################################


#check 3PL Fee Directory
ftp.cwd('/TNG Uploads/3PL/Fee files')
file_list = ftp.nlst()
print(file_list)
		
ftp.quit()