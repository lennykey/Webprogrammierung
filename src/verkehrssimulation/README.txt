=======================================
Chapter 4: Modules, Packages, Libraries
=======================================


Modules
=======

A module is a Python source file (*.py) or a compiled Python file
(e.g. *.pyc) containing a sequence of statements that are executed
during the first import.

Usually a module contains function and class definitions, but it
may also define variables that are then "module global".


Packages
========

Packages are just directories containing an __init__.py file (or
a compiled Python file). Upon first import of a package this __init__
pseudo module is executed; the symbols defined in it appear in the
packages name space.

Often the __init__ module is just empty; the real code is in most
cases in other modules residing in the package directory.

Packages may not only contain modules but also other packages, thus
building up an arbitrarily complex package hierarchy.


A Simulation Library
====================

A library may consist of one or more modules or one or more packages
with the packages and modules it it.

In this chapter we try to set up a small simulation library using
the language elements we already know.

As in the previous chapters "cybertrain" is the top-level package,
"ch04" is the package collecting all elements of this chapter's
library.

  >>> import world
  >>> import car

  >>> world.addCar('red')
  >>> world.step((5,))
  >>> world.report()
  0 / red : 0... 5...
  >>> world.step((5,))
  >>> world.report()
  0 / red : 1.38... 10.0

  >>> world.step((8,))
  >>> world.report()
  0 / red : 4.16... 18.0

  >>> world.step((8,))
  >>> world.report()
  0 / red : 9.16... 22.44...

Now let's slam on the brakes.

  >>> world.step((-10,))
  >>> world.report()
  0 / red : 15.40... 4.62...

  >>> world.step((-10,))
  >>> world.report()
  0 / red : 16.68... 0.0


