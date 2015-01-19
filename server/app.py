from flask import Flask, url_for, request, render_template
import requests
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
def searchYouTube(songName):
    url=""
    songArray=[]
    return songArray
def searchMP3Skull(songName):
    url="http://mp3skull.com/mp3/"+ str(songName.replace(' ','_')+".html")
    print(url)
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
        s=songArray.append(s)
        i+=1
    return (songArray)
@app.route('/')
def serveGUI():
    return render_template('index.html')
@app.route('/search')
def searchForSongs():
    name = request.args.get('songname')
    links=[]
    links=searchDownloadNL(name)
    links+=searchMP3Skull(name)
    return (allSongsToJson(links))
if __name__ == '__main__':
    app.run(debug=True)


