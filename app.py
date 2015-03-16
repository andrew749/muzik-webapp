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
app=Flask(__name__)
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
downloadsnllink="http://www.downloads.nl/results/mp3/1/";#add string of song to end
#Seaches the site and returns an array of linksmum
#TODO implement groove shark
#TODO implement goear
#TODO implement yourlisten
def searchDownloadNL(songName):
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
#method to search local datastore and see if there is a verified link
def getVerifiedLinks(songName):

    return False;
"""
This function searches youtube but is too slow.
"""
def followTrendingMP3Link(url):
    return None
def searchYouTube(songName):
    url="https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyBSH5Wy0l4XSTif-8StQjmtJCcqu_uHE2c&q="+str(quote(songName)+"&max-results=25")
    page=requests.get(url)
    temp=json.loads(page.text)
    results=temp["items"]
    songArray=[]
    for element in results:
        try:
            name=element["snippet"]["title"]
            url="https://www.youtube.com/embed/"+element["id"]["videoId"]+"?rel=0"
            songArray.append(Song(name,url))
        except Exception as e:
            print(e)
    return songArray
"""
This function searches MP3 Skull
"""
def searchMP3Skull(songName):
    url="http://mp3skull.com/mp3/"+ str(songName.replace(' ','_')+".html")
    page=requests.get(url,headers=header)
    tree=html.fromstring(page.text)
    songs=tree.xpath("//div[@id='song_html']//a[text()='Download']/@href")
    names=tree.xpath("//div[@id='song_html']//div/div/b/text()")
    i=0
    songArray=[]
    for x in range(len(songs)):
        if(i>100):
            break
        s=Song(names[x],songs[x])
        songArray.append(s)
        i+=1
    return (songArray)
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
    links=searchMP3Skull(name)
    links+=searchDownloadNL(name)
    links+=searchYouTube(name)
    return (allSongsToJson(links))
if __name__ == '__main__':
    app.run(debug=True)


