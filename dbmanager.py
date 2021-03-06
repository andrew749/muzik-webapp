import pymysql
import pdb
import json
import Song
import os

def connect():
    conn=pymysql.connect(host=os.environ['RDS_HOSTNAME'],port=int(os.environ['RDS_PORT']),user=os.environ['RDS_USERNAME'],passwd=os.environ['RDS_PASSWORD'],db="Muzik")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS entries (id INT AUTO_INCREMENT NOT NULL, songtitle varchar(255) unique, url MEDIUMTEXT, artist varchar(255), albumArtUrl varchar(255), verified integer,PRIMARY KEY (id))')
    return (conn,cursor)

"""Creates a song Entry in the main table"""
def addSong(title,artist,albumArtUrl):
    instance=connect()
    conn=instance[0]
    cursor=instance[1]
    cursor.execute("""INSERT IGNORE INTO entries (`songtitle`, `url`, `artist`, `albumArtUrl`, `verified`) VALUES(%s,'[]',%s,%s,0)""",[conn.escape_string(title),artist,conn.escape_string(albumArtUrl)])
    conn.commit()
    closeConnection(conn)

"""Adds a song result. assuming song object is created"""
def addSongResult(name,title,url):
    instance=connect()
    conn=instance[0]
    cursor=instance[1]
    cursor.execute("""SELECT * FROM entries WHERE songtitle=%s""",[conn.escape_string(name)])
    row=cursor.fetchone()
    data=json.loads(row[2])
    data.append({title:url})
    cursor.execute("""UPDATE entries SET url=%s WHERE songtitle=%s """,[json.dumps(data),conn.escape_string(name)])
    conn.commit()
    closeConnection(conn)

"""Get all the entries of a particular song"""
def getSongEntries(name):
    instance=connect()
    conn=instance[0]
    cursor=instance[1]
    cursor.execute("""SELECT * FROM entries WHERE songtitle LIKE %s""",(conn.escape_string(name),))
    song=cursor.fetchone()
    if song is None:
        return None
    s=Song.Song(name,None,song[3],song[4],song[5])
    flag=0
    for x in json.loads(song[2]):
        flag=1
        for (k,v) in x.items():
            s.addURL(k,v)
    if(flag == 1):
        return s
    else:
        return None
    closeConnection(conn)

def printTables(name):
    instance=connect()
    conn=instance[0]
    cursor=instance[1]
    print("Main Table")
    for row in cursor.execute("SELECT * FROM entries"):
        print(row)
    closeConnection(conn)


def closeConnection(conn):
    conn.close()
