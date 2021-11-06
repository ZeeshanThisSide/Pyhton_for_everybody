import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')

uh = urllib.request.urlopen(address, context=ctx).read()


data = uh
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
s = 0
for item in results:
    x = item.find('count').text
    s = s + int(x)
print('Sum:',s )
