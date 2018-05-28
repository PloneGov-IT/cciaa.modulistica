.. contents::

Introduction
============

The italian word `modulistica`__ means "*documentation*", "*downloadable forms*". 

__ http://www.wordreference.com/iten/modulistica

This product adds the following features to your Plone folders:

* a new view ("*Downloadable forms view*") to display files in the folder
* a new field, where you can enter a set of column names, used in the view

This product has been designed for public administration offices, but can be used from any other company that
needs to display a large amount of files that can be downloaded from visitors. 

How to use the view
===================

This view will simply show in a table all files and links in the folder, ignoring all other
stuff.

Files are displayed in a two-column table.

.. image:: http://keul.it/images/plone/cciaa.modulistica-2.0.0-01.png
   :alt: Simple view, without related items

You can optionally use a new field of the folder called *Columns titles* to control the heading of the table.
If you don't provide a value for this field, no heading will be used. Please note that the field is only
displayed when the view is applied to the folder

Related items of files
----------------------

If files have related items, they are used to expand the table with more columns. This features is
mainly used for giving secondary, alternative format for a downloadale document.

.. image:: http://keul.it/images/plone/cciaa.modulistica-2.0.0-02.png
   :alt: Main files with secondary ones

Keep in mind that:

* related items of Link content type are ignored
* only related items of type File or Link are used

Pages
-----

In facts the view also use Pages inside the folder, but for a special use case.

Pages are loaded, and the body content is inserted inside a wide table header row. This can be useful if you
need to comment a subset of files.

.. image:: http://keul.it/images/plone/cciaa.modulistica-2.0.0-03.png
   :alt: Table with comments

You can use this feature for simple comment inside the table, or for provide a complex structure:

.. image:: http://keul.it/images/plone/cciaa.modulistica-2.0.0-04.png
   :alt: Table with (more) comments

You can find a lot of additional examples in the `Modulistica section`__ of the Chamber of Commerce of Ferrara.

__ http://www.fe.camcom.it/cciaa/modulistica-cciaa

Dependency
==========

Tested on Plone 4.3 and Plone 5

Credits
=======

Developed with the support of `Camera di Commercio di Ferrara`__;
Camera di Commercio di Ferrara supports the `PloneGov initiative`__.

.. image:: http://www.fe.camcom.it/cciaa-logo.png/
   :alt: CCIAA Ferrara - logo

__ http://www.fe.camcom.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/

