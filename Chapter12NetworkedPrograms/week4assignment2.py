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

count = 0
countInput = input('Enter Count: ')
positionInput = input('Enter position: ')


# Retrieve all of the anchor tags
tags = soup('a')
while count < countInput:
    for tag in tags:
        if position != positionInput:
            continue
            count += 1
            #print("COUNT: ", count)
            #print(tag.get('href', None))
            #print('TAG:', tag)
            #print('URL:', tag.get('href', None))
            print('Contents:', tag.contents[3])
            #print('Attrs:', tag.attrs)

#tags = soup('span')
#sum = 0
#tagSum = 0
#for tag in tags:
#    tagSum = tag.contents[0]
#    sum += int(tagSum)
#print("sum: ", sum)
