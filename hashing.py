#!/usr/bin/env python
from configparser import ConfigParser
import hashlib, uuid
import getpass
import os

if os.path.isfile('details.config'):
    parser = ConfigParser()
    parser.read('details.config')
    passwd=getpass.getpass("Enter the password ")
    hashed_password = hashlib.md5(passwd).hexdigest()
    verify_pass=parser.get('details_config', 'password')
    if hashed_password  == verify_pass:
        print(parser.get('details_config', 'url'))
        #for section_name in parser.sections():
        #    for key,value in parser.items(section_name):
        #        print('  {} = {}'.format(key, value))
    else:
        print("No match found")
else:
    with open('details.config','w+') as f:
        f.write("[details_config]")
        f.write("\nurl=http://localhost:3036/")
        user=raw_input("Enter username ")
        f.write("\nusername="+user)
        passw=getpass.getpass("Enter the password")
        f.write("\npassword="+hashlib.md5(passw).hexdigest())

