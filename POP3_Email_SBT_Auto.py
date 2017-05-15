#! python3
#POP3 Email
"""Retrieve emails from POP3 email exchange"""

import poplib
import email
import os
import sys
import re
import csv

def retrieve_POS_reports():
	#Set email protocol settings
	host = '10.0.240.196'
	#user = input("Username" + "\n")
	user = 'svc_aataskbot3'
	#password = input("Password" + "\n")
	password = '1R0bot2rule.them@ll'
	
	#Connect to email exchange server
	popObj = poplib.POP3_SSL(host)
	print(popObj.getwelcome())
	popObj.user(user)
	popObj.pass_(password)

	#returns message count and mailbox size in bytes
	email_stat = popObj.stat()

	#List provides email response code, total number of emails and byte size, 
	#and a list of stats for each message...
	#input(popObj.list())

	for i in range(email_stat[0]):
		#retr returns (response, ['line'], octets)
		#converts raw email into string
		message = popObj.retr(i+1)[1]
		str_message = email.message_from_bytes(b'\n'.join(message))
		

		from_addr = str_message['from']
		subject = str_message['subject']
		
		#TO DO - extract company name from email address and use to name the file
			
		print(from_addr)
		print(subject)
		
		#ignore any emails not part of the POS to AR process
		if "sbtauto@thenewsgroup.com" not in from_addr:
			continue
		
		#discard DRIVR reports - not used for evaluating POS
		if "autsbt_drivr" in subject.lower():
			#popObj.dele(i+1) #disabled for testing purposes
			continue
		
		#Capture chain number and use to name the file
		chain_regex = re.compile(r'\d{7}')
		chain = chain_regex.search(subject)
		chain = chain.group()
		
		#save the attachment
		for part in str_message.walk():
			#print(part.get_content_type())
			
			if part.get_content_maintype() == 'multipart':
				continue
				
			if part.get('Content-Disposition') is None:
				#print('no content dispo')
				continue
				
			filename = part.get_filename()
			if not(filename): filename = "test.txt"
			#print(filename)
			
			#Computac print files do not contain an extension
			if list(os.path.splitext(filename))[1] == "": #captures file extension (if there is one).
				filepath = open(os.path.join("L:\\", "POS_Reporting", chain + "_" + str(i)) + ".txt", 'wb')
				filepath.write(part.get_payload(decode=1))
				filepath.close()
				print(os.path.join("L:", "POS_Reporting", chain + "_" + str(i) + ".txt"))
				
			#parse through recap reports
			process_recap_reports(os.path.join("L:\\", "POS_Reporting", chain + "_" + str(i) + ".txt"), chain)
			
		print("\n")
		#delete email after the attachment has been retrieved.
		#popObj.dele(i+1) #disabled for testing purposes.

	popObj.quit()
	sys.exit(0)

def process_recap_reports(filepath, chain):
	"""Parses through the SBT recap reports for POS totals"""
	
	#agency map
	agency_map = {
		"TNG CALGARY" : "Calgary",
		"TNG HALIFAX" : "Halifax",
		"TNG - ARIZONA" : "Arizona",
		"TNG - JACKSON" : "Jackson",
		"TNG - SPECIALTY" : "Specialty",
		"TNG - TEXAS" : "Texas",
		"TNG-ALASKA" : "Alaska",
		"TNG - FIFE" : "Fife",
		"TNG - HAWAII" : "Hawaii",
		"TNG - ATLANTA" : "Atlanta",
		"TNG - SACRAMENTO" : "Sacramento",
		"TNG - SALT LAKE CITY" : "Salt Lake City",
		"TNG ONTARIO" : "Toronto"
		}
	
	text_file = open(filepath)
	
	grand_total_count = 0
	line_count = 0
	agency = ""
	for line in text_file:
		#assign agency
		if "tng" in line.lower():
			for i in agency_map.items():
				if i[0] in line:
					agency = i[1]
		
		if "grand totals:" in line.lower():
			grand_total_count += 1
			
		#third instance of the string "grand totals" includes POS totals
		if grand_total_count == 3:
			pos_amount = re.search(r'\d.*', line)
			pos_amount = pos_amount.group()
			
			#negative values need to be formatted
			if "-" in pos_amount:
				pos_amount = pos_amount.replace("-","")
				pos_amount = -float(pos_amount)
			
			break
			
	text_file.close()
	
	#Record POS amounts to file.
	record_pos_amounts(agency, chain, pos_amount)

def record_pos_amounts(agency, dealer, pos_amount):
	"""write POS amounts to file for further reference later"""
	
	outputWriter.writerow([agency, dealer, pos_amount])
	
	
#open CSV file to record POS amounts
output_file = open(os.path.join("L:\\", "POS_Reporting", "Dealer_Log.csv"), "w", newline = "")
outputWriter = csv.writer(output_file)
#Record header
outputWriter.writerow(['Agency','Chain_Master','POS_Amount'])

retrieve_POS_reports()

#Close CSV file
output_file.close()
