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
import time
import _thread
import dbmanager
import sys
sys.path.append("plugins")
from plugins import imports
from plugins import mp3skull
from plugins import mp3raid
from plugins import DownloadNL
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}


application=Flask(__name__)

"""
This function get the top 100 list from iTunes.
"""
def getTopHits():
    url="https://itunes.apple.com/us/rss/topsongs/limit=100/xml"
    namespaces={'im':'http://itunes.apple.com/rss','xmlns':"http://www.w3.org/2005/Atom"}
    data={}

    #Checks for a temp file with the top hit information
    try:
        with open('hits','r') as f:
            data = json.loads(f.read())
        if(time.time()*1000-data['time']<86400000):
            return JsonToSongs(data['data'])
    except Exception:
        pass
    #Get the data from the apple
    songArray=[]
    page=requests.get(url,headers=header)
    tree=etree.fromstring(page.content)

    #Parse all of the results
    for x in tree.findall('xmlns:entry',namespaces):
        s=Song(x.find('im:name',namespaces).text)
        s.setArtist(x.find('im:artist',namespaces).text)
        s.setAlbumArtURL(x.find('im:image[@height="170"]',namespaces).text)
        songArray.append(s)
    f=open('hits','w')
    json.dump({'time':int(time.time()*1000),'data':allSongsToJson(songArray)},f)
    return songArray

@application.route('/top')
def getTop():
    elements=getTopHits()
    return (allSongsToJson(elements))

@application.route('/landing')
def serveLanding():
    return render_template('landingpage.html')

@application.route('/')
def serveGUI():
    elements=getTopHits()
    return render_template('index.html',elements=elements)

@application.route('/search')
def searchForSongs():
    name = request.args.get('songname')
    return search(name)

def getResults(name):
    links=[]
    links_mp3skull=mp3skull.searchMP3Skull(name)
    links_downloadnl=DownloadNL.searchDownloadNL(name)
    links_mp3raid=mp3raid.getMP3RaidSongs(name)
    if(links_mp3skull is not None):
        links+=links_mp3skull
    if(links_downloadnl is not None):
        links+=links_downloadnl
    if(links_mp3raid is not None):
        links+=links_mp3raid
    if(links is None):
        links_youtube=YouTube.searchYouTube(name)
        links+=links_youtube
    return links


def search(name):
    #escape character incase of bad stuff
    name.replace("'","\'");
    x = dbmanager.getSongEntries(name)
    if(x is not None):
        print("getting cached results Database")
        s = json.dumps(Song(name,x.url,x.artist,x.albumArt,x.album).songToJson(),indent=4)
        return s
    links=getResults(name)
    if len(links)>0:
        dbmanager.addSong(name,"Unknown Artist","")
        for y in links:
            for (k,v) in y.items():
                dbmanager.addSongResult(name,k,v)
        print ("done searching for ",name)
        return json.dumps(Song(name,links,"Unknown Artist","","").songToJson(),indent=4)
    return json.dumps({})


@application.route('/callback')
def handleCallback():
    pdb.set_trace()

def cacheTopHitResults():
    topHits = getTopHits()
    i=0
    for x in topHits:
        print("Searching for ",x.title.encode('utf-8'))
        search(x.title+" "+x.artist)
        if i==20:
            break
        else:
            i+=1

def runTopHitCachingAsync():
    _thread.start_new_thread(cacheTopHitResults,())

#runTopHitCachingAsync()

#cacheTopHitResults()

if __name__ == '__main__':
    application.run(debug=True,host="0.0.0.0",port=8080)
