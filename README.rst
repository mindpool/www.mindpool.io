~~~~~~~~~~~~~~~~
www.mindpool.io
~~~~~~~~~~~~~~~~

This is the application that runs the company internet properties.

Setup
=====

Production Deployments
----------------------

#. Install ``memcached`` on your system
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

   export PATH=$PATH:/usr/local/share/npm/bin/ (or .bashrc depending on your setup)

#. Run ``make start-dev``

If you don't want to use the default of ``pypy`` as your Python binary, then
you can pass ``make`` variables to select the one that you want. For example,
on a sysmte that doesn't have pypy installed, you can do this::

  $ PYTHON=`which python` TWISTD=`which twistd` make start-dev

Using the Twisted Plugin
------------------------

The ``Makefile`` is provided for convenience, but one also has the option of
overriding various defaults for the site pluging when using it directly. For
instance:

* **enable caching** - ``twistd -n mindpool-site --cache``

* **enable debugging** - ``twistd -n mindpool-site --debug``

* **change the port** - ``twistd -n mindpool-site --webport 10080``

As one might expect, you can do them all at the same time ;-)

::

  $ twistd -n mindpool-site --cache --debug --webport 10080

You can also start in daemonized mode: ``twistd mindpool-site``. To stop the
daemon, simply do: ``twistd mindpool-site stop``. Note that in damonized mode
you can still use all of the plugin options, just as above.

Managing Content
================

Adding URLs, Pages, and Content
-------------------------------

#. Edit ``mindpoolsite.urls.map``.

#. Add the new URL to whatever menus are appropriate in the same ``urls``
   module.

#. Make the new URL routable by updating ``mindpoolsite.routes`` with a new
   function (or static method, if you're putting it into an organizing class)
   that instantiates a page class appropriate for your URL.

#. If your new page can be cached, add the ``@pages.cache`` decorator. Cached
   route methods return a class, not an instance, in order to decrease
   unnecessary overhead. Also, note that the caching decorator has to be right
   above the function definition (if ``@pages.route`` is directly above the
   function, ``@pages.cache`` will get swallowed by it and no caching will
   happen).

#. Add a new page class to ``mindpoolsite.views.pages``, subclassing the
   appropriate parent class, defining the appropriate HTML content (see the
   others in that module for example usage).

#. Add your content to ``mindpoolsite.content.MODULE``, as appropriate.


.. Links
.. _pypy-1.9: http://pypy.org/download.html


