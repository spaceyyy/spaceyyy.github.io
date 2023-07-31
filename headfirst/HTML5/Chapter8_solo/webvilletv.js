// GLOBAL VARIABLES
var position = 0;  // keeping track of video playing
var playlist;       // video playlist array
var video;          // reference to the video element

window.onload = function() {

  playlist = ["video/preroll",
              "video/areyoupopular",
              "video/destinationearth"];

  video = document.getElementById("video");

  video.addEventListener("ended", nextVideo, false);
  video.addEventListener("error", errorHandler, false);

  video.src = playlist[position] + getFormatExtension();
  video.load();
  video.play();

  alert("Playing " + video.currentSrc);
}


function nextVideo() {
  position++ ;    // increment the position in the playlist array
  if (position >= playlist.length) {
    position = 0;   // end of list, we'll just loop back around by setting the pos. to 0 again.
  }

  video.src = playlist[position] + getFormatExtension();   // src of the player to the next video
  video.load();
  video.play();

  alert("Playing " + video.currentSrc);
}


function getFormatExtension() {
  if (video.canPlayType("video/mp4") != "") {  // we know we'll only get "maybe" and empty string as answers,
    return ".mp4";                             // so we'll just make sure our matching type doesn't result in an empty string.
  } else if (video.canPlayType("video/webm") != "") {
    return ".webm";
  } else if (video.canPlayType("video/ogg") != "") {
    return ".ogv";
  }
}


function errorHandler() {
  var video = document.getElementById("video");
  if (video.error) {
    video.poster = "images/technicaldifficulties.jpg";
    alert(video.error.code);
  }
}
