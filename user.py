#sample model for a user entry
class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def getName(self):
        return self.name
    def getSongList(self):
        return None
    def addToSongList(self, song):
        self.songs.append(song)
