#!/usr/bin/env python
import requests
import json
import urllib3
import getpass
import os
from os import path

jiraurl='https://jira.endurance.com/rest/api/2/search?jql=description~%22List%20of%20Affected%20TLDs%22%20and%20project=%22Enterprise%20-%20Monitoring%20Center%20Server%20Issues%22&fields=id,key,description'

username=raw_input("Enter username : ")
password=getpass.getpass("Enter the password : ")


# Disalbe or ignore ssl verification warnings message
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


response = requests.get(jiraurl, verify=False, auth=(username, password))
jsondata= json.loads(response.text)

count = len(jsondata['issues'])
def datacollect():
	if count > 0:
		with open('/home/sunny.t/datafile.txt' , 'w') as f:
        		for i in range(count):
                        	data =  str(jsondata['issues'][i]['key']) + '\n' + str(jsondata['issues'][i]['fields']['description'])		
				f.write(data)
	else:
		print("No issues found")

def listoftlds():	
	if path.exists('/home/sunny.t/datafile.txt'):
    		file = open('/home/sunny.t/datafile.txt').read().splitlines()
    		for index, line in enumerate(file):
        		if 'EMCSI' in line or 'Start time' in line or 'End time' in line:
            			print(line)
        		elif "List of Affected TLDs" in line :
            			for data in file[index+1:index+1000]:
                			if not '---' in data:
                    				print(data)
    		os.remove('/home/sunny.t/datafile.txt')
	else:
		print("No file found")
datacollect()
listoftlds()
