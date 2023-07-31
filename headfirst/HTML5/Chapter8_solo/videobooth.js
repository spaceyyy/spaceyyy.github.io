/* videobooth.js */

var videos = {
  video1: "video/demovideo1",
  video2: "video/demovideo2"
}

var effectFunction = null;


window.onload = function() {

  var video = document.getElementById("video");
  video.src = videos.video1 + getFormatExtension();
  video.load();

  // add click handlers to control anchors
  var controlLinks = document.querySelectorAll("a.control");
  for (var i = 0; i < controlLinks.length; i++) {
    controlLinks[i].onclick = handleControl;
  }

  //add click handlers to effect anchors
  var effectLinks = document.querySelectorAll("a.effect");
  for (var i = 0; i < effectLinks.length; i++) {
    effectLinks[i].onclick = setEffect;
  }

  // add click handlers to videoSelection anchors
  var videoLinks = document.querySelectorAll("a.videoSelection");
  for (var i = 0; i < videoLinks.length; i++) {
    videoLinks[i].onclick = setVideo;
  }

  // add click handlers to video play
  // video.onplay = processFrame;
  // video.onended = endedHandler;
  video.addEventListener("play", processFrame, false);
  video.addEventListener("ended", endedHandler, false);

  pushUnpushButtons("video1", []);
  pushUnpushButtons("normal", []);
}


function setEffect(e) {
  var id = e.target.getAttribute("id");

  if (id == "normal") {
    pushUnpushButtons("normal", ["western", "noir", "scifi"]);  // pushes "normal", unpushes buttons in array
    effectFunction = null;
    // alert("normal button pressed");
  } else if (id == "western") {
    pushUnpushButtons("western", ["normal", "noir", "scifi"]);
    effectFunction = western;
    // alert("western button pressed");
  } else if (id == "noir") {
    pushUnpushButtons("noir", ["normal", "western", "scifi"]);
    effectFunction = noir;
    // alert("noir button pressed");
  } else if (id == "scifi") {
    pushUnpushButtons("scifi", ["normal", "western", "noir"]);
    effectFunction = scifi;
    // alert("scifi button pressed");
  }
}


function setVideo(e) {
  var id = e.target.getAttribute("id");
  var video = document.getElementById("video");

  if (id == "video1") {
    pushUnpushButtons("video1", ["video2"]);
  } else if (id == "video2") {
    pushUnpushButtons("video2", ["video1"]);
  }
  video.src = videos[id] + getFormatExtension();  // adds file extension to the end of video
  video.load();
  video.play();

  pushUnpushButtons("play", ["pause"]);
}


function getFormatExtension() {
  var video = document.getElementById("video");

  if (video.canPlayType("video/mp4") != "") {  // we know we'll only get "maybe" and empty string as answers,
    return ".mp4";                             // so we'll just make sure our matching type doesn't result in an empty string.
  } else if (video.canPlayType("video/webm") != "") {
    return ".webm";
  } else if (video.canPlayType("video/ogg") != "") {
    return ".ogv";
  }
}


function handleControl(e) {
  var id = e.target.getAttribute("id");
  var video = document.getElementById("video");

  if (id == "play") {
    pushUnpushButtons("play", ["pause"]);
    if (video.ended) {
      video.load();
    }
    video.play();
    // alert("play button pressed");
  } else if (id == "pause") {
    pushUnpushButtons("pause", ["play"]);  // depending on which btn it was, we alter the interface to reflect the
    video.pause();
    // alert("pause button pressed");         // btn that was pushed. For instance if pause was pushed then play shouldn't be.
  } else if (id == "loop") {
    if (isButtonPushed("loop")) {
      pushUnpushButtons("", ["loop"]);  // using a helper function to make sure the onscreen btn states are taken care of,
      // alert("loop button pressed");
    } else {                          // it's called `pushUnpushButtons` and it takes a pushed btn along w/ an array of unpushed
      pushUnpushButtons("loop", []);  // btns and updates the interface to reflect that state.
      // alert("loop button pressed");
    }
    video.loop = !video.loop;  // loops vid
  } else if (id == "mute") {
    if (isButtonPushed("mute")) {
      pushUnpushButtons("", ["mute"]);
      // alert("mute button pressed");
    } else {
      pushUnpushButtons("mute", []);  // various btns have different semantics. `play` and `pause` are like true
      // alert("mute button pressed");   // btns, while `mute` and `loop` are like toggle btns.
    }
    video.muted = !video.muted;  // mutes vid
  }
}

//
// "ended" event handler
//
function endedHandler(e) {
  pushUnpushButtons("", ["play"]);
}


