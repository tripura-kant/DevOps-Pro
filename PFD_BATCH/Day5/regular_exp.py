'''
Regular expression for extracting email ids

'''


import re

text = '''
	This alert will notify tripurakant@Gmail.com and trainwithmonu@gmail.com


'''

#print(dir(re.findall))
#print(re.findall.__doc__)

list_of_emails = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",text)
print(list_of_emails)



