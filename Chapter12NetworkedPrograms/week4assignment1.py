#In this assignment you will write a Python program to use urllib to read the HTML
#from the data files below, and parse the data, extracting numbers and compute the
#sum of the numbers in the file




#To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
#from bs4 import BeautifulSoup
import bs4
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
tagSum = 0
for tag in tags:
    tagSum = tag.contents[0]
    sum += int(tagSum)
print("sum: ", sum)


    # Look at the parts of a tag
    #print(line.decode().strip())
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
