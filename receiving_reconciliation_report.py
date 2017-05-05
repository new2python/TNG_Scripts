#! python3
#AP Magazine Receiving Report
#Created by: Curtis Cholon
#03/23/2017

"""
Parses through the AP Receiving Reconciliation report to extract 
the receiving report for each vendor and save as an individual file
"""

#Test Values

####################################################
region = "Atlanta"
agency = "Atlanta"
####################################################

import re
from sys import argv


text_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " - START RECEIVING.txt")
		
block = ""
vendor = ""

for line in text_file:
	if "RECEIVING RECONCILIATION REPORT" in line:
		if vendor:
			output_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " " \
				+ re.sub('[^A-Za-z0-9]+',' ',vendor) + " - START RECEIVING.txt","a+")
			output_file.write(block)
			output_file.close()
			block = ""
			vendor = ""
			block += line
		else:
			block += line
			continue
	elif "OUR ACCOUNT # :" in line:
		vendor = line.replace("OUR ACCOUNT # :","").strip()
		block += line
	else:
		block += line
		