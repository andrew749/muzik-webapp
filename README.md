<h1>Play-webapp</h1>

<h2>A website that streams free music from a variety of sources.</h2>
Currently play is DMCA compliant. If for any change your conntent appears without consent, informme and I will take it down immediately.
<h3>API Usage
</h3>
<h4>Query</h4>
Form an url with query parameter songname.
```javascript
http://example.com/search?songname=NAME_OF_SONG
```
<h4>Result</h4>
The server will respond with a json encoded file with the following form:
```javascript
{
title:"SongName",
url:[array of urls]
albumArt:"album art url",
artist:"song artist",
verified:"whether or not the song has a verified link"
}
```
<h3>Reporting Issues</h3>
To report any api issues, email me at andrewcod749@gmail.com
 Live @ muzik-api.herokuapp.com
