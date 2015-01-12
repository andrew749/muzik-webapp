import json
class Song:
    def __init__(self,title, url):
        self.title=title
        self.url=url
    def songToJson(self):
        return json.dumps({"title":self.title,"url":self.url})