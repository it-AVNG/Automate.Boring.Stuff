from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
    # look at all part of the tag
    print('TAG: ', tag)
    print('URL: ', tag.get('href', None))
    # print('CONTENT: ', tag.contents[0])
    # print('ATTRs: ', tag.attrs)
    #print(tag.get('href', None))