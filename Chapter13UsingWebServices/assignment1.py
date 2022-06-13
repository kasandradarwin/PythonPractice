import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('Retrieving:', url)


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open the link and pull out the count(s)
linkOpener = urllib.request.urlopen(url, context=ctx)

#print("link opener ",linkOpener.read())
tree = ET.fromstring(linkOpener.read())
#print(linkOpener.decode())
#countList = tree.findall('commentinfo/comments/comment/count')
countList = tree.findall('.//count')
for item in countList:
    print('Count',item.text)
# data = linkOpener.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
# tree = ET.fromstring(data)

print("tree: ",tree)
#print("counts: ",counts)
