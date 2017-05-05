#Read Text File

from sys import argv

#script, region, agency, account_number, account_name = argv

#input("press enter to continue")

region = "US_East"
agency = "Atlanta"
account_number = 691186
account_name = "Rite Aid"

word = "PRIMARY SEQ#:"

#use account number as string reference for the search parameter
account_number_str = str(account_number)

#add leading spaces to the account number if not long enough
while len(account_number_str) < 12:
    account_number_str = str(" " + account_number_str)

search_string = word + account_number_str

#open print file
text_file = open("L:\\Merge and Print\\Print_Files\\" + region + "\\" + agency + " CREDITS.txt")
output_file = open("L:\Merge and Print\\In_Process\\" + region + "\\" + agency + " " \
                   + str(account_number) + " " + account_name + ".txt","a+")
block=""
found = False
verification_num = ""

#parse through each line
for line in text_file:
    if found:
        if word in line.strip():
            if search_string in line.strip():
                block += line + "\n"
            else:
                found = False
                break
        elif "invoice number:" in line.strip().lower():
            invoice_number = int(line.strip().lower().replace("invoice number:",""))
            if invoice_number == verification_num:
                block = ""
                found = False
        elif "for verification" in line.strip().lower():
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

#write the contents to a new file
#output_file = open("L:\Merge and Print\\In_Process\\Current_Substring.txt","w")

output_file.write(block)output_file.close()