function processFrame(e) {
  var video = document.getElementById("video");

  if (video.paused || video.ended) {
    return;
  }

  var bufferCanvas = document.getElementById("buffer");
  var displayCanvas = document.getElementById("display");
  var buffer = bufferCanvas.getContext("2d");
  var display = displayCanvas.getContext("2d");

  buffer.drawImage(video, 0, 0, bufferCanvas.width, bufferCanvas.height);
  var frame = buffer.getImageData(0, 0, bufferCanvas.width, bufferCanvas.height);
  // not in .zip file  buffer.drawImage(video, 0, 0, bufferCanvas.width, displayCanvas.height);
  // not in .zip file  var frame = buffer.getImageData(0, 0, bufferCanvas.width, displayCanvas.height);
  var length = frame.data.length / 4;  // each pixels have four values, RGBA

  for (var i = 0; i < length; i++) {   // grabbing pixels per frame
    var r = frame.data[i * 4 + 0];     // starts at index 0 which is R
    var g = frame.data[i * 4 + 1];
    var b = frame.data[i * 4 + 2];
    if (effectFunction) {
      effectFunction(i, r, g, b, frame.data);
    }
  }
  display.putImageData(frame, 0, 0);

  setTimeout(processFrame, 0);  // works on firefox & IE, does not work on Chrome for effects
	// try this line instead of the setTimeout above if you are on Chrome
	//requestAnimationFrame(processFrame);  // still does not work on Chrome, use ctrl + shift i
}


function noir(pos, r, g, b, data) {  // function called once per pixel in the video frame. last paramater is a reference to the frame data array in the canvas.
  var brightness = (3*r + 4*g  + b) >>> 3;  // bitwise oper that shifts the bits in the # value over to modify the #
  if (brightness < 0) brightness = 0;
  data[pos * 4 + 0] = brightness;
  data[pos * 4 + 1] = brightness;  // assigning each component in the canv img to that brgtness
  data[pos * 4 + 2] = brightness;  // `brightness` at the end has the affect of setting the pxl to a grey scale value
}                                  // that corresponds to the pixel's overall brightness.


function western(pos, r, g, b, data) {
  var brightness = (3*r + 4*g + b) >>> 3;
  data[pos * 4 + 0] = brightness + 40;
  data[pos * 4 + 1] = brightness + 20;
  data[pos * 4 + 2] = brightness - 20;
  data[pos * 4 + 3] = 255;  // 220;
}


function scifi(pos, r, g, b, data) {
  var offset = pos * 4;
  data[offset] = Math.round(255 - r);
  data[offset + 1] = Math.round(255 - g);
  data[offset + 2] = Math.round(255 - b);
}

/*
* bwcartoon is an extra filter for an excersice
*/
function bwcartoon(pos, r, g, b, outputData) {
  var offset = pos * 4;
  if (outputData[offset] < 120) {
    outputData[offset] = 80;
    outputData[++offset] = 80;
    outputData[++offset] = 80;
  } else {
    outputData[offset] = 255;
    outputData[++offset] = 255;
    outputData[++offset] = 255;
  }
  outputData[++offset] = 255;
  ++offset;
}


function pushUnpushButtons(idToPush, idArrayToUnpush) {
  if (idToPush != "") {  // check to make sure the `id` of the button to push is not empty
    var anchor = document.getElementById(idToPush);  // grab the anchor element using that id
    var theClass = anchor.getAttribute("class");  // and get the class attribute
    if (!theClass.indexOf("selected") >= 0) {
      theClass = theClass + " selected";  // 'press' the button by adding the "selected" class to the anchor
      anchor.setAttribute("class", theClass);
      var newImage = "url(images/"+ idToPush + "pressed.png)";  // update the bkgd img of the <a> so it covers up
      anchor.style.backgroundImage = newImage;  // that btn w/ a 'button pressed' image. So 'pause' uses the "pausedpressed.png" image
    }
  }

  for (var i = 0; i < idArrayToUnpush.length; i++) {  // to unpush btns, we loop thru the array of ids to unpush, grabbing each <a>
    anchor = document.getElementById(idArrayToUnpush[i]);
    theClass = anchor.getAttribute("class");
    if (theClass.indexOf("selected") >= 0) {  // make sure the btn is really pushed (if it is, it will have a "selected" class)
      theClass = theClass.replace("selected", "");  // remove "selected" from the class
      anchor.setAttribute("class", theClass);
      anchor.style.backgroundImage = "";  // remove the bkgd img so we see the unpushed button
    }
  }
}


function isButtonPushed(id) {  // checks to see if a btn is pushed. It takes the `id` of an anchor
  var anchor = document.getElementById(id);
  var theClass = anchor.getAttribute("class");
  return (theClass.indexOf("selected") >= 0);  // returns `true` if the <a> has the "selected" class
}


// in the future create a video effect that is psychedlic or any other type of theme/archetype
