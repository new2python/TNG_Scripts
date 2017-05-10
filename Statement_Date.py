#! python3
#Statement Date
#Created by Curtis Cholon
#05/10/2017

"""
	Based on today's date, find the current statement date.
	i.e. Today is Wednesday, what statement week are we
	currently working in? Previous Sunday
"""

import datetime

def current_statement_date():
	# get the current datetime object
	now = datetime.datetime.now()
	#get the current day of the week - Sunday = 0
	weekday = now.strftime('%w')
	
	#days since the last statement date
	time_delta = 0 - int(weekday)

	#calculate current statement date
	statement_date = datetime.datetime.now() + datetime.timedelta(time_delta)
	#convert to "mm/dd/yy"
	statement_date = statement_date.strftime('%m/%d/%y')
	print(statement_date)
	
current_statement_date()