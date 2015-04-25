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
url="http://www.mp3raid.ws/download/"
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
def getSongs(songName):
    end=songName.replace(" ","_")+".html"
    concaturl=url+end
    page=requests.get(concaturl,headers=header)
    tree=html.fromstring(page.text)
    elements=tree.xpath("//*[@class='index1']//a[@class='dl']")
    songArray=[]
    for song in elements:
        nexturl="http://www.mp3raid.ws/search/ddl/"+song.xpath("@id")[0]+"/"+end
        print(nexturl)
        page2=requests.get(nexturl,headers=header)
        tree2=html.fromstring(page2.text)
        pdb.set_trace()
        songName=tree2.xpath("//table/tr/*[1]/td/*[2]/text()")
        print(songName)
        pdb.set_trace()
        songURL=tree2.xpath("//table/tr/*[2]/td/*[2]/text()")
        print(songURL)
        songArray.append(Song(songName,songURL))

getSongs("hooked on a feeling")
