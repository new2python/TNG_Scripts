#! python3
#Stage Cowley credits
#Created by Curtis Cholon
#05/03/2017

"""
	Parses credit documents provided by Cowley & Benjamin and seperates into
	seperate credits
"""

import os
import re
import time

def stage_credits(partner):
	block = ""
	first_line = ""

	path = os.path.join("L:", "Merge and Print", "Print_Files", partner)
	file_list = os.listdir(path)

	output_filepath = os.path.join("L:", "Merge and Print", "In_Process", partner)

	for file in file_list:
		text_file = open(os.path.join(path, file))
		
		#parse through contents of file
		line_count = 0
		for line in text_file:
			line_count += 1
			if line.startswith("\fPG"): #if line starts with formfeed character
				if os.path.isfile(os.path.join(path, account_number + ".txt")):
					output_file = open((os.path.join(path, account_number + ".txt")), "a")
					output_file.write(block)
					output_file.close()
					block = ""
					first_line += line #save the first line until the account number is found
				else:
					output_file = open((os.path.join(path, account_number + ".txt")), "w")
					output_file.write(block)
					output_file.close()
					block = ""
					first_line += line #save the first line until the account number is found
			elif "account number:" in line.lower(): #assign current account number
				account_regex = re.compile(r'ACCOUNT NUMBER:(.*)')
				account_number = account_regex.search(line)
				account_number = account_number.group()
				account_number = account_number.replace("ACCOUNT NUMBER:","").strip()
				if os.path.isfile(os.path.join(path, account_number + ".txt")):
					#add the first line, saved earlier, to the block variable
					first_line = first_line + block
					block = first_line
					first_line = ""
					block += line
				else:
					#add the first line, saved earlier, to the block variable
					first_line = first_line.strip() + "\n"
					first_line = first_line + block
					block = first_line
					first_line = ""
					block += line
			else:
				block += line
		
		text_file.close()
		
stage_credits("Cowley")

stage_credits("Benjamin")