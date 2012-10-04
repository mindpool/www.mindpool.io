var mindpoolLogin = function(assertion) {
  //console.log("onlogin");
  //console.log(assertion);
  var data = JSON.stringify({"assertion": assertion});
  //console.log("here's the jsonified data:");
  //console.log(data);
  var request = $.ajax({
    url: "/login",
    type: "POST",
    contentType: "text/json",
    data: data,
    dataType: "json"});
  request.done(function(data) {
    $("#persona-login").text(data.results);
  });
  request.fail(function(jqXHR, status) {
    //console.log(jqXHR);
    //console.log(status);
  });
};


var mindpoolLogout = function() {
  console.log("onlogout");
};


var mindpoolLoginOnClick = function() {
  $("#persona-login").text("logging in...");
  return navigator.id.request({
  siteName: "MindPool Members' Site"});
  // XXX once we're running HTTPS, we can enable the siteLogo parameter
  //siteLogo : "/static/img/mindpool-logo-tiny.png"});
};


var mindpoolOnReady = function() {
  $("#persona-login-link").click(mindpoolLoginOnClick);
};
