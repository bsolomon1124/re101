"""Commonly-used regular expressions.

DISCLAIMER
===============
Use these regular expressions with care.  It is unlikely that any of
    them cover 100.00% of the cases that they are intended to cover.
    They are built to handle 99.x% of cases.  With all regular expressions,
    a balance must be made: covering an incremental 0.1% of cases often
    requires a large marginal amount of work and code.

If you do notice egregious mistakes or omissions, please consider
    submitting an issue or pull request.  See the "Contributing" file.

Categories of expressions that don't belong here include credit card
    patterns, passwords, and social security numbers, given that the
    only real purpose of having these is for malicious information
    retrieval.  You get the gist.

Source directory
===============
[1]     Goyvaerts, Jan & Steven Levithan.  Regular Expressions Cookbook,
        2nd ed.  Sebastopol: O'Reilly, 2012.
[2]     Friedl, Jeffrey.  Mastering Regular Expressions, 3rd ed.
        Sebastopol: O'Reilly, 2009.
[3]     Goyvaerts, Jan.  Regular Expressions: The Complete Tutorial.
        https://www.regular-expressions.info/.
[4]     Python.org documentation: `re` module.
        https://docs.python.org/3/library/re.html
[5]     Kuchling, A.M.  "Regular Expression HOWTO."
        https://docs.python.org/3/howto/regex.html
[6]     Python.org documentation: `ipaddress` module.
        Copyright 2007 Google Inc.
        Licensed to PSF under a Contributor Agreement.
        https://docs.python.org/3/library/ipaddress.html
[7]     nerdsrescueme/regex.txt.
        https://gist.github.com/nerdsrescueme/1237767

Citations are included for "unique" regexes that are copied from a
    singular source.  More "generic" regexes that can be found in
    similar form from multiple public sources may not be cited here.

Notes
===============
It is recommended to import the module rather than its specific contents
    directly.  A handful of object names here may conflict with common
    modules or objects from Python's Standard Library
    For example, use `import re101` --> `re101.email`.
"""

# TODO: re.X annotations
# TODO: include https://regexr.com/ links


__author__ = 'Brad Solomon <brad.solomon.1124@gmail.com>'
__all__ = []  # TODO
__license__ = 'MIT'


import re

# https://gist.github.com/nerdsrescueme/1237767
#
#
# https://stackoverflow.com/questions/1449817/what-are-some-of-the-most-useful-regular-expressions-for-programmers


# ---------------------------------------------------------------------
# *Email address*.  Source: [3]

email = re.compile(r"^\"*[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&@'*+/=?^_`{|}~-]+)*\"*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", flags=re.I)


# ---------------------------------------------------------------------
# *Valid HTML tag + contents*.

# TODO: sure we want to implement this>?
# https://stackoverflow.com/a/1732454/7954504

any_tag = re.compile(r'<tag\b[^>]*>(.*?)</tag>')


def tag(tagname):
    return re.compile(r'<{tag}\b[^>]*>(.*?)</{tag}>'.format(tag))


# ---------------------------------------------------------------------
# *Whitespace*


# 2+ consecutive of any whitespace
# \s --> ` \t\n\r\f\v`
mult_whitespace = re.compile(r'\s\s+')

# 2+ consecutive literal spaces, excluding other whitespace
mult_spaces = re.compile(r'  +')


# ---------------------------------------------------------------------
# *Words*

# A generic word tokenizer, defined as one or more alphanumeric characters
# bordered by word boundaries
word = re.compile(r'\b\w+\b')

# Source: [4]
adverb = re.compile(r'\w+ly')


def not_followed_by(word):
    return re.compile(r'\b\w+\b(?!\W+{word}\b)'.format(word=word))


def followed_by(word):
    return re.compile(r'\b\w+\b(?=\W+{word}\b)'.format(word=word))


# ---------------------------------------------------------------------
# *Phone numbers*

