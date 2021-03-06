import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_1527516.xml'
url = input("Enter a URL -")
print('Retrieving:', url)


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open the link. If link cannot be opened return an error message.
try:
    linkOpener = urllib.request.urlopen(url, context=ctx)
except:
    print("Error: Please use a URL")
    quit()

#read link and convert string to data tree
tree = ET.fromstring(linkOpener.read())

#find the child at comment info > comments > comment > count
#initialize variable to found each iteration, and sum all the numbers
countList = tree.findall('.//count')
sum = 0

# for every item in the list, pull the value out, count the number of iterations
for item in countList:
    eachCount = (item.text)
    sum = sum + int(eachCount)

print("Count: ", len(countList))
print("Sum: ", sum)
