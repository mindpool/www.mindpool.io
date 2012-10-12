~~~~
TODO
~~~~

Fit and Finish
--------------

* fix page padding on both templates when in smaller modes

  * also, in smaller modes the hover background color for the drop-down menu
    items is wrong (bright blue)

  * the footer in smaller modes doesn't display well...

* add a custom 404 page

* add a custom 401 page (and other permissions pages)

* add a caruosel to the front page that highlights some of our expertise
  (starting with the main logo)

  http://twitter.github.com/bootstrap/javascript.html#carousel

* add session timeout command line option


Deployments
-----------

* create a staging vhost

* test pypy andn auth on the staging server


Content Management
------------------

* finish adding content in RST format


Authentication / Authorization
------------------------------

* when a default email is added, it needs to be added to the list of emails

* a system needs to be put in place for protecting specific resources

  * once that's done, we'll be able to allow resouces by Account

* roles need to be defined, associated with accounts, etc.

  * allowed roles can be passed as a list of interfaces to route decorators

* an admin interface needs to be added for managing users

* account data needs to be stored

  * account objects will also have roles, so role data will need to be stored
    as well

  * session object storage is one place, but we're going to need persistent
    user account data

  * what will the releationship be between session data and persisted account
    data?

* a "persona audience" parameter needs to be added to mindpoolsite.app, so that
  dev and production can run easily from the same code


Members' Area
-------------

* need to add links for areas of the site that logged in users have been
  granted access to


Data
----

* abstract the data-getting process

  * right now it's getting from modules

  * use a function that returns maybeDeferred so that we can plug any data
    source into that later


Optimization
------------

* add an admin URL that we can hit to purge the memcache page

  * then add a command line option for doing it
