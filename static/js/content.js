function entry(title, url){
    this.title=title;
    this.url=url;
}
var firsttime=true;
var audioPlayer=0;
var songArray=[];
var contentMain;
var spinner;
$(document).ready(function(){
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
    $("#content").height(0);
    $(".page").next().remove();
    var searchString=$("#searchtext").val();
    getSongs(searchString);

}
function handleSearchClick(e){
    $("#content").empty();
    $("#content").height(0);
    $(".page").next().remove();
    $('#searchtext').val(e);
    getSongs(e);
}

function goBack(){
    $("#content").empty();
    $(".page").next().remove();
    $('#content').append(contentMain).masonry();
    $("#backbutton").addClass("deactivatedarrow")
}
var opts = {
    lines: 13, // The number of lines to draw
    length: 20, // The length of each line
    width: 10, // The line thickness
    radius: 30, // The radius of the inner circle
    corners: 1, // Corner roundness (0..1)
    rotate: 0, // The rotation offset
    direction: 1, // 1: clockwise, -1: counterclockwise
    color: '#000', // #rgb or #rrggbb or array of colors
    speed: 1, // Rounds per second
    trail: 60, // Afterglow percentage
    shadow: false, // Whether to render a shadow
    hwaccel: false, // Whether to use hardware acceleration
    className: 'spinner', // The CSS class to assign to the spinner
    zIndex: 2e9, // The z-index (defaults to 2000000000)
    top: '50%', // Top position relative to parent
    left: '50%', // Left position relative to parent
    padding:10
};
function showLoadingDialog(){
    $('#spinner').removeClass('hidden');
    $("#spinner").addClass("dialog");
    var target=document.getElementById("spinner");
    spinner = new Spinner(opts).spin(target);
}
function stopLoadingDialog(){
    spinner.stop();
    $('#spinner').removeClass('dialog');
    $('#spinner').addClass('hidden');
}
var request;
function backArrowHandle(){
    $("#backbutton").removeClass("deactivatedarrow");
    $("#backbutton").click(function(){
        goBack();
        stopLoadingDialog();
        request.abort();
    });
}
function getSongs(songName){
    console.log(songName);
    backArrowHandle();
    showLoadingDialog();
    request=$.ajax({
        url:  "/search",
        type: 'GET',
        data:{'songname':songName},
        datatype:'jsonp',
        success: function(data) {
            stopLoadingDialog();
            data=JSON.parse(data);
            songArray=[];
            for (var y in data.url){
                var x=data.url[y];
                if(x!=null){
                    var element=$("<div/>").addClass("outerelement col-md-2");
                    var innerelement=$("<div/>").addClass("element result-element").attr('id',y);
                     var key=Object.keys(x);
                    var title=$("<h4/>").text(key);
                    element.append(innerelement);
                    innerelement.append(title);
                    $('#content').append(element);
                    songArray.push(x[key]);
                }
            }
            $('body').on('click', '.element', function() {
                // do something
                $('.activatedEntry').removeClass('activatedEntry');
                $(this).addClass("activatedEntry");
                playSong(songArray[this.id]);

            });
            $("#content").masonry({itemSelector:'.outerelement',isFitWidth:true, isAnimated:true});
        }
    });
}
function addSource(path){
    $("#ap").attr('src',path).trigger("play");
}
var playing=false;
function playSong(link){
    if(firsttime){
        $("#playerbar").css("display","block");
    }
    $('body').keyup(function(e){
        var play=$('#ap')[0];
        e.preventDefault();
        if(!$('#searchtext').is(":focus")){
            if(e.keyCode==32){
                if(play.paused==false){
                    play.pause();
                }
                else{
                    play.play();
                }
            }
        }
    });
    //handle adding the audio player to the page.
    if(!audioPlayer){
        $("iframe").remove();
        $("#playerholder").append($("<audio />",{autoPlay:'autoplay',controls:'controls', id:"ap", class:"col-md-12"}));
        audioPlayer=1;
    }
    addSource(link);
}
