import json
import urllib.request, urllib.parse, urllib.error
import ssl


#url = input(print("Please enter a URL"))
url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print("Please enter a URL:",url)
print('Retrieving:', url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    linkOpener= urllib.request.urlopen(url, context=ctx)
    info = linkOpener.read()


except:
     print("PC load letter? WTF does that mean?")
     quit()
#print("data",data)
print('Retrieved:', len(info), 'characters')

#numbers['count'] = count
sum = 0
#print("data", data)
data = json.loads(data)

if 'count' in info:
    print('yep, found it')
else:
    print('nope, its not here')
# number = ('Count',data['count'])
# print(number)

# for line in data:
#     #print("line: ",line)
#     number = ('Count',data['count'])
#     print(number)




    #print('Name', line['name'])
     #print('Id', item['id'])
     #print('Attribute', item['x'])


# Should look like:
# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...
