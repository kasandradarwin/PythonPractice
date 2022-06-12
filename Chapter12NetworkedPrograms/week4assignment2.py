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
url =  "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
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
iterationCount = 0
totalCount = 0
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
subseqentUrl = None
subsequentLinks = []
print("Retrieving: ",url)

for i in range(timesToRepeat):
    iterationCount += 1
    for tag in tags:
        subsequentLinks.append(tag.get('href', None))
        html = urllib.request.urlopen(url, context=ctx).read()
    #iterationCount += 1
        while totalCount < (timesToRepeat + 1):
            if url != None:

                if iterationCount == positionInput:
                    totalCount += 1
                    url = tag.get('href', None)
            #iterationCount = (iterationCount - timesToRepeat)


#while count < (timesToRepeat + 1):
