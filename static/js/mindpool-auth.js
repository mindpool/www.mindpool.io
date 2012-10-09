var updateLoginDOM = function(results) {
    // XXX we need to build a link to the acount page (/members/account) as
    // well as a link to the log out page (/logout)
    //
    // If this doesn't match what is produced by the Python code at
    // mindpoolsite.views.basefragments.AuthFragment.getAuthedLink, then
    // there's something wrong.
    $("#persona-login").text(results.displayName + " | Sign out ");
};


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
    console.log(data);
    //updateLoginDOM(data.results);
    $("#persona-login").text("loading ...");
    window.location.reload();
  });
  request.fail(function(jqXHR, status) {
    //console.log(jqXHR);
    console.log(status);
  });
};


var mindpoolLogout = function() {
  console.log("onlogout");
  var request = $.ajax({
    url: "/logout",
    type: "POST"});
  request.done(function(data) {
    $("#persona-login").text("loading ...");
    window.location.reload();
  });
  request.fail(function(jqXHR, status) {
    //console.log(jqXHR);
    console.log(status);
  });
};


var mindpoolLoginOnClick = function() {
  //$("#persona-login").text("logging in...");
  return navigator.id.request({
    siteName: "MindPool Members' Site"});
    // XXX once we're running HTTPS, we can enable the siteLogo parameter
    //siteLogo : "/static/img/mindpool-logo-tiny.png"});
};


var mindpoolLogoutOnClick = function() {
  navigator.id.logout();
  // XXX hrm, for whatever reason, the logout function doesn't seem to be
  // getting called by navigator.id.watch ... so, we'll do it manually here
  mindpoolLogout();
};


var mindpoolOnReady = function() {
  $("#persona-login-link").click(mindpoolLoginOnClick);
  $("#persona-logout-link").click(mindpoolLogoutOnClick);
};
