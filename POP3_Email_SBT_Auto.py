#! python3
#POP3 Email
"""Retrieve emails from POP3 email exchange"""

import poplib
import email
import os
import sys

def retrieve_POS_reports():
	#Set email protocol settings
	host = '10.0.240.196'
	user = 'svc_aataskbot3'
	pass_word = '1R0bot2rule.them@ll'

	#Connect to email exchange server
	popObj = poplib.POP3_SSL(host)
	print(popObj.getwelcome())
	popObj.user(user)
	popObj.pass_(pass_word)

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
		
		if "sbtauto@thenewsgroup.com" not in from_addr:
			continue
		
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
			
			#TO DO - deposit download file to Merge and Print directory
			
			#Computac print files do not contain an extension
			if list(os.path.splitext(filename))[1] == "":
				filepath = open(os.path.join("C:\\", "Temp_Email", filename + "_" + str(i)) + ".txt", 'wb')
				filepath.write(part.get_payload(decode=1))
				filepath.close()
				print(os.path.join("C:", "Temp_Email", filename + "_" + str(i)))
		print("\n")
		#delete email after the attachment has been retrieved.
		#popObj.dele(i+1) #disabled for testing purposes.

	popObj.quit()
	sys.exit(0)


retrieve_POS_reports()