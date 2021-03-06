# re101

A compendium of commonly-used regular expressions.

This package pertains specifically to regular expressions embedded inside Python and compiled with Python's [`re`](https://docs.python.org/3/library/re.html) module.

----

## Introduction

All importable objects are compiled regular expressions.  For instance, `US_PHONENUM` matches sequences following the North American Number Plan (NANP) format.  In plain English, this is what would qualify as a "North American telephone number":

```python
>>> from re101 import US_PHONENUM
>>> text = """
... Ross McFluff: +1 (834) 345.1254 155 Elm Street
... Ronald Heathmore: 892-345-3428 436 Finley Avenue
... Frank Burger: 541-7625 662 South Dogwood Way
... Heather Albrecht: 5483264584 919 Park Place"""

>>> US_PHONENUM.findall(text)
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
- personally identifiable information

## Naming Conventions

Objects exported by the package may be in either `UPPERCASE`, `CamelCase`, or `lower_case`:

- `UPPERCASE`: These are compiled regular expressions, of type `re.Pattern`, which is the result of `re.compile()`.
- `CamelCase`: These are classes whose `__new__()` method returns a compiled regular expression, but takes a few additional parameters that add optionality to the compiled result.  For instance, the `Number` class lets you allow or disallow leading zeros and commas.
- `lower_case`: These are traditional functions built around the package's regex constants.  They do not share any consistency in their call syntax or result type.

## Disclaimer

Use these regular expressions with care.  It is unlikely that any of them cover 100.00% of the cases that they are intended to cover.  They are built to handle "99.x%" of cases.  With all regular expressions, a balance must be made: covering an incremental 0.1% of cases often requires a large marginal amount of work and code.

If you do notice egregious mistakes or omissions, please consider submitting an issue or pull request.  See the "Contributing" file.

Please assume these expressions are "US-centric" unless noted otherwise.  For instance, the `zipcodes` expression looks only for XXXXX or XXXXX-XXXX zip codes.

## Sources

Citations are included for "unique" regexes that are copied from a singular source.  More "generic" regexes that can be found in similar form from multiple public sources may not be cited here.

1. Goyvaerts, Jan & Steven Levithan.  Regular Expressions Cookbook, 2nd ed.  Sebastopol: O'Reilly, 2012.
2. Friedl, Jeffrey.  Mastering Regular Expressions, 3rd ed.  Sebastopol: O'Reilly, 2009.
3. Goyvaerts, Jan.  Regular Expressions: The Complete Tutorial.  https://www.regular-expressions.info/.
4. Python.org documentation: `re` module.  https://docs.python.org/3/library/re.html
5. Kuchling, A.M.  "Regular Expression HOWTO."  https://docs.python.org/3/howto/regex.html
6. Python.org documentation: `ipaddress` module.  Copyright 2007 Google Inc.  Licensed to PSF under a Contributor Agreement.  https://docs.python.org/3/library/ipaddress.html
7. nerdsrescueme/regex.txt.  https://gist.github.com/nerdsrescueme/1237767

## To-Do List

These patterns are not currently implemented:

- IPv6 address (RFC 4291)
- Dates and times (both ISO-8601 and more informal, such as those that can be parsed by Python's `dateutil`)
- Money/currency (including both the leading or trailing sign, numbers, and punctuation)
