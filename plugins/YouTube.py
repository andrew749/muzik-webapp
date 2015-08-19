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

header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
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

