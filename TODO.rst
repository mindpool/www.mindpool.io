~~~~
TODO
~~~~

Fit and Finish
--------------

* fix page padding on both templates when in smaller modes


Chopshop
--------

* views.pages.ContentPage needs a data method that calls tag.fillSlots

  * that data method needs to passed sidebar, content, and footer params

  * the sidebar param needs to call a getSidebar method that builds stacked
    pills for content that has multiple parts (e.g., services, people, about)

  * the content param needs to call a getContent method that:

    * checks the current url to determine which content.*.* variable name to
      use, and then return the value of that variable

  * the footer param needs to instantiate the footer Element and return it

* we probably need to have side-bar pages and non-side-bar pages
