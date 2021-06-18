#JAMF Class Wipe
#Deletes all classes in JAMF
#By Jeremy Neville
#Written 6/18/2021
#Python 2 ONLY, will not work with Python 3+

import urllib2
import base64
import json
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

#Enter authentication info
print('Enter your username: ')
username = input()
print('Enter your password: ')
password = input()
print('Enter your server URL: ')
jssUrl = input()

#Get list of classes from server
request = urllib2.Request(jssUrl + '/JSSResource/classes')
request.add_header('Authorization', 'Basic ' + base64.b64encode(username + ':' + password))
request.add_header('Accept', 'application/json')
response = urllib2.urlopen(request)
print('RESPONSE FROM LIST:'), response.code

#Convert response to JSON
s = (response.read())
#print(s)
data = json.loads(s)

#Loop through each class ID
for i in data['classes']:
    #Set the ID and URL
    id=i['id']
    url = jssUrl+'/JSSResource/classes/id/'+str(id)
    
	#Delete the group
	xRequest = urllib2.Request(jssUrl+'/JSSResource/classes/id/'+str(id))
	xRequest.add_header('Authorization', 'Basic ' + base64.b64encode(username + ':' + password))
	#xRequest.add_header('Content-Type', 'text/xml')
	xRequest.get_method = lambda: 'DELETE'
	xResponse = urllib2.urlopen(xRequest)
	print'class deleted!'
    
