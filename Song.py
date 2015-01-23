import json
class Song:
    def __init__(self,title, url=None):
        self.title=title
        self.url=url
    def songToJson(self):
        return json.dumps({"title":self.title,"url":self.url,"albumUrl":self.album})
    def setAlbumArtURL(self, albumArtUrl):
        self.album=albumArtUrl
def allSongsToJson(songs):
    jsonstring=""
    return json.dumps([{"title":x.title,"url":x.url}for x in songs],indent=4)
