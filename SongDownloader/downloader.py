import sys
import os
import spotipy
import spotipy.util as util
username=""
if len(sys.argv)>1:
    username=sys.argv[1]
print (username)
token=util.prompt_for_user_token(username,'user-library-read',client_id='fd7c6f6f41ce496eb78490a59071e67d',client_secret='3cb0a046f8904f5d86d0b8eb43c323ad',redirect_uri='http://localhost:5000 ')
if(token):
    sp=spotipy.Spotify(auth=token)
    playlists=sp.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
