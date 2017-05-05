#! python3
#Parses Kent Credits and Renames According to Store / Account
#Created by Curtis Cholon
#05/03/2017

import os
from shutil import copyfile
import re

path = os.path.join("L:", "Merge and Print", "Print_Files", "Kent")
file_list = os.listdir(path) #list of files provided by Kent

#Parse through each file - need to be renamed to .txt in order to use
for file in file_list:
	#rename file to .txt so that we can parse through the contents
	copyfile((os.path.join(path, file)), (os.path.join(path, file + ".txt")))
	#delete the original file
	os.remove(os.path.join(path, file))
	
	#read the contents of the file
	text_file = open(os.path.join(path, file + ".txt"))
	for line in text_file:
		if "account number:" in line.lower():
			account_regex = re.compile(r'ACCOUNT NUMBER:(.*)')
			account_number = account_regex.search(line)
			account_number = account_number.group()
			account_number = account_number.replace("ACCOUNT NUMBER:","").strip()
			break
	
	text_file.close()
	#Rename file according to account number
	copyfile((os.path.join(path, file + ".txt")), (os.path.join(path, account_number + ".txt")))
	os.remove(os.path.join(path, file + ".txt"))
