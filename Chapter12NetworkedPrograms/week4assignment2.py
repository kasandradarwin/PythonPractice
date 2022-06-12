# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#import requests

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url =  "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
timesToRepeat = '4'
positionInput = '3'
#timesToRepeat = input('Repeat how many times?: ')
#positionInput = input('Enter Position: ')
try:
    timesToRepeat = int(timesToRepeat)
    positionInput = int(positionInput)
except:
    print("please add an number")
    quit()

# Retrieve all of the anchor tags
totalCount = 0
currentRepetitionCount = 0

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("Retrieving: ",url)
#tags = soup('a')

#Leave this all alone ^^^^

for i in range(timesToRepeat+1):
    #soup=BeautifulSoup(requests.get(url).text)
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.select('a')[positionInput]
    html = urllib.request.urlopen(url, context=ctx).read()
    url = tag.get('href')
    print("Retrieving: ",url)
    # #html = urllib.request.urlopen(url, context=ctx).read()
    # for tag in tags:
    #     currentRepetitionCount += 1
    #
    #     if not totalCount >= timesToRepeat:
    #         if currentRepetitionCount == positionInput:
    #             #print("current",currentRepetitionCount)
    #             #print("total",totalCount)
    #             #print("Retrieving: ",url)
    #             currentRepetitionCount = 0
    #             totalCount +=1
    #             url = tag.get('href', None)
    #
    #             print("Retrieving: ",url)
