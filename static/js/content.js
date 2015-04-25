function entry(title, url){
  this.title=title;
  this.url=url;
}
var audioPlayer=0;
var songArray=[];
var contentMain;
$(document).ready(function(){
  contentMain=$(".outerelement");
  var $container = $('#content');
  $container.masonry('bindResize')
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
  getSongs(e);

}

function goBack(){
  $("#content").empty();
  $(".page").next().remove();
  $('#content').append(contentMain).masonry();
  $("#backbutton").addClass("deactivatedarrow")
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
        $('#content').append(element);
        songArray.push(data[x].url[0]);
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
var isYoutube=false;
function playSong(link){
  //handle adding the audio player to the page.
  if(!audioPlayer){
    //if(link.search("youtube")){
      //isYoutube=true;
      //$("audio").remove();
      //$("#playerholder").append($("<iframe/>",{height:100, width:500}));

    //}else{
      isYoutube=false;
      $("iframe").remove();
      $("#playerholder").append($("<audio />",{autoPlay:'autoplay',controls:'controls', id:"ap", class:"col-md-12"}));

    //}
    audioPlayer=1;
  }
  if(!isYoutube){
    addSource(link);
  }else{
    $("iframe").attr("src", link);
  }

}
