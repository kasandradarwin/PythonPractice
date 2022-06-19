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
print("1")
#address = 'South Federal University' place id should be: ChIJNeHD4p-540AR2Q0_ZjwmKJ8

while True:
    print("2")
    address = input('Enter location: ')
    if len(address) < 1:
        address = 'South Federal University'

    parms = dict()
    parms['address'] = address #address type = string
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("3")

    try:
        js = json.loads(data)
        dumpy = (json.dumps(js, indent=4))
        print("4")
        #print(dumpy)

    except:
        js = None

    print("5")

    counter = 0
    print("6")
    for item in dumpy:
        #parms.append(js['place_id'])
        counter += 1
        print("7")
        place_id = js['results'][0]['place_id']
        print("8")
        #lng = js['results'][0]['geometry']['location']['lng']
        # print('lat', lat, 'lng', lng)
        # print('Retrieved', len(data), 'characters')
        # print("Place id = ", placeId)
        #location = js['results'][0]['formatted_address']
        print(place_id)
        print(place_id)
        print(place_id)
