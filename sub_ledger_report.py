#! python3
#Start Sub Ledger	
#Created by: Curtis Cholon
#03/24/2017

"""
Parses through the AP Sub Ledger report to extract 
the receiving report for each vendor and save as an individual file
"""

#Test values

##########################################################
region = "Atlanta"
agency = "Atlanta"
##########################################################

import re
from sys import argv

text_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " - START LEDGER.txt")
		
block = ""
vendor = ""
vendor_regex = re.compile('\\d{9}')

for line in text_file:
	vendor_match = re.match('\\d{9}', line)
	if vendor_match:
		if vendor:
			output_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " " \
				+ vendor + " - START LEDGER.txt","a+")
			output_file.write(block)
			output_file.close()
			block = ""
			vendor = vendor_regex.search(line)
			vendor = vendor.group()
			block += line
		else:
			vendor = vendor_regex.search(line)
			vendor = vendor.group()
			block += line
			continue
	elif "ACCOUNTS PAYABLE BALANCE FORWARD LEDGER" in line:
		continue
	elif "="*30 in line:
		continue
	else:
		block += line