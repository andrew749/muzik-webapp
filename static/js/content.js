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
  //$(".page").next().remove();
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

function getSongs(songName){
  console.log(songName);
  showLoadingDialog();
  $.ajax({
    url:  "/search",
    type: 'GET',
    data:{'songname':songName},
    datatype:'jsonp',
    success: function(data) {
      stopLoadingDialog();
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
  if(firsttime){
  $("#playerbar").css("display","block");
  }
  //handle adding the audio player to the page.
  if(!audioPlayer){
    $("iframe").remove();
    $("#playerholder").append($("<audio />",{autoPlay:'autoplay',controls:'controls', id:"ap", class:"col-md-12"}));
    audioPlayer=1;
  }
  addSource(link);
}
