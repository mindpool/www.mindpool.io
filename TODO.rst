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

  * headings on content pages are squished with little or no spaces

  * there needs to be more vertical space between the heading and the first
    paragraph


Authentication / Authorization
------------------------------

* a system needs to be put in place for protecting specific resources

  * once that's done, we'll be able to allow resouces by Account

* roles need to be defined, associated with accounts, etc.

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

* style the login in the top navs

  * fix the text rendering/styling; maybe bold the login text?
