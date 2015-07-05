import json
"""
Takes parameters title, url, artist, album art url.

Can create json for songs or hits.

"""
class Song:
    def __init__(self,title, url=None,artist="Unknown Artist",albumArtUrl=None,album="Unkown Album"):
        self.verified=False
        self.title=title
        self.url=[url]
        self.artist=artist
        self.albumArt=albumArtUrl
        self.album=album
    def songToJson(self):
        return {"title":self.title,"url":self.url,"albumArt":self.albumArt,"artist":self.artist,"album":self.album,"verified":self.verified}
    def setAlbumArtURL(self, albumArtUrl):
        self.albumArt=albumArtUrl
    def addURL(self,songtitle,url):
        self.url.append({songtitle:url})
    def setArtist(self, artist):
        self.artist=artist
#condition should be true or false
    def setVerified(self,condition):
        self.verified=condition
    def deleteUrl(self, position):
        self.url.pop(position)
    def setAlbum(self,album):
        self.album=album
def allSongsToJson(songs):
    return json.dumps([x.songToJson()for x in songs],indent=4)
def JsonToSongs(j):
    songArray=[]
    for x in json.loads(j):
        s=Song(x['title'],x['url'],x['artist'],x['albumArt'],x['album'])
        songArray.append(s)
    return songArray
