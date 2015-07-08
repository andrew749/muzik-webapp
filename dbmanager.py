import pymysql
import pdb
import json
import Song
import os
conn=pymysql.connect(host=os.environ['RDS_HOSTNAME']+":"+os.environ['RDS_PORT'],user=os.environ['RDS_USERNAME'],passwd=os.environ['RDS_PASSWORD'],db="Muzik")
bcursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS entries (title text unique,url text, artist text, albumArtUrl text, verified integer)')


"""Creates a song Entry in the main table"""
def addSong(title,artist,albumArtUrl):
    cursor.execute('INSERT OR IGNORE INTO entries VALUES(?,"[]",?,?,0)',[title,artist,albumArtUrl])
    conn.commit()

"""Adds a song result. assuming song object is created"""
def addSongResult(name,title,url):
    cursor.execute('SELECT * FROM entries WHERE title=?',[name])
    row=cursor.fetchone()
    data=json.loads(row[1])
    data.append({title:url})
    cursor.execute('UPDATE entries SET url=? WHERE title=? ',[json.dumps(data),name])
    conn.commit()

"""Get all the entries of a particular song"""
def getSongEntries(name):
    cursor.execute('SELECT * FROM entries WHERE title=?',[name])
    song=cursor.fetchone()
    if song is None:
        return None
    s=Song.Song(name,None,song[2],song[3],song[4])
    flag=0
    for x in json.loads(song[1]):
        flag=1
        for (k,v) in x.items():
            s.addURL(k,v)
    if(flag == 1):
        return s
    else:
        return None

def printTables(name):
    print("Main Table")
    for row in cursor.execute("SELECT * FROM entries"):
        print(row)


def closeConnection():
    conn.close()
