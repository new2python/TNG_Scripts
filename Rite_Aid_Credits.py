#Read Text File

from sys import argv

script, region, agency, account_number, account_name = argv

# TEST VALUES
############################################################
#region = "US_Midwest"
#agency = "Jackson"
#account_number = 32883
#account_name = "Rite Aid"
############################################################

word = "PRIMARY SEQ#:"

#use account number as string reference for the search parameter
account_number_str = str(account_number)

#add leading spaces to the account number if not long enough
while len(account_number_str) < 12:
    account_number_str = str(" " + account_number_str)

search_string = word + account_number_str

###CREATE OUTPUT FILE###
#if output file does not exist then create it, otherwise append to the current document
output_file = open("L:\Merge and Print\\In_Process\\" + region + "\\" + agency + " " \
                   + str(account_number) + " " + account_name + ".txt","a+")

#### CREDITS ####

#open print file
text_file = open("L:\\Merge and Print\\Print_Files\\" + region + "\\" + agency + " CREDITS.txt")

block=""
found = False
verification_num = ""

#parse through each line
for line in text_file:
    if found:
        if word in line.strip():
            output_file.write(block) #write contents of block to file - 1 page at a time
            block = ""
            if search_string in line.strip(): #next instance of dealer
                block += line + "\n"
            else:
                found = False
                break
        elif "invoice number:" in line.strip().lower(): #capture invoice number
            invoice_number = int(line.strip().lower().replace("invoice number:",""))
            if invoice_number == verification_num: #delete contents of current page if the invoice number = verification number
                block = ""
                found = False
        elif "for verification" in line.strip().lower(): #if invoice contains "for verification" flag the invoice number
            verification_num = invoice_number
            block = ""
            found = False
        else:
            block += line
    else:
        if search_string in line.strip():
            found = True
            block = line.strip()

text_file.close()
output_file.close()
