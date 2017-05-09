#! python3
#Merge and Print FTP
#Created by Curtis Cholon
#04/05/2017

"""Cycles through TNG regions and pulls down print files from computac,
	parses the files to determine the contents and saves accordingly."""
	
import csv
import ftplib
import os
import shutil
import re

#Agency map / naming conventions
agency_map = {"TNG-ALASKA":"Alaska", 
		"TNG - SPECIALTY":"Specialty", 
		"TNG - TEXAS":"Texas", 
		"TNG - ATLANTA": "Atlanta",
		"TNG-JACKSON":"Jackson",
		"TNG - ARIZONA":"Arizona",
		"TNG - HAWAII":"Hawaii",
		"TNG - FIFE":"Fife",
		"TNG-SLC":"Salt Lake City",
		"TNG - SALT LAKE":"Salt Lake City",
		"TNG - SACRAMENTO":"Sacramento"}

#open and parse through region map
region_map = open("L:\\Merge and Print\\Region_Mapping.csv")
read_csv = csv.reader(region_map)
region_data = list(read_csv)

#request login details
login = input("Login")
pasword = input("Password")

#Process each region seperately
count = 0
for row in region_data:
	count += 1
	if count == 1: #skip the header row
		continue
	else:
		region, stp_file, ip_address, print_directory = row
		
		#create filepath for print files
		local_directory = os.path.join("L:\\Merge and Print\\Print_Files", region)
		if os.path.exists(local_directory) == False:
			os.makedirs(local_directory)
		else:
			shutil.rmtree(local_directory)
			os.mkdir(local_directory)
		
		#open FTP session
		ftp = ftplib.FTP(ip_address)
		ftp.login(login, password)
	
		#navigate to the proper print directory
		ftp.cwd(print_directory + "/#TB3PRT")
		
		#get a list of files available
		file_list = ftp.nlst()
		
		#download each file and save with a .txt extension
		for file in file_list:
			#skip any SBT files that may be in the QUEUE
			if "SBT" in file:
				continue
		
			local_filename = os.path.join(local_directory, file + ".txt") #writes file with .txt extension
			local_file = open(local_filename,"wb")
			ftp.retrbinary('RETR ' + file, local_file.write)
			local_file.close()
			print(local_filename)
			
			#Inspect file contents and determine agency and document type
			local_file = open(local_filename, "r")
			agency = ""
			document_type = ""
			for line in reversed(local_file.readlines()): #reads in reverse - starting at the end of the document
				#Determine document type.
				if "MAG.CREDIT MEMOS -  Y ORDER 01   Y  N  N  N  N" in line:
					document_type = "Credits"
					print(document_type)
				elif "MAG. INVOICES    -  Y ORDER 01" in line:
					document_type = "Invoices"
					print(document_type)
				elif "STATEMENTS       -  Y ORDER 01" in line:
					document_type = "Statements"
					print(document_type)
				
				#Determine statement date
				if "DOCUMENTS   FROM -" in line and document_type == "Invoices": #the date range for invoices is different
					stmt_regex = re.compile(r'\d{2}/\d{2}/\d{2}') 
					stmt_date = stmt_regex.findall(line)
					stmt_date = stmt_date[1]
					print(stmt_date)
				
				if "PROCESSED   FROM -" in line and document_type != "Invoices":
					stmt_regex = re.compile(r'\d{2}/\d{2}/\d{2}') 
					stmt_date = stmt_regex.findall(line)
					stmt_date = stmt_date[1]
					print(stmt_date)
				
				# Determine agency name
				if agency != "": #exit the loop once the agency has been assigned
					break
				elif "tng" in line.lower():
					for i in agency_map.items():
						if i[0] in line:
							agency = i[1]
							print(agency)
							break
			
			local_file.close()
			print("\n")
			
			#Rename file
			new_filename = local_directory + "\\" + agency + " " + document_type + ".txt"
			os.rename(local_filename, new_filename)
	ftp.quit()
