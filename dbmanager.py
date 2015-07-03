import sqlite3
import pdb
import json
import Song
conn=sqlite3.connect('muzik.db',check_same_thread=False)
conn.row_factory=sqlite3.Row
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS entries (title text unique,url text, artist text, albumArtUrl text, verified integer)')


"""Creates a song Entry in the main table"""
def addSong(title,artist,albumArtUrl):
    cursor.execute('INSERT OR IGNORE INTO entries VALUES(?,"[]",?,?,0)',[title,artist,albumArtUrl])
    conn.commit()
    
"""Adds a song result. assuming song object is created"""
def addSongResult(name,url):
    cursor.execute('SELECT * FROM entries WHERE title=?',[name])
    row=cursor.fetchone()
    array=json.loads(row[1])
    array.append(url)
    cursor.execute('UPDATE entries SET url=? WHERE title=? ',[json.dumps(array),name])
    conn.commit()
    
"""Get all the entries of a particular song"""
def getSongEntries(name):
    cursor.execute('SELECT * FROM entries WHERE title=?',[name])    
    song=cursor.fetchone()
    if song is None:
        return None
    s=Song.Song(name,[],song[2],song[3],song[4])
    flag=0
    for x in json.loads(song[1]):
        flag=1
        s.addURL(x)
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
    