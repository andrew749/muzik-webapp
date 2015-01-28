import requests
from lxml import html
import lxml
import json
from lxml import etree
from Song import *
from urllib.parse import quote
import urllib
import pdb
songName="Hooked on a feeling"
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml',}

url="http://gdata.youtube.com/feeds/api/videos?q="+str(quote(songName))+"&max-results=10&v=2"
print(url)
parser = etree.XMLParser(remove_blank_text=True)
print(1)
page=urllib.request.urlretrieve(url)
print (2)
tree = etree.parse(page, parser)
root = tree.getroot()
namespaces = {'media':'http://search.yahoo.com/mrss/'}
items = iter(root.xpath('//entry/title/text()',
                   namespaces=namespaces))
for item in items:
    print (item)
