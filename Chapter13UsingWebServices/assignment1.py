import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_1527516.xml'
url = input("Enter a URL -")
print('Retrieving:', url)


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open the link and pull out the count(s)
try:
    linkOpener = urllib.request.urlopen(url, context=ctx)
except:
    print("Error: Please use a URL")
    quit()

#print("link opener ",linkOpener.read())
tree = ET.fromstring(linkOpener.read())
#print(linkOpener.decode())
#countList = tree.findall('commentinfo/comments/comment/count')
countList = tree.findall('.//count')
sum = 0
numberofitems = 0
for item in countList:
    eachCount = (item.text)
    numberofitems += 1
    sum = sum + int(eachCount)
print("Count: ", numberofitems)
print("Sum: ", sum)
    #sum = sum + int(eachCount)
    #print(sum)
# data = linkOpener.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
