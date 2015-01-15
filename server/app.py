from flask import Flask, url_for
import requests
from xml.dometree import ElementTree
from lxml import html
import pdb
import json
from Song import *
from urllib.parse import quote
app=Flask(__name__)
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
downloadsnllink="http://www.downloads.nl/results/mp3/1/";#add string of song to end
#Seaches the site and returns an array of links
def searchDownloadNL(songName):
    print ("started")
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    url=downloadsnllink+str(quote(songName))
    page=requests.get(url, headers=header)
    tree=html.fromstring(page.text)
    songs=tree.xpath("//div/a[@onclick]/@href")
    songArray=[]
    for song in songs:
        s=Song(songName,"www.downloads.nl"+song)
        songArray.append(s)
    return songArray
def searchMP3Skull(songName):
    url="http://mp3skull.com/mp3/"+ str(quote(songName))
    print(url)
    page=requests.get(url,headers=header)
    tree=html.fromstring(page.text)
    songs=tree.xpath("//div[@id='song_html']//a/@href")
    songArray=[]
    for song in songs:
        s=Song(songName,song)
        s=SongArray.append(s)
    return (songArray)
@app.route('/search')
def searchForSongs():
    print("1")
    links=searchDownloadNL("hooked on a feeling")
    links+=searchMP3Skull("hooked on a feeling")
    return (allSongsToJson(links))
if __name__ == '__main__':
    app.run(debug=True)


