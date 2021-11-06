import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
#url = serviceurl + urllib.parse.urlencode({'address':address})
uh = urllib.request.urlopen(address).read()

info = json.loads(uh)



s = 0
for item in info['comments']:
    x = item['count']
    s = s + int(x)
print('Sum:',s )
