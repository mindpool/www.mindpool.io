~~~~
TODO
~~~~

Fit and Finish
--------------

* fix page padding on both templates when in smaller modes

* on regular pages, the top nav element that should be highlighted for the
  current page, isn't getting highlighted; probably somethings up with the
  logic for the computed CSS in the view

* on regular pages, the footer needs to have white text

* on regular pages, the "active" links in the sidebar aren't getting
  highlighted (and all links are active)


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
