
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
from selenium import webdriver
url="http://www.mp3raid.ws/download/"
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
def getSongs(songName):
    concaturl=url+songName.replace(" ","_")+".html"
    page=requests.get(concaturl,headers=header)
    driver=webdriver.Firefox()
    driver.get(concaturl)
    driver.find_elements(By.XPATH,"//*[@class='index1']")
    songArray=[]
    for song in elements:
        #pdb.set_trace()
        print (song.xpath("strong/text()"))
        driver.click(song)
        #nexturl=song.xpath("a[@class='dl']")
        #page2=requests.get(nexturl,header)
        #importanturl=page2.xpath("#ssilka//a/@href")
        #songArray.append(Song(page2.xpath("//")))

getSongs("hooked on a feeling")
