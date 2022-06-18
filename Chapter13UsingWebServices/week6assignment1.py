import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input(print("Please enter a URL"))
#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1527517.json'


try:
    linkOpener= urllib.request.urlopen(url, context=ctx)
    info = linkOpener.read()

except:
     print("PC load letter? WTF does that mean?")
     quit()

data = json.loads(info)
comments = data['comments']
counter = 0
counts = list()
for comment in comments:
    counts.append(comment['count'])
    counter += 1

total = (sum(counts))


print('Retrieving:', url)
print('Retrieved:', len(info), 'characters')
print('Count:', counter)
print("Sum:", total)

# Should look like:

# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...
