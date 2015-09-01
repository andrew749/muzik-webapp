import imports
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
def searchMP3Skull(songName):
    url="http://mp3skull.com/mp3/"+ str(songName.replace(' ','_')+".html")
    songArray = []
    try:
        page=requests.get(url,headers=header)
        tree=html.fromstring(page.text)
        songs=tree.xpath("//div[@id='song_html']//a[text()='Download']/@href")
        names=tree.xpath("//div[@id='song_html']//div/div/b/text()")
        i=0
        for x in range(len(songs)):
            if(i>30):
                break
            songArray.append({names[x]:songs[x]})
            i+=1
    except:
        pass
    return (songArray)
