/* mightygumball.js */

/*
 * get the content of a JSON file using JSONP
 * update every 3 seconds.
 *
 */

var lastReportTime = 0;

window.onload = init;

function init() {
  var interval = setInterval(handleRefresh, 3000);
  handleRefresh();
}

//
// try to add a proxy server ahead of gumball url such as `https:cors-anywhere.heroku.app/[...gumball..]
// and 3 other alternative proxy servers and still receiving a error 404. I believe the issue is
// that the link no longer works, which checked to see if so and it did not, also found the original
// user's github saying the link is broken. Only odd thing is, when ran on my own file C:/Users...
// it works on all three HFHTML5 folders from spaceyyy.github, HFHTML5_solo, and hfhtml5, but only
// when all browsers are closed and only opened in one browser. For example: All browsers must be 
// closed, but only open each file from each directory on that specific browsing app, will run but not
// when open in different ones. Can only work when opened only on Chrome, only on Firefox, only on
// Edge, but will have in error if opened simultaneously on each one.
// Oddly enough, sometimes when I check the Network tab in the inspector and then in the Headers tab
// the Status Code is coming back as : 200 OK, but when copied the link and pasted, a 404 Not Found
// error re-occurs. Spent HOURS trying to figure out how the page is being repopulated with data and
// how the data is even being chosen, and coming up empty handed. Will need to speak to someone 
// about this, but moving on.
//
// in original ` url = "http:[...] + '&random' "
// can only populate if  ` url = "http" not "https" `but will not bypass error unless "https"
//
function handleRefresh() {
  console.log("here");
  var url = "http://gumball.wickedlysmart.com" +
              "?callback=updateSales" +
              "&lastreporttime=" + lastReportTime +
              "&random=" + (new Date()).getTime();
  var newScriptElement = document.createElement("script");
  newScriptElement.setAttribute("src", url);
  newScriptElement.setAttribute("id", "jsonp");
  var oldScriptElement = document.getElementById("jsonp");
  var head = document.getElementsByTagName("head")[0];
  if (oldScriptElement == null) {
    head.appendChild(newScriptElement);
  } else {
    head.replaceChild(newScriptElement, oldScriptElement);
  }
}

function updateSales(sales) {
  var salesDiv = document.getElementById("sales");
  for (var i = 0; i < sales.length; i++) {
    var sale = sales[i];
    var div = document.createElement("div");
    div.setAttribute("class", "saleItem");
    div.innerHTML = sale.name + " sold " + sale.sales + " gumballs";
    // salesDiv.appendChild(div);
    if (salesDiv.childElementCount == 0) {
      salesDiv.appendChild(div);
    } else {
      salesDiv.insertBefore(div, salesDiv.firstChild);
    }
  }

  if (sales.length > 0) {
    lastReportTime = sales[sales.length-1].time;
  }
}
