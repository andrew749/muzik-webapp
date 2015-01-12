from flask import Flask, url_for
import requests
from lxml import html
from urllib.parse import quote
app=Flask(__name__)
downloadsnllink="http://www.downloads.nl/results/mp3/1/";#add string of song to end

def searchDownloadNL(songName):
    print ("started")
    url=downloadsnllink+str(quote(songName))
    page=requests.get(url)
    print ( url)
    tree=html.fromstring(page.text)
    song=tree.xpath("//a[@target='_blank']")
    print(song)
    return song
@app.route('/search')
def searchForSongs():
    print("1")
    searchDownloadNL("hooked on a feeling")
    return ("done")
if __name__ == '__main__':
    app.run(debug=True)