# Restricted to follow the North American Numbering Plan (NANP),
#     a telephone numbering plan that encompasses 25 distinct
#     regions in twenty countries primarily in North America,
#     including the Caribbean and the U.S. territories.
# https://en.wikipedia.org/wiki/North_American_Numbering_Plan#Modern_plan
nanp_phonenum = re.compile(r'(?<!-)(\b|\+|)(?:1( |-|\.|\()?)?(?:\(?[2-9]\d{2}( |-|\.|\) |\))?)?[2-9]\d{2}( |-|\.)?\d{4}\b')


# ---------------------------------------------------------------------
# *Dates & times*

date = None  # TODO


# ---------------------------------------------------------------------
# *IP addresses*

# Unlike Python's ipaddress module, we are only concerned with
#     string representations of IP addresses, not their integer or
#     bytes representations.
#     Definitions: https://docs.python.org/3/library/ipaddress.html

# Valid IPv4 address:  (Source: [6])
# A string in decimal-dot notation, consisting of four decimal integers
# in the inclusive range 0–255, separated by dots (e.g. 192.168.0.1).
# Each integer represents an octet (byte) in the address. Leading zeroes
# are tolerated only for values less than 8 (as there is no ambiguity
# between the decimal and octal interpretations of such strings).
ipv4 = re.compile(r'\b(([0]{1,2}[0-7]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0]{1,2}[0-7]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b')

# Valid IPv6 address:  (Source: [6])
# A string consisting of eight groups of four hexadecimal digits,
# each group representing 16 bits. The groups are separated by colons.
# This describes an exploded (longhand) notation. The string can also be
# compressed (shorthand notation) by various means. See RFC 4291 for details.
# For example, "0000:0000:0000:0000:0000:0abc:0007:0def" can be compressed
# to "::abc:7:def".
# See also: https://tools.ietf.org/html/rfc4291.html
ipv6 = None  # TODO
ip = ipv4  # TODO


# ---------------------------------------------------------------------
# (Valid) URL

# Valid Uniform Resource Locator (URL) as prescribed by
# RFC 1738; format is <scheme>:<scheme-specific-part>.
# This means that 'google.com' is not in itself a valid URL.
# See http://www.ietf.org/rfc/rfc1738.txt
url = re.compile('\b(https?|ftp|file)://.+\/?\b')


# ---------------------------------------------------------------------
# *Numbers and currency*

# All currency symbols in the {Sc} category (Symbol, currency)
# Source: http://www.fileformat.info/info/unicode/category/Sc/list.htm
moneysign = (u'\u0024\u00A2\u00A3\u00A4\u00A5\u058F\u060B\u09F2\u09F3'
             u'\u09FB\u0AF1\u0BF9\u0E3F\u17DB\u20A0\u20A1\u20A2\u20A3'
             u'\u20A4\u20A5\u20A6\u20A7\u20A8\u20A9\u20AA\u20AB\u20AC\u20AD'
             u'\u20AE\u20AF\u20B0\u20B1\u20B2\u20B3\u20B4\u20B5\u20B6\u20B7'
             u'\u20B8\u20B9\u20BA\u20BB\u20BC\u20BD\u20BE\u20BF\uA838\uFDFC'
             u'\uFE69\uFF04\uFFE0\uFFE1\uFFE5\uFFE6')

integer = r'[+-]*\b[0-9]{1,3}(,[0-9]{3})*'
decimal = r'[+-]*(\b[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\b|\b[0-9]{1,3}(,[0-9]{3})*\.[0-9]*(?!\d)|(?<!\d)\.\d+\b)'
number = re.compile(r'(' + r'|'.join((integer, decimal)) + r')')
integer = re.compile(integer)
decimal = re.compile(decimal)

currency = None  # TODO: deal with front/back-end symbol


# ---------------------------------------------------------------------
# *Geographic info*

zipcode = re.compile(r'\b[0-9]{5}(?:-[0-9]{4})?\b(?!-)')

# Source: [7]
states = re.compile(r'\b(A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])\b')
