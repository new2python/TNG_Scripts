#Read Text File

from sys import argv

#script, agency, account_number, account_name = argv

agency = "Atlanta"
account_number = 691186
account_name = "Rite_Aid"

word = "PRIMARY SEQ#:"

#use account number as string reference for the search parameter
account_number_str = str(account_number)

#add leading spaces to the account number if not long enough
while len(account_number_str) < 12:
    account_number_str = str(" " + account_number_str)

search_string = word + account_number_str

#open print file
text_file = open("L:\\Merge and Print\\Python Scripts\\" + agency + " CREDITS.txt", "r")
block = ""
found = False

#parse through each line
for line in text_file:
    if found:
        if word in line.strip():
            if search_string in line:
                block += line
	    else:
                found = False
                break
        else:
            block += line
    else:
        if search_string in line.strip():
            found = True
            block = line.strip()
        
text_file.close()

#write the contents to a new file
output_file = open("L:\\Merge and Print\\Python Scripts\\" + account_number + "_" + account_name+".txt","w")
output_file.write(block)
output_file.close()

