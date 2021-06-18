#JAMF Class to Group Converter
#By Jeremy Neville
#Written 8-14-2017
#Updated 6/18/2021
#Python 2 ONLY, will not work with Python 3+

#NOTE: If running for the first time before a school year, please run groupWipe.py first to clear old classes!

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
#print(response.read())

#Convert response to JSON
s = (response.read())
print(s)
data = json.loads(s)

#Loop through each class ID
for i in data['classes']:
    
    #Set the current URL to the class ID
    id=i['id']
    url = jssUrl+'/JSSResource/classes/id/'+str(id)  
    
    #Get a response from the URL
    requestN = urllib2.Request(url)
    requestN.add_header('Authorization', 'Basic ' + base64.b64encode(username + ':' + password))
    requestN.add_header('Accept', 'application/json')
    responseN = urllib2.urlopen(requestN)
    print('RESPONSE FROM'), id,(':'), responseN.code
    
    #Convert response to JSON
    sN = responseN.read()
    dataN = json.loads(sN)
    
    #Get and print the information needed
    thisName = dataN['class']['name']
    print('Class Name:'), thisName
    theseStudents = dataN['class']['student_ids']
    print('Students:'),theseStudents
    
    #Make the XML ElementTree
    xRoot=Element('user_group')
    xID=Element('id')
    xID.text=str(id)
    xRoot.append(xID)
    xName=Element('name')
    xName.text=str(thisName)
    xRoot.append(xName)
    xSmart=Element('is_smart')
    xSmart.text='false'
    xRoot.append(xSmart)
    xNotify=Element('is_notify_on_change')
    xNotify.text='false'
    xRoot.append(xNotify)
    xSite=Element('site')
    xRoot.append(xSite)
    xSiteID=Element('id')
    xSiteID.text='-1'
    xSite.append(xSiteID)
    xSiteName=Element('name')
    xSiteName.text='None'
    xSite.append(xSiteName)
    xCriteria=Element('criteria')
    xRoot.append(xCriteria)
    xCriteriaSize=Element('size')
    xCriteriaSize.text='0'
    xCriteria.append(xCriteriaSize)
    xUsers=Element('users')
    xRoot.append(xUsers)
    xUsersSize=Element('size')
    xUsersSize.text=str(len(theseStudents))
    xUsers.append(xUsersSize)
    xTree=ElementTree(xRoot)
    for j in theseStudents:
        xUser=Element('user')
        xUsers.append(xUser)
        xUserID=Element('id')
        xUserID.text=str(j)
        xUser.append(xUserID)

    #POST XML back to JSS for each class
    xRequest = urllib2.Request(jssUrl+'/JSSResource/usergroups/id/'+str(id))
    xRequest.add_header('Authorization', 'Basic ' + base64.b64encode(username + ':' + password))
    xRequest.add_header('Content-Type', 'text/xml')
    xRequest.get_method = lambda: 'POST'

    #Try to send it, print a response if it doesn't work
    try:
        xResponse = urllib2.urlopen(xRequest, etree.tostring(xRoot))
    except:
        print ('HTTP Error 409, this class already exists!')
