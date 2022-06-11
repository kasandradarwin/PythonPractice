# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
firstClickUrl =  "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
timesToRepeat = input('Repeat how many times?: ')
positionInput = input('Enter Position: ')
try:
    timesToRepeat = int(timesToRepeat)
    positionInput = int(positionInput)
except:
    print("please add an number")
    quit()

# Retrieve all of the anchor tags
#for i in range(timesToRepeat):
count = 0
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print("retrieving",firstClickUrl)
#def getLink(positionInput,target):
    html = urllib.request.urlopen(target, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        count += 1
        if count == positionInput:
            url = tag.get('href', None)
    #print(url)
    return(url)
subsequentUrl = getlink

while count < (timesToRepeat + 1):
    print(getLink(positionInput,url))
