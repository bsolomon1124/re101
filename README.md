# `re101`

A compendium of commonly-used regular expressions.

This module pertains specifically to regexes embedded inside Python and compiled with Python's [`re`](https://docs.python.org/3/library/re.html).

----

## Introduction

All importable objects are compiled regular expressions.  For instance, `nanp_phonenum` matches sequences following the North American Number Plan (NANP) format.  In plain English, this is what would qualify as a "North American telephone number":

```python
>>> from re101 import nanp_phonenum
>>> text = """
... Ross McFluff: +1 (834) 345.1254 155 Elm Street
... Ronald Heathmore: 892-345-3428 436 Finley Avenue
... Frank Burger: 541-7625 662 South Dogwood Way
... Heather Albrecht: 5483264584 919 Park Place"""

>>> nanp_phonenum.findall(text)
['+1 (834) 345.1254', '892-345-3428', '541-7625', '5483264584']
```

Currently, the package supports regexes related to:

- email addresses
- whitespace
- words/tokens
- phone numbers
- IP addresses
- URLs
- integers, decimals, numbers
- geographic information

## Disclaimer

Use these regular expressions with care.  It is unlikely that any of them cover 100.00% of the cases that they are intended to cover.  They are built to handle "99.x%" of cases.  With all regular expressions, a balance must be made: covering an incremental 0.1% of cases often requires a large marginal amount of work and code.

If you do notice egregious mistakes or omissions, please consider submitting an issue or pull request.  See the "Contributing" file.

Please assume these expressions are "US-centric" unless noted otherwise.  For instance, the `zipcodes` expression looks only for XXXXX or XXXXX-XXXX zip codes.

## Sources

Citations are included for "unique" regexes that are copied from a singular source.  More "generic" regexes that can be found in similar form from multiple public sources may not be cited here.

- 1. Goyvaerts, Jan & Steven Levithan.  Regular Expressions Cookbook, 2nd ed.  Sebastopol: O'Reilly, 2012.
- 2. Friedl, Jeffrey.  Mastering Regular Expressions, 3rd ed.  Sebastopol: O'Reilly, 2009.
- 3. Goyvaerts, Jan.  Regular Expressions: The Complete Tutorial.  https://www.regular-expressions.info/.
- 4. Python.org documentation: `re` module.  https://docs.python.org/3/library/re.html
- 5. Kuchling, A.M.  "Regular Expression HOWTO."  https://docs.python.org/3/howto/regex.html
- 6. Python.org documentation: `ipaddress` module.  Copyright 2007 Google Inc.  Licensed to PSF under a Contributor Agreement.  https://docs.python.org/3/library/ipaddress.html
- 7. nerdsrescueme/regex.txt.  https://gist.github.com/nerdsrescueme/1237767
