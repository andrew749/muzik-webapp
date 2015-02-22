window.onload=function(){

}
var canvas=document.getElementById("mainbackground");
var context=canvas.getContext("2d");
window.requestAnimFrame = (function(callback) {
    return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
        function(callback) {
        window.setTimeout(callback, 1000 / 60);
    };
})();

function drawRectangle(myRectangle, context) {
    context.beginPath();
    context.rect(myRectangle.x, myRectangle.y, myRectangle.width, myRectangle.height);
    context.fillStyle="rgba(66,66,66,0.5)";
    context.fill();
}
function animate(myRectangle, canvas, context, startTime) {
    // update
    var time = (new Date()).getTime() - startTime;

    var linearSpeed = 10;
    // pixels / second
    var newY = linearSpeed * time / 1000;

    if(newY < canvas.height - myRectangle.height - myRectangle.borderHeight / 2) {
        myRectangle.y = newY;
    }

    // clear
    context.clearRect(0, 0, canvas.width, canvas.height);

    drawRectangle(myRectangle, context);

    // request new frame
    requestAnimFrame(function() {
        animate(myRectangle, canvas, context, startTime);
    });
}
var myRectangle = {
    x: 0,
    y: 0,
    width: 100,
    height: 50,
    borderWidth: 5
};
setTimeout(function() {
    var startTime = (new Date()).getTime();
    animate(myRectangle, canvas, context, startTime);
}, 1000);