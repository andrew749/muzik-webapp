import requests
from lxml import html
import lxml
import json
from lxml import etree
from Song import *
from urllib.parse import quote
import urllib.urlopen
import pdb
songName="Hooked on a feeling"
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml',}

url="https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyBSH5Wy0l4XSTif-8StQjmtJCcqu_uHE2c&q="+str(quote(songName))
print(url)
parser = etree.XMLParser(remove_blank_text=True)
page=request(url)
tree = etree.parse(page, parser)
root = tree.getroot()
namespaces = {'media':'http://search.yahoo.com/mrss/'}
items = iter(root.xpath('//entry/title/text()',
                   namespaces=namespaces))
for item in items:
    print (item)
