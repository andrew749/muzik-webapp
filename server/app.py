from flask import Flask, url_for
import requests
from lxml import html
import pdb
import json
from urllib.parse import quote
app=Flask(__name__)
downloadsnllink="http://www.downloads.nl/results/mp3/1/";#add string of song to end
#Seaches the site and returns an array of links
#TODO need to return object of song
def searchDownloadNL(songName):
    print ("started")
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    url=downloadsnllink+str(quote(songName))
    page=requests.get(url, headers=header)
    print ( url)
    tree=html.fromstring(page.text)
    songs=tree.xpath("//div/a[@onclick]/@href")
    songArray=[]
    for song in songs:
        songArray.append("www.downloads.nl"+song)
        print(song)
    return song
@app.route('/search')
def searchForSongs():
    print("1")
    links=searchDownloadNL("hooked on a feeling")        
    return (links)
if __name__ == '__main__':
    app.run(debug=True)


