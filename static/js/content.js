function entry(title, url){
    this.title=title;
    this.url=url;

}
var audioPlayer=0;
var songArray=[];
var contentMain;
$(document).ready(function(){
    var downloadsnllink="http://www.downloads.nl/results/mp3/1/";//add string of song to end
    contentMain=$(".outerelement");
    var $container = $('#content');
    // initialize
    $container.imagesLoaded( function() {
        $container.masonry({itemSelector:'.outerelement',isFitWidth:true});
    });
    var msnry = $container.data('masonry');
    $("#searchform").submit(function(e){
        e.preventDefault();

    });
    $("#searchbutton").click(function(e){
        e.preventDefault();
        handleSearch(e);

    });
    $('#searchtext').keydown(function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            handleSearch(e);
        }
    });

});
function handleSearch(e){
    $("#content").empty();
    $(".page").next().remove();
    var searchString=$("#searchtext").val();
    getSongs(searchString);

}
function handleSearchClick(e){
    $("#content").empty();
    $(".page").next().remove();
    getSongs(e);

}

function goBack(){
    $("#content").empty();
    $(".page").next().remove();
    console.log(contentMain);
    $('#content').append(contentMain).masonry('appended',element,true);
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
            $("#backbutton").removeClass("deactivatedarrow");
            $("#backbutton").click(function(){
                goBack();
            });
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
                $('.activatedEntry').removeClass('activatedEntry');
                $(this).addClass("activatedEntry");
                playSong(songArray[this.id]);

            });
            var $container = $('#content');

            // $container.masonry({itemSelector:'.outerelement',isFitWidth:true});
        }
    });
}

function addSource(path){
    $("#ap").attr('src',path).trigger("play");
}
function playSong(link){
    if(!audioPlayer){
        $("#playerholder").append($("<audio />",{autoPlay:'autoplay',controls:'controls', id:"ap", class:"col-md-12"}));
        audioPlayer=1;
    }
    addSource(link);
    console.log("doneadding");

}