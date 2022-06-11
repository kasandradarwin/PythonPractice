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

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

countInput = input('Enter Count: ')
positionInput = input('Position: ')
count = 0
position = 0

# Retrieve all of the anchor tags
tags = soup('a')

for i in range(positionInput):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    for tag in tags:
        count += 1
        if count > countInput:
            break
        #print("COUNT: ", count)
        #print('TAG:', tag)
        link= tag.get('href', None)
print(link)
        #print('Contents:', tag.contents)
        #print('Attrs:', tag.attrs)

#tags = soup('span')
#sum = 0
#tagSum = 0
#for tag in tags:
#    tagSum = tag.contents[0]
#    sum += int(tagSum)
#print("sum: ", sum)
