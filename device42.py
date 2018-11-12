#!/usr/bin/env python
import requests
import json
import urllib3
import getpass

device42url='https://dcmgr.hou1.hostgator.com/api/1.0/devices/all/?name='
urlpass='https://dcmgr.hou1.hostgator.com/api/1.0/passwords/?device='

hostname=raw_input("Enter the hostname : ")
username=raw_input("Enter username : ")
password=getpass.getpass("Enter the password : ")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get(device42url+hostname, verify=False, auth=(username, password))
passresponse = requests.get(urlpass+hostname+"&plain_text=yes", verify=False, auth=(username, password))
jsondata= json.loads(response.text)
passdata= json.loads(passresponse.text)
list1=jsondata['Devices'][0]['ip_addresses']

print("------------------------- Details for "+hostname+" -------------------------")
print("Manufacturer : "+jsondata['Devices'][0]['manufacturer'])
print('Service Level : '+jsondata['Devices'][0]['service_level'])
print('Type :'+jsondata['Devices'][0]['type'])
print("Hardware model :"+jsondata['Devices'][0]['hw_model'])
print("Password for Management : "+passdata['Passwords'][0]['password'])
print("Password for IPMI : "+passdata['Passwords'][1]['password']) 


for i in range(len(list1)):
	if jsondata['Devices'][0]['ip_addresses'][i]['label'].strip() == 'IPMI':
		print(jsondata['Devices'][0]['ip_addresses'][i]['label'].strip() +" Address is "+ jsondata['Devices'][0]['ip_addresses'][i]['ip'])
	elif jsondata['Devices'][0]['ip_addresses'][i]['label'].strip() == 'Management':
		print(jsondata['Devices'][0]['ip_addresses'][i]['label'].strip() +" Address is "+ jsondata['Devices'][0]['ip_addresses'][i]['ip'])
	else:
		pass
