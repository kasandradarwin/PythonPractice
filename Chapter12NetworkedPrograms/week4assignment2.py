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
#html = urllib.request.urlopen(url, context=ctx).read()


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

def getLink(positionInput,target):
    html = urllib.request.urlopen(target, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        count += 1
        if count == positionInput:
            url = tag.get('href', None)
    #print(url)
    return(url)

while count < (timesToRepeat + 1):
    print(getLink(positionInput,url))

#print(firstClickUrl)
#for i in range(timesToRepeat):
    #linkToPrint = getLink(positionInput,)
    #subsequentLink =  getLink(positionInput,firstClickUrl)
    #thirdLink = getLink(positionInput,subsequentLink)
    #fourthLink = getLink(positionInput,thirdLink)
    #fifthLink = getLink(positionInput,fourthLink)

#print(subsequentLink)
#print(thirdLink)
#print(fourthLink)
#print(fifthLink)
    #print(subsequentLink)
