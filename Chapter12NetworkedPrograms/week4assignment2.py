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
timesToRepeat = '4'
positionInput = '3'
# url =  "http://py4e-data.dr-chuck.net/known_by_Scott.html"
# timesToRepeat = '7'
# positionInput = '18'
#timesToRepeat = input('Repeat how many times?: ')
#positionInput = input('Enter Position: ')
try:
    timesToRepeat = int(timesToRepeat)
    positionInput = int(positionInput)
except:
    print("please add an number")
    quit()

# Retrieve all of the anchor tags

# extracting the first link:
html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup('a')

#Leave this all alone ^^^^
#extracting the following 4

for i in range(timesToRepeat+timesToRepeat):
    print("Retrieving: ",url)
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.select('a')[positionInput-1]
    html = urllib.request.urlopen(url, context=ctx).read()
    url = tag.get('href')
    
