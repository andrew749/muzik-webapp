from imports import *
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

def searchDownloadNL(songName):
    downloadsnllink = "http://www.downloads.nl/results/mp3/1/{0}";#add string of song to end
    end = songName.replace(" ","_")
    url = (downloadsnllink.format(end))
    songArray = []
    try:
        page=requests.get(url, headers=header, timeout=3)
        tree=html.fromstring(page.text)
        elements=tree.xpath("//a[@class='tl j-lnk']")
        for song in elements:
            songLink=song.xpath("@href")
            songText=song.xpath("b//text()")
            name=""
            for i in songText:
                name+=i
            #print(name, songLink)
            s={name:"http://www.downloads.nl"+songLink[0]}
            songArray.append(s)
    except Exception as e:
        print ("DownloadNL Failed")
        print (e)
    return songArray
