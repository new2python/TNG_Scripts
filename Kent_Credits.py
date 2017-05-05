#! python3
#Process partner credits
#05/01/2017
#Created by Curtis Cholon

"""Parses partner credits for processing during the Rite Aid document circulation task"""

import os
import re

found = False
block = ""
trap = False
account_number = 2964

text_file = open(os.path.join("L:\\Merge and Print","Print_Files","Kent","Kent Credits.txt"))
for line in text_file:
	while not trap:
		if "the news group" in line.lower():
			trap = True
			if len(block) > 0: #write the contents of block to file
						
		else:
			continue

	if trap:
		block += line
		if "account number" in line.lower():
			account_regex = re.compile(r'ACCOUNT NUMBER:(.*)')
			account_num = account_regex.search(line)
			account_num = account_num.group()
			account_num = account_num.replace("ACCOUNT NUMBER:","").strip()
			
			if account_num != str(account_number):
				block = ""
				trap = False #will continue to next page of credits.
				continue
			
				
				
