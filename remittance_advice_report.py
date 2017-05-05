#! python3
#Start Remittance Advice
#Created by: Curtis Cholon
#03/24/2017

"""
Parses through the AP Remittance Advice report to extract 
the receiving report for each vendor and save as an individual file
"""

#Test values

##########################################################
region = "Atlanta"
agency = "Atlanta"
##########################################################

import re
from sys import argv

text_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " - START REMIT.txt")
		
block = ""
vendor = ""

for line in text_file:
	if "<< REMITTANCE ADVICE REPORT >>" in line:
		if vendor:
			output_file = open("L:\\Start and End Reports\\" + region + "\\#TB1PRT\\" + agency + " " \
				+ vendor + " - START REMIT.txt","a+")
			output_file.write(block)
			output_file.close()
			block = ""
			vendor = ""
			block += line
		else:
			block += line
			continue
	elif "VENDOR #:" in line:
		vendor_regex = re.compile('\\d{9}')
		vendor = vendor_regex.search(line)
		vendor = vendor.group()
		block += line
	else:
		block += line