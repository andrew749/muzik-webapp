import sqlite3
import pdb
conn=sqlite3.connect('muzik.db')

cursor=conn.cursor()

def createTable():
    cursor.execute('CREATE TABLE entries (title text, artist text, albumArtUrl text, verified integer)')

def createEntryTable(name):
    cursor.execute('CREATE TABLE '+name+' (url text)')

"""Creates a song Entry in the main table"""
def addSong(title,artist,albumArtUrl):
    cursor.execute('INSERT INTO entries VALUES(?,?,?,0)',[title,artist,albumArtUrl])
    conn.commit()
    
"""Adds a song result to one of the song tables"""
def addSongResult(name, url):
    obj=cursor.execute('SELECT * FROM entries WHERE title=?',name)
    if(obj==None):
        addSongEntry(name,name,"Unknown Artist","")
    obj2=cursor.execute('SELECT * FROM '+name +' WHERE title=?',name)
    if(obj2==None):
        createEntryTable(name)
    cursor.execute('INSERT INTO '+name+' VALUES('+url+')')
    conn.commit()
    
"""Get all the entries of a particular song"""
def getSongEntries(name):
    song=cursor.execute('SELECT * FROM entries WHERE title=?',name)    
    pdb.set_trace()
    if(song.count > 0):
        s=Song(name,None,song.artist,song.albumArtUrl,"UnknownAlbum")
        for x in cursor.execute('SELECT * FROM ?',name):
            songEntries.append(Song(name,))
        
def printTables(name):
    print("Main Table")
    print(cursor.execute("SELECT * FROM entries"))
def closeConnection():
    conn.close()
    
#createTable()
printTables("tets")
addSong("Hooked","blue","why")
printTables("test")
closeConnection()