function entry(title, url){
    this.title=title;
    this.url=url;

}
$(document).ready(function(){
    var downloadsnllink="http://www.downloads.nl/results/mp3/1/";//add string of song to end
    var $container = $('#content');
    // initialize
    $container.masonry({
        columnWidth: 200,
        itemSelector: '.item'
    });
    var msnry = $container.data('masonry');

    $("#searchform").submit(function(e){
        e.preventDefault();

    });
    $("#searchbutton").click(function(e){
        handleSearch(e);

    });
    $('#searchtext').keydown(function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            handleSearch(e);
        }
    });
    function handleSearch(e){
        e.preventDefault();
        var searchString=$("#searchtext").val();
        console.log();
        getSongs(searchString);

    }
    function getSongs(songName){
        console.log(songName);
        $.ajax({
            url:  "/search",
            type: 'GET',
            data:{'songname':songName},
            datatype:'jsonp',
            success: function(data) {
                var row=$("\tr")
                var amount=30;
                var j=0;
                $("#content").empty();
                data=JSON.parse(data);
                for (var x in data){
                    if(j>amount)break;
                    j++;
                    var element=$('<div class="col-md-3 outerelement"><div class="element"><div><h2>'+data[x].title+'</h2></div><div><a href="'+data[x].url+'">'+data[x].url+'</a><audio controls> <source src="'+data[x].url+'"type="audio/mpeg">Your browser does not support the audio element.</audio></div></div></div>');
                    $('#content').append(element).masonry('appended',element,true);            
                }

            }
        });
    }

});
