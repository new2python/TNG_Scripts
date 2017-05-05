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
		"TNG - SACRAMENTO":"Sacramento"}

#open and parse through region map
region_map = open("L:\\Merge and Print\\Region_Mapping.csv")
read_csv = csv.reader(region_map)
region_data = list(read_csv)

#Process each region seperately
count = 0
for row in region_data:
	count += 1
	if count == 1: #skip the header row
		continue
	else:
		region, stp_file, ip_address, print_directory = row
		
		#create filepath for print files
		local_directory = os.path.join("C:\\Test", region)
		if os.path.exists(local_directory) == False:
			os.makedirs(local_directory)
		else:
			shutil.rmtree(local_directory)
			os.mkdir(local_directory)
		
		#open FTP session
		ftp = ftplib.FTP(ip_address)
		ftp.login("taskbot3", "alsbridge")
	
		#navigate to the proper print directory
		ftp.cwd(print_directory + "/#TB3PRT")
		
		#get a list of files available
		file_list = ftp.nlst()
		
		#download each file and save with a .txt extension
		for file in file_list:
			local_filename = os.path.join(local_directory, file + ".txt") #writes file with .txt extension
			local_file = open(local_filename,"wb")
			ftp.retrbinary('RETR ' + file, local_file.write)
			local_file.close()
	ftp.quit()