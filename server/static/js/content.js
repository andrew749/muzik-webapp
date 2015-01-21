function entry(title, url){
    this.title=title;
    this.url=url;

}
$(document).ready(function(){
    var downloadsnllink="http://www.downloads.nl/results/mp3/1/";//add string of song to end
    var $container = $('#content');
    var playerexists=0;
    // initialize
    $container.masonry({
        columnWidth: 200,
        itemSelector: '.item'
    });
    var msnry = $container.data('masonry');
    var songArray=[];
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

    function addSource(elem,path){
        $('<source />').attr('src',path).appendTo(elem);
    }
    function playSong(link){
        if(!playerexists){
        var player=$("<audio />",{autoPlay:'autoplay',controls:'controls'});
            playerexists=1;
        }else{
        player=$("audio");
        }
        addSource(player,link);
        $("#playerholder").append(player);
        console.log("doneadding");

    }

    function handleSearch(e){
        e.preventDefault();
        $("#content").empty();
        var searchString=$("#searchtext").val();
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
                var amount=30;
                var j=0;
                data=JSON.parse(data);
                songArray=[];
                for (var x in data){
                    if(j>amount)break;
                    j++;
                    var element=$("<div/>").addClass("outerelement col-md-3");
                    var innerelement=$("<div/>").addClass("element").attr('id',x);
                    var title=$("<h2/>").text(data[x].title);
                    element.append(innerelement);
                    innerelement.append(title);
                    $('#content').append(element).masonry('appended',element,true);
                    songArray.push(data[x].url);
                }
                $('body').on('click', '.element', function() {
                    // do something
                    playSong(songArray[this.id]);

                });

            }
        });
    }

});
