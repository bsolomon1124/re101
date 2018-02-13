=====
re101
=====

A compendium of commonly-used regular expressions.

This module pertains specifically to regexes embedded inside Python and compiled with Python's `re
<https://docs.python.org/3/library/re.html>`_ module.

.. code:: python

    >>> # Capture sequences following the
    ... # North American Numbering Plan (NANP) phone number format
    ... from re101 import nanp_phonenum

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

Use these regular expressions with care.  It is unlikely that any of them cover 100.00% of the cases that they are intended to cover.  They are built to handle "99.x%" of cases.  With all regular expressions, a balance must be made: covering an incremental 0.1% of cases often requires a large marginal amount of work and code.

If you do notice egregious mistakes or omissions, please consider submitting an issue or pull request.  See the "Contributing" file.

Categories of expressions that don't belong here include credit card patterns, passwords, and social security numbers, given that the only real purpose of having these is for malicious information retrieval.  You get the gist.

----------------
Source directory
----------------

[1]     Goyvaerts, Jan & Steven Levithan.  Regular Expressions Cookbook, 2nd ed.  Sebastopol: O'Reilly, 2012.
[2]     Friedl, Jeffrey.  Mastering Regular Expressions, 3rd ed.  Sebastopol: O'Reilly, 2009.
[3]     Goyvaerts, Jan.  Regular Expressions: The Complete Tutorial.  https://www.regular-expressions.info/.
[4]     Python.org documentation: `re` module.  https://docs.python.org/3/library/re.html
[5]     Kuchling, A.M.  "Regular Expression HOWTO."  https://docs.python.org/3/howto/regex.html
[6]     Python.org documentation: `ipaddress` module.  Copyright 2007 Google Inc.  Licensed to PSF under a Contributor Agreement.  https://docs.python.org/3/library/ipaddress.html
[7]     nerdsrescueme/regex.txt.  https://gist.github.com/nerdsrescueme/1237767

Citations are included for "unique" regexes that are copied from a singular source.  More "generic" regexes that can be found in similar form from multiple public sources may not be cited here.

-----
Notes
-----
It is recommended to import the module rather than its specific contents directly.  A handful of object names here may conflict with common modules or objects from Python's Standard Library.

For example, use :code:`import re101` with :code:`re101.email` rather than :code:`from re101 import email`, which could potentially conflict with Python's `email.py` module.
