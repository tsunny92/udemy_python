#!/usr/bin/env python
import requests
import json
import urllib3
import getpass


urlpass='https://dcmgr.hou1.hostgator.com/api/1.0/passwords/?device='
device42url='https://dcmgr.hou1.hostgator.com/api/1.0/devices/name/'

hostname=raw_input("Enter the hostname : ")
username=raw_input("Enter username : ")
password=getpass.getpass("Enter the password : ")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get(device42url+hostname, verify=False, auth=(username, password))
passresponse = requests.get(urlpass+hostname+"&plain_text=yes", verify=False, auth=(username, password))
jsondata= json.loads(response.text)
passdata= json.loads(passresponse.text)


print("------------------------- Details for "+hostname+" -------------------------")

if str(jsondata['hw_model']) == 'None': 
	pass
else:
	print('Hardware model : '+jsondata['hw_model'])

if str(jsondata['manufacturer']) =='None': 
	pass
else:
	print('Manufacturer : '+jsondata['manufacturer'])

if str(jsondata['os']) == 'None': 
	pass
else:
	print("Operating system : "+jsondata['os'])

print('Service Level : '+jsondata['service_level'])

if jsondata['type'] == 'virtual':
	print('Type : '+jsondata['type'])
	print('Host machine '+jsondata['virtual_host_name'])
else:
	print('Type : '+jsondata['type'])

length=len(jsondata['ip_addresses'])

for i in range(length):
	if jsondata['ip_addresses'][i]['label'] == '' or str(jsondata['ip_addresses'][i]['label']) == 'None':
		pass
	else:
		print(jsondata['ip_addresses'][i]['label'].strip()+' address is : '+jsondata['ip_addresses'][i]['ip'])


for i in range(len(passdata['Passwords'])):
	if passdata['Passwords'][i]['label'] == '':
		pass
	else:
		print(passdata['Passwords'][i]['label'].strip()+' password is '+passdata['Passwords'][i]['password'])
