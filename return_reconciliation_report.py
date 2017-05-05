#! python3
#AP Magazine Return Report
#Created by: Curtis Cholon
#03/23/2017

"""
Parses through the AP Return Reconciliation report to extract 
the receiving report for each vendor and save as an individual file
"""

#Test Values

####################################################
region = "Atlanta"
agency = "Atlanta"
####################################################

import re
from sys import argv


text_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " - START RETURN.txt")
		
block = ""
vendor = ""

for line in text_file:
	if "RETURN RECONCILIATION REPORT" in line:
		if vendor:
			output_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " " \
				+ vendor + " - START RETURN.txt","a+")
			output_file.write(block)
			output_file.close()
			block = ""
			vendor = ""
			block += line
		else:
			block += line
			continue
	elif "TO: ACCOUNT #" in line:
		vendor = re.search('\\d+', line)
		vendor = vendor.group()
		block += line
	else:
		block += line
		