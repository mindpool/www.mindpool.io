~~~~~~~~~~~~~~~~
www.mindpool.io
~~~~~~~~~~~~~~~~

This is the application that runs the company internet properties.

Setup
=====

Production Deployments
----------------------

#. Download `pypy-1.9`_.

#. Unzip it and move it to ``/usr/local``.

#. Run ``make install``.

#. Run ``make start-prod``.

Development
-----------

#. Download and install pypy as above.

#. Install MongoDB.


#. Run ``make install-dev``

   This step will install Bootstrap (in the local dir) and the LESS compiler
   (using ``npm``).

   If you run into errors:

   sudo ln -sf /usr/local/share/npm/bin/lessc /usr/local/bin/

   export export PATH=$PATH:/usr/local/share/npm/bin/ (or .bashrc depending on your setup)

#. Run ``make start-dev``

If you don't want to use the default of ``pypy`` as your Python binary, then
you can pass make variables to select the one that you want. For example, on a
sysmte that doesn't have pypy installed, you can do this::

  $ PYTHON=`which python` TWISTD=`which twistd` make start-dev

Managing Content
================

Adding URLs, Pages, and Content
-------------------------------

#. Edit ``mindpoolsite.const.urls``.

#. Add the new URL to whatever menus are appropriate in the same ``const``
   module.

#. Make the new URL routable by updating ``mindpoolsite.routes`` with a new
   function that instantiates a page class appropriate for your URL.

#. Add a new page class to ``mindpoolsite.views.pages``, subclassing the
   appropriate parent class, defining the appropriate HTML content (see the
   others in that module for example usage).

#. Add your content to ``mindpoolsite.content.MODULE``, as appropriate.


.. Links
.. _pypy-1.9: http://pypy.org/download.html


