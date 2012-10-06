~~~~
TODO
~~~~

Fit and Finish
--------------

* fix page padding on both templates when in smaller modes

* fix logo situation

  * remove "Home" link on regular pages

  * move small logo to where the "Home" link used to be

  * link the small logo to the splash page

* add a custom 404 page

* add a custom 401 page (and other permissions pages)


Content Management
------------------

* start adding content in RST format

* add support for rendering RST to HTML

* update the styles of the content pages to display text properly


Authentication
--------------

* the login form should only display when a user is not logged in

* a system needs to be put in place for protecting specific resources

  * once that's done, we'll be able to allow resouces by Account

* roles need to be defined, associated with accounts, etc.

* an admin interface needs to be added for managing users

* account data needs to be stored

  * account objects will also have roles, so role data will need to be stored
    as well

* a "persona audience" parameter needs to be added to mindpoolsite.app, so that
  dev and production can run easily from the same code

* add logout logic in JS and Python

* add session support so that logins are remembered

* chop up the login parts of the top navs to remove duplicate templating

* style the login in the top navs

  * maybe move the logo over to the far left?

  * can we adjust the "logged in as ...@..." text to something shorter? Just
    the username?

    * looks like the only returned is the string itself, so this will have to
      be parsed and adjusted in JS

  * fix the text rendering/styling

* add error pages

  * what happens with a bad authentication?

  * what happens with a good auth, but a user who is not in the system?

REST
----

* 
