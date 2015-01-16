function entry(title, url){
    this.title=title;
    this.url=url;

}
$(document).ready(function(){
    var downloadsnllink="http://www.downloads.nl/results/mp3/1/";//add string of song to end
    $("#searchform").submit(function(e){
        e.preventDefault();

    });
    $("#searchbutton").click(function(e){
        e.preventDefault();
        var searchString=$("#searchtext").val();
        console.log();
        getSongs(searchString);

    });
    function getSongs(songName){
        console.log(songName);
        $.ajax({
            url:  "/search",
            type: 'GET',
            data:{'songname':songName},
            datatype:'jsonp',
            success: function(data) {
                console.log(data);
                $("body").append(data);
            }
        });
    }

});
