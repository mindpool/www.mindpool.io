~~~~
TODO
~~~~

Fit and Finish
--------------

* fix page padding on both templates when in smaller modes

* add a custom 404 page

* add a custom 401 page (and other permissions pages)


Content Management
------------------

* finish adding content in RST format

* update the styles of the content pages to display text properly

  * update CSS on content pages: link colors are too light


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

  * when the logout functionality lands, be sure that the session is expired
    upon logout

* chop up the login parts of the top navs to remove duplicate templating

* style the login in the top navs

  * can we adjust the "logged in as ...@..." text to something shorter? Just
    the username?

    * looks like the only returned is the string itself, so this will have to
      be parsed and adjusted in JS

  * fix the text rendering/styling; maybe bold the login text?

  * add a login link next to thte logged in name: "Your Name | logout "

* add error pages

  * what happens with a bad authentication?

  * what happens with a good auth, but a user who is not in the system?
