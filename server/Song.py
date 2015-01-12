import json
class Song:
    def __init__(title, artist, url):
        self.title=title
        self.url=url
    def songToJson():
        json.dumps({"title":self.title,"url":self.url})