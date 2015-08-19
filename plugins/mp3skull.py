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
def searchMP3Skull(songName):
    url="http://mp3skull.com/mp3/"+ str(songName.replace(' ','_')+".html")
    page=requests.get(url,headers=header)
    tree=html.fromstring(page.text)
    songs=tree.xpath("//div[@id='song_html']//a[text()='Download']/@href")
    names=tree.xpath("//div[@id='song_html']//div/div/b/text()")
    i=0
    songArray=[]
    for x in range(len(songs)):
        if(i>30):
            break
        songArray.append({names[x]:songs[x]})
        i+=1
    return (songArray)
