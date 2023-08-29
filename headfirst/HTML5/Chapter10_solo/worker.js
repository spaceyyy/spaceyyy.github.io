//
// pingpong worker
//
onmessage = pingpong;

function pingpong(event) {
  if (event.data == "ping") {
    postMessage("pong");
  } else {
    // intentionally make an error!
    1/x;
  }
}

/*
onmessage = pingPong;

function pingPong(event) {
  if (event.data == "ping") {
    postMessage("pong");
  }
}
*/
