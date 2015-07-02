import sqlite3
conn=sqlite3.connect('muzik.db')

cursor=conn.cursor()

def createTable():
    cursor.execute('''CREATE TABLE entries
             (title text, artist text, albumArtUrl text, verified integer)''')