#! python3
#created by: Curtis Cholon
#03/24/2017

"""Parses the AP starting reconciliation reports and splits according
to vendor
"""

#Test Values

######################################################
#region = "Atlanta"
#agency = "Atlanta"
######################################################

import re
from sys import argv

script, region, agency = argv

def remit():
	"""Remittance Advice"""
	
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
			
def sub_ledger():
	"""Sub ledger"""
	
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
			
def receiving():
	"""Receiving reconciliation report"""
	
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
			
def returns():
	"""Return reconciliation report"""
	
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

#MAIN

remit()

sub_ledger()

receiving()

returns()


			