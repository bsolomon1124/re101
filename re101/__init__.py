# flake8: ignore=E501

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

With regex comes responsibility:

Categories of expressions that don't belong here include credit card
    patterns, passwords, and social security numbers, given that the
    only real purpose of having these is for malicious information
    retrieval.  You get the gist.

Please assume these expressions are "US-centric" unless noted otherwise.

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

# TODO: include https://regexr.com/ links
# TODO: https://gist.github.com/nerdsrescueme/1237767
# TODO: re.X annotations (careful with re.X, whitespace, and (?=
#       https://bugs.python.org/issue15606)


__author__ = 'Brad Solomon <brad.solomon.1124@gmail.com>'
__all__ = ['email', 'nanp_phonenum', 'mult_whitespace', 'mult_spaces', 'word', 'adverb', 'not_followed_by', 'followed_by', 'ipv4', 'url', 'moneysign', 'Number', 'Integer', 'Decimal', 'zipcode', 'states']  # TODO
__license__ = 'MIT'


import re


# ---------------------------------------------------------------------
# *Email address*.  Source: [3]

email = re.compile(r"^\"*[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&@'*+/=?^_`{|}~-]+)*\"*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", flags=re.I)


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
nanp_phonenum = re.compile(r'(?<!-)(?:\b|\+|)(?:1(?: |-|\.|\()?)?(?:\(?[2-9]\d{2}(?: |-|\.|\) |\))?)?[2-9]\d{2}(?: |-|\.)?\d{4}\b')


# ---------------------------------------------------------------------
# *Dates & times*

# TODO


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

# TODO - ipv6


# ---------------------------------------------------------------------
# (Valid) URL

# Valid Uniform Resource Locator (URL) as prescribed by
# RFC 1738; format is <scheme>:<scheme-specific-part>.
# This means that 'google.com' is not in itself a valid URL.
# See http://www.ietf.org/rfc/rfc1738.txt
url = re.compile(r'\b(https?|ftp|file)://.+\/?\b')

# TODO: "loose" URL (non-strict syntax)


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

# TODO: currency; deal with front/back-end symbol

# For the lexical structure for a "number," we steal from the Postgres
# docs, with a few additions:
#
#     Numeric constants are accepted in these general forms:
#
#     digits
#     digits.[digits][e[+-]digits]
#     [digits].digits[e[+-]digits]
#     digitse[+-]digits
#
#     where digits is one or more decimal digits (0 through 9).
#     At least one digit must be before or after the decimal point,
#     if one is used. At least one digit must follow the exponent marker
#     (e), if one is present.  Brackets indicate optionality.
#
# To this, we add the optionality to use commas and allow or disallow
# leading zeros.
#
# Four different variations of a "number" regex based on whether
# we want to allow leading zeros and/or commas.
# Thanks @WiktorStribiżew for the lookahead:
# https://stackoverflow.com/a/50223631/7954504

number_combinations = {
    (True, True):  # Leading zeros permitted; commas permitted.
        (
            r'(?:(?<= )|(?<=^))(?<!\.)\d+(?:,\d{3})*(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\.)\d+(?:,\d{3})*\.\d+(?:[eE][+-]?\d+)?(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        ),
    (True, False):  # Leading zeros permitted; commas not permitted.
        (
            r'(?:(?<= )|(?<=^))(?<!\.)\d+(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\.)\d+\.\d+(?:[eE][+-]?\d+)?(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        ),
    (False, True):  # Leading zeros not permitted; commas permitted.
        (
            r'(?:(?<= )|(?<=^))(?<!\.)[1-9]+\d*(?:,\d{3})*(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\.)[1-9]+\d*(?:,\d{3})*\.\d+(?:[eE][+-]?\d+)?(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        ),
    (False, False):  # Neither permitted.
        (
            r'(?:(?<= )|(?<=^))(?<!\.)[1-9]+\d*(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\.)[1-9]+\d*\.\d+(?:[eE][+-]?\d+)?(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        )
    }


class Number(object):
    """A regex to match a wide syntax for 'standalone' numbers.

    "Number" is an inclusive term covering:
    - "Integers": 12, 1,234, 094,509.
    - "Decimals": 12.0, .5, 4., 12,000.00
    - Scientific notation: 12.0e-03, 1E-5

    The class instance is a compiled regex.

    Parameters
    ----------
    allow_leading_zeros: bool, default True
        Permit leading zeros on numbers.  (I.e. 042, 095,000, 09.05)
    allow_commas: bool, default True
        If True, allow *syntactically correct* commas.  (I.e. 1,234.09)
    flags: {int, enum.IntFlag}, default 0
        Passed to `re.compile()`.

    Returns
    -------
    _sre.SRE_Pattern, the object produced by `re.compile()`
    """

    def __new__(cls, allow_leading_zeros=True, allow_commas=True, flags=0):
        key = allow_leading_zeros, allow_commas
        pattern = '|'.join(number_combinations[key])
        return re.compile(pattern, flags=flags)


class Integer(object):
    def __new__(cls, allow_leading_zeros=True, allow_commas=True, flags=0):
        key = allow_leading_zeros, allow_commas
        # The only difference here is we use 0th element only.
        pattern = number_combinations[key][0]
        return re.compile(pattern, flags=flags)


class Decimal(object):
    def __new__(cls, allow_leading_zeros=True, allow_commas=True, flags=0):
        key = allow_leading_zeros, allow_commas
        # 0th element is for Integer; other are for Decimal.
        pattern = '|'.join(number_combinations[key][1:])
        return re.compile(pattern, flags=flags)


# ---------------------------------------------------------------------
# *Geographic info*

# Five digits with optional 4-digit extension
# https://en.wikipedia.org/wiki/ZIP_Code#ZIP+4
zipcode = re.compile(r'\b[0-9]{5}(?:-[0-9]{4})?\b(?!-)')

# Source: [7]
states = re.compile(r'\b(A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])\b')
