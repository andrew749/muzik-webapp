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
import mp3skull
import DownloadNL
import YouTube

header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
app=Flask(__name__)
#Seaches the site and returns an array of linksmum
#TODO implement groove shark
#TODO implement goear
#TODO implement yourlisten
#method to search local datastore and see if there is a verified link
def getVerifiedLinks(songName):
    return False;
def followTrendingMP3Link(url):
    return None
"""
This function get the top 100 list from iTunes.
"""
def getTopHits():
    url="https://itunes.apple.com/us/rss/topsongs/limit=100/xml"
    page=requests.get(url,headers=header)
    tree=html.fromstring(page.content)
    names=tree.xpath("//entry//title/text()")
    art=tree.xpath("//entry//*[@height='170']/text()")
    i=0
    songArray=[]
    for x in range(len(names)):
        if(i>100):
            break
        s=Song(names[x])
        s.setAlbumArtURL(art[x])
        songArray.append(s)
        i+=1
    return songArray

@app.route('/top')
def getTop():
    elements=getTopHits()
    return (allSongsToJson(elements))

@app.route('/landing')
def serveLanding():
    return render_template('landingpage.html')

@app.route('/')
def serveGUI():
    elements=getTopHits()
    return render_template('index.html',elements=elements)

@app.route('/search')
def searchForSongs():
    name = request.args.get('songname')
    links=[]
    links=mp3skull.searchMP3Skull(name)
    links+=DownloadNL.searchDownloadNL(name)
    links+=YouTube.searchYouTube(name)
    return (allSongsToJson(links))

if __name__ == '__main__':
    app.run(debug=True)


