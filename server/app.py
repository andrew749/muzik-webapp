from flask import Flask, url_for
app=Flask(__name__)
@app.route('/search')
def searchForSongs():
    return ("need content")
if __name__ == '__main__':
    app.run()

downloadsnllink="http://www.downloads.nl/results/mp3/1/";#add string of song to end
