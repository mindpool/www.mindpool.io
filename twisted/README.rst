~~~~~~~~~~~~~~~~
www.mindpool.io
~~~~~~~~~~~~~~~~

This is the application that runs the company internet properties.

Known Issues
============

* When running with ``pypy``, logging in with Persona causes the process to hang.


Setup
=====


Production Deployments
----------------------

#. Install ``memcached`` on your system.

#. Change directory to your production checkout of ``mindpoolsite``.

#. Run ``make install``.

#. Run ``make start-prod``.


Development
-----------

#. Download and install the dependencies for the production environment.

#. Install MongoDB.

#. Run ``make install-dev``

   This step will install Bootstrap (in the local dir) and the LESS compiler
   (using ``npm``).

   If you run into errors::

     sudo ln -sf /usr/local/share/npm/bin/lessc /usr/local/bin/

     export PATH=$PATH:/usr/local/share/npm/bin/ (or .bashrc depending on your setup)

#. Run ``make start-dev``

If you don't want to use the default Python binary, then you can pass ``make``
variables to select the one that you want. For example, on a sysmte that
doesn't have pypy installed, you can do this::

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

#. If your new page can be cached, be sure to add the ``caching=True``
   parameter to the ``@pages.route`` decorator. Cached route methods return a
   class, not an instance (in order to decrease unnecessary overhead), so make
   sure you're not creating an instance in route functions/methods when you
   have caching enabled.

#. Add a new page class to ``mindpoolsite.views.pages``, subclassing the
   appropriate parent class, defining the appropriate HTML content (see the
   others in that module for example usage).

#. Add your content to ``mindpoolsite.content.MODULE``, as appropriate.


.. Links
.. _pypy-1.9: http://pypy.org/download.html


