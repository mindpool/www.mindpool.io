~~~~~~~~~~~~~~~
www.mindpool.io
~~~~~~~~~~~~~~~

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

#. Run ``make start-dev``


.. Links
.. _pypy-1.9: http://pypy.org/download.html


