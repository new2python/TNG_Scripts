#! python3
#sharepoint lists
#check sharepoint site and cycles through the list

import requests
from requests_ntlm import HttpNtlmAuth
from shareplum import Site
import json

site = "http://tng/SharedServices/AR/Lists/Rite%20Aid%20Credit%20Distribution/Datasheet_View.aspx"
username = "thenewsgroup\\svc_aadevbot2"
password = "1R0bot2rule.them@ll"
list_name = "Rite_Aid_Credit_Distribution"

# headers = {
	# "Accept":"application/json; odata=verbose",
    # "Content-Type":"application/json; odata=verbose",
    # "odata":"verbose",
    # "X-RequestForceAuthentication": "true"
# }
# response = requests.get(site+"lists/getbytitle('%s')" %list_name, auth = HttpNtlmAuth(username,password), headers=headers)

# #list_id = response.json()['d']['ID']
# #print(list_id)

# print(response.status_code)
# print(response.headers['content-type'])
# print(response.encoding)
# print(response.headers)
# input(response.text)

