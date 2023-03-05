#using Google APIfor geo coding
# simple application to prompt the user string
#using Google APi extract the information and return JSON

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

#if apikey is available enter it herer
#resource:  https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
  api_key = 42
  serviceURL= 'http://py4e-data.dr-chuck.net/json?'
else:
  serviceURL = 'https://maps.googleapis.com/maps/api/geocode/json?'

#ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode - ssl.CERT_NONE


while True:
  address = input('location: ')
  if len(address) <1 : break
  parms = dict()
  parms['address'] = address
  if api_key is not False: parms['key'] =api_key
  url = serviceURL + urllib.parse.urlencode(parms)

  print('Retrieving', url)
  uh = urllib.request.urlopen(url, context=ctx)
  data = uh.read().decode()
  print(f'retrieved {len(data)} characters')
  try:
    js =json.loads(data)
  except:
    js = None
  
  if not js or 'status' not in js or js['status'] != 'OK':
    print('=====Failure to Retriev=====')
    print(data)
    continue

  print(json.dumps(js, indent=4))

  lat=js['results'][0]['geometry']['location']['lat']
  lng=js['results'][0]['geometry']['location']['lng']

  print(f'lat: {lat}; lng: {lng}')
  location = js['results'][0]['formatted_address']
  print(location)


