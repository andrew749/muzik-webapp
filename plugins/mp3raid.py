from imports import *
url="http://www.mp3raid.info/download/"
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
def getMP3RaidSongs(songName):
    end=songName.replace(" ","_")+".html"
    concaturl=url+end
    songArray = []
    try:
        page=requests.get(concaturl,headers=header,timeout=3)
        tree=html.fromstring(page.text)
        elements=tree.xpath("//*[@class='index1']//a[@class='dl']")
        for song in elements:
            nexturl="http://www.mp3raid.info/search/ddl/"+song.xpath("@id")[0]+"/"+end
            page2=requests.get(nexturl,headers=header)
            tree2=html.fromstring(page2.text)
            songName=tree2.xpath("//table/tr/*[2]/text()")[0]
            songURL=tree2.xpath("//table/tr/*[2]/text()")[1]
            songArray.append({songName:songURL})
    except Exception as e:
        print ("mp3raid failed")
        print (e)
    return songArray
