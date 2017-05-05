#Document Circulation

from sys import argv
import os
import subprocess

script, region, agency, account_number, account_name, statements, invoices, credits = argv

#TEST VALUES

##################################################################
#region = "US_East"
#agency = "Atlanta"
#account_number = 690982
#account_name = "Rite_Aid_#2795"
#statements = "False"
#invoices = "False"
#credits = "True"
##################################################################

def stmts():
        """Retrieve Statements"""
        block = ""
        found = False

        #open statement text file
        text_file = open("L:\\Merge and Print\\Print_Files\\" + region + "\\" + agency \
                         + " STATEMENTS.txt")

        #parse through each line in the statements text file
        for line in text_file:
                if found:
                        if WORD in line:
                                if search_string in line:
                                        block += line
                                else:
                                        found = False
                                        break
                        else:
                                block += line
                else:
                        if search_string in line:
                                found = True
                                global output
                                if output: #if the output file has already received text then write the raw string
                                        block = line
                                else: #remove the form feed character
                                        block = line.strip() + "\n"
                                        output = True

        # write contents to output file
        output_file.write(block)
        #print(block)
        # close the statement text file
        text_file.close

def process_invoices():
        """Retrieve Invoices"""
        block = ""
        found = False

        #open invoice text file
        text_file = open("L:\\Merge and Print\\Print_Files\\" + region + "\\" + agency + \
                         " INVOICES.txt")

        #parse through each line of the invoice file
        for line in text_file:
                if found:
                        if WORD in line:
                                if search_string in line:
                                        block += line
                                else:
                                        found = False
                                        break
                        else:
                                block += line
                else:
                        if search_string in line:
                                found = True
                                global output
                                if output:
                                        block = line
                                else:
                                        block = line.strip() + "\n"
                                        output = True

        #write contents to output file
        output_file.write(block)
        #print(block)
        #close text file
        text_file.close()

def process_credits():
        """Retrieve credit memos"""
        block = ""
        found = False
        verification_num = ""

        #open credit memo text file
        text_file = open("L:\\Merge and Print\\Print_Files\\" + region + "\\" + agency + \
                         " CREDITS.txt")

        #parse through each line
        for line in text_file:
                if found:
                        if WORD in line:
                                output_file.write(block) # write contents to the output file - append 1 page at a time
                                #print(block)
                                block = ""
                                global output
                                output = True
                                if search_string in line: #next instance of the dealer
                                        block += line
                                else:
                                        found = False
                                        break
                        elif "for verification:" in line.lower():
                                verification_num = invoice_number
                                block = ""
                                found = False
                                output = False
                        else:
                                block += line
                else:
                        if search_string in line:
                                found = True
                                if output:
                                        block = line
                                else:
                                        block = line.strip() + "\n"

        text_file.close()

#True / False - output file has received text
output = False

#constant string
WORD = "PRIMARY SEQ#:"

#use account number as string reference for the search parameter
account_number_str = str(account_number)

#add leading spaces to the account number if the not long enough
while len(account_number_str) < 12:
        account_number_str = " " + account_number_str

#concatenate to define the search string:
search_string = WORD + account_number_str

#create output file
output_file = open("L:\\Merge and Print\\In_Process\\" + region + "\\" + agency + " " \
                   + str(account_number) + " " + account_name + ".txt", "a")

#MAIN
if statements == "True":
        stmts()

if invoices == "True":
        process_invoices()

if credits == "True":
        process_credits()

output_file.close()

path = "L:\\Merge and Print\\In_Process\\" + region + "\\" + agency + " " \
                   + str(account_number) + " " + account_name + ".txt"

#if the output file has not received any text, delete
if output == False:
        os.remove("L:\\Merge and Print\\In_Process\\" + region + "\\" + agency + " " \
                   + str(account_number) + " " + account_name + ".txt")
else:
		subprocess.run(["C:\\Program Files (x86)\\Text2PDF v1.5\\txt2pdf.exe",path,"-pfs8","-plm25","-prm25", \
				"-ptm25","-pbm25","-pdn:Lucida Console"])
		os.remove(path)

