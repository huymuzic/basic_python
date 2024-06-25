import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://www.dr-chuck.com/page1.htm"
for line in urllib.request.urlopen(url):
    print(line.strip())
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    fhand = urllib.request.urlopen(tag.get('href', None))
    for line in fhand:
        print(line.decode().strip())