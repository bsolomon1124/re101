=====
re101
=====

A compendium of commonly-used regular expressions.

This module pertains specifically to regexes embedded inside Python and compiled with Python's `re
<https://docs.python.org/3/library/re.html>`_ module.

.. code:: python

    >>> from re101 import nanp_phonenum
    >>> text = """
    ... Ross McFluff: +1 (834) 345.1254 155 Elm Street
    ... Ronald Heathmore: 892-345-3428 436 Finley Avenue
    ... Frank Burger: 541-7625 662 South Dogwood Way
    ... Heather Albrecht: 5483264584 919 Park Place"""
    >>> nanp_phonenum.findall(text)
    ['+1 (834) 345.1254', '892-345-3428', '541-7625', '5483264584']

----------
Disclaimer
----------

xxx

----------------
Source directory
----------------

xxx

