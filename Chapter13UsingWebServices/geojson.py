#The program will prompt for a location, contact a web service and retrieve
#JSON for the web service and parse that data, and retrieve the first place_id from the JSON.
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#address = 'South Federal University' place id should be: ChIJNeHD4p-540AR2Q0_ZjwmKJ8

address = input('Enter location: ')
if len(address) < 1:
    address = 'South Federal University'

parms = dict()
parms['address'] = address #address type = string
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

try:
    js = json.loads(data)
    dumpy = (json.dumps(js, indent=4))

except:
    js = None

counter = 0

for item in dumpy:
    counter += 1
    place_id = js['results'][0]['place_id']
print("counter",counter)
print('Retrieving', url)
print('Retrieved', len(data), 'characters')
print("Place id", place_id)
