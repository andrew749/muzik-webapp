from flask import Flask, url_for, request, render_template
import requests
from lxml import html
import lxml
import json
from lxml import etree
from Song import *
from urllib.parse import quote
import pdb
from urllib.request import urlopen,Request
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
def searchDownloadNL(songName):
    downloadsnllink="http://www.downloads.nl/results/mp3/1/";#add string of song to end
    url=downloadsnllink+str(quote(songName))
    page=requests.get(url, headers=header)
    tree=html.fromstring(page.text)
    elements=tree.xpath("//a[@class='tl j-lnk']")
    songArray=[]
    for song in elements:
        songLink=song.xpath("@href")
        songText=song.xpath("b//span/text()")
        print (songLink," ",songText)
        s=Song(songName,"http://www.downloads.nl"+songLink[0])
        songArray.append(s)
    return songArray

