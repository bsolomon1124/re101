"""A compendium of commonly-used regular expressions.

Conventions:
- Compiled regular expressions (of type re.Pattern) are in UPPERCASE.
- Utility functions are in lower_case.
- Classes with __new__() constructors, which take a few configuration options
and produce an re.Pattern type, are in CamelCase.

Sources
=======
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
"""

__author__ = 'Brad Solomon <brad.solomon.1124@gmail.com>'
__license__ = 'MIT'

import functools
import re
import warnings

# ---------------------------------------------------------------------
# *Email address*.  Source: [3]

EMAIL = re.compile(r"^\"*[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&@'*+/=?^_`{|}~-]+)*\"*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", flags=re.I)

# ---------------------------------------------------------------------
# *Whitespace*

# 2+ consecutive of any whitespace
# \s --> ` \t\n\r\f\v`
MULT_WHITESPACE = re.compile(r'\s\s+')

# 2+ consecutive literal spaces, excluding other whitespace.
# Space is Unicode code-point 32.
MULT_SPACES = re.compile(r'  +')

# ---------------------------------------------------------------------
# *Grammar*

# A generic word tokenizer, defined as one or more alphanumeric characters
# bordered by word boundaries
WORD = re.compile(r'\b\w+\b')

# Source: [4]
ADVERB = re.compile(r'\w+ly')


def not_followed_by(word: str) -> re.Pattern:
    return re.compile(r'\b\w+\b(?!\W+{word}\b)'.format(word=word))


def followed_by(word: str) -> re.Pattern:
    return re.compile(r'\b\w+\b(?=\W+{word}\b)'.format(word=word))


# ---------------------------------------------------------------------
# *Phone numbers*

# Restricted to follow the North American Numbering Plan (NANP),
#     a telephone numbering plan that encompasses 25 distinct
#     regions in twenty countries primarily in North America,
#     including the Caribbean and the U.S. territories.
# https://en.wikipedia.org/wiki/North_American_Numbering_Plan#Modern_plan
US_PHONENUM = re.compile(r'(?<!-)(?:\b|\+|)(?:1(?: |-|\.|\()?)?(?:\(?[2-9]\d{2}(?: |-|\.|\) |\))?)?[2-9]\d{2}(?: |-|\.)?\d{4}\b')
# NON_US_PHONENUM = re.compile(r'\+(?:[0-9] ?){6,14}[0-9]')  # Source: [1]

_global_phonenum = (
    r'(?:\+ ?)?'                  # Optional leading plus, followed by optional space
    r'(?:1(?: \d{3})?|\d{2,3})'   # Country code
    r'[ -.]?'                     # Optional sep: space, hyphen, or period
    r'\d{2,3}'                    # Area code
    r'[ -.]?'                     # Optional sep: space, hyphen, or period
    r'\d{3,4}(?:[ -.]?\d{4})?'    # Phone number
)

LOOSE_GLOBAL_PHONENUM = re.compile(_global_phonenum)
# ---------------------------------------------------------------------

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
IPV4 = re.compile(r'\b(([0]{1,2}[0-7]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0]{1,2}[0-7]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b')

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

# Valid Uniform Resource Locator (URL) as prescribed by RFC 1738
# http://www.ietf.org/rfc/rfc1738.txt
STRICT_URL = re.compile(r'\b(?:https?|ftp|file)://[-A-Z0-9+&@#/%?=~_|$!:,.;]*[A-Z0-9+&@#/%=~_|$]', re.I)
LOOSE_URL = re.compile(r'\b(?:(?:https?|ftp|file)://|(?:www|ftp)\.)[-A-Z0-9+&@#/%?=~_|$!:,.;]*[A-Z0-9+&@#/%=~_|$]', re.I)

# ---------------------------------------------------------------------
# *Numbers and currency*

# All currency symbols in the {Sc} category (Symbol, currency)
# Source: http://www.fileformat.info/info/unicode/category/Sc/list.htm
MONEYSIGN = (u'\u0024\u00A2\u00A3\u00A4\u00A5\u058F\u060B\u09F2\u09F3'
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
    (True, True): (
        # Leading zeros permitted; commas permitted.
        r'(?:(?<= )|(?<=^))(?<!\.)\d+(?:,\d{3})*(?= |$)',
        r'(?:(?<= )|(?<=^))(?<!\.)\d+(?:,\d{3})*\.\d+(?:[eE][+-]?\d+)?(?= |$)',
        r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        ),
    (True, False): (
        # Leading zeros permitted; commas not permitted.
            r'(?:(?<= )|(?<=^))(?<!\.)\d+(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\.)\d+\.\d+(?:[eE][+-]?\d+)?(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        ),
    (False, True): (
        # Leading zeros not permitted; commas permitted.
            r'(?:(?<= )|(?<=^))(?<!\.)[1-9]+\d*(?:,\d{3})*(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\.)[1-9]+\d*(?:,\d{3})*\.\d+(?:[eE][+-]?\d+)?(?= |$)',
            r'(?:(?<= )|(?<=^))(?<!\d)\.\d+(?:[eE][+-]?\d+)?(?= |$)'
        ),
    (False, False): (
        # Neither permitted.
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
    re.Pattern, the object produced by `re.compile()`
    """

    def __new__(
        cls,
        allow_leading_zeros: bool = True,
        allow_commas: bool = True,
        flags=0
    ) -> re.Pattern:
        key = allow_leading_zeros, allow_commas
        pattern = '|'.join(number_combinations[key])
        return re.compile(pattern, flags=flags)


class Integer(object):
    def __new__(
        cls,
        allow_leading_zeros: bool = True,
        allow_commas: bool = True,
        flags=0
    ) -> re.Pattern:
        key = allow_leading_zeros, allow_commas
        # The only difference here is we use 0th element only.
        pattern = number_combinations[key][0]
        return re.compile(pattern, flags=flags)


class Decimal(object):
    def __new__(
        cls,
        allow_leading_zeros: bool = True,
        allow_commas: bool = True,
        flags=0
    ) -> re.Pattern:
        key = allow_leading_zeros, allow_commas
        # 0th element is for Integer; other are for Decimal.
        pattern = '|'.join(number_combinations[key][1:])
        return re.compile(pattern, flags=flags)


# ---------------------------------------------------------------------
# *Geographic info*

# Five digits with optional 4-digit extension
# https://en.wikipedia.org/wiki/ZIP_Code#ZIP+4
US_ZIPCODE = re.compile(r'\b[0-9]{5}(?:-[0-9]{4})?\b(?!-)')

# Source: [7]
US_STATE = re.compile(r'\b(A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])\b')

# ---------------------------------------------------------------------
# PII
# Please use these tools for benevolent purposes.

_pw = r'p(?:ass)?w(?:ord)?'
_un = r'user(?:name)?'


def make_userinfo_re(start: str, flags=re.I) -> re.Pattern:
    return re.compile(start + r'(?:\s*[:=]\s*|\s+is\s+)(?P<token>\S+)',
                      flags=flags)


PASSWORD = make_userinfo_re(start=_pw)
USERNAME = make_userinfo_re(start=_un)


def _extract(s: str, name: str, *, r: re.Pattern = None) -> list:
    if not r:
        raise ValueError('`r` must not be null')
    return r.findall(s)


def _make_extract_info_func(start: str, name: str, flags=re.I):
    r = make_userinfo_re(start=start, flags=flags)
    return functools.partial(_extract, r=r)


extract_pw = _make_extract_info_func(start=_pw, name='password')
extract_un = _make_extract_info_func(start=_un, name='username')

# Social security numbers: AAA-GG-SSSS
# https://www.ssa.gov/history/ssn/geocard.html
STRICT_SSN = re.compile(r'\d{3}-\d{2}-\d{4}')
LOOSE_SSN = re.compile(r'\d{3}[ -]?\d{2}[ -]?\d{4}')

# Credit cards
_mastercard_start = r'\b(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)'
_cards = dict(
    _new_visa=r'\b4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}',  # 4XXX-XXXX-XXXX-XXXX
    _old_visa=r'\b4\d{3}[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}',  # 4XXX-XXX-XXX-XXX
    _mastercard=_mastercard_start + r'[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}',  # 5[1-5]XX-XXXX-XXXX-XXXX or [2221-2720]-XXXX-XXXX-XXXX
    _amex=r'3[47]\d{2}[ -]?\d{6}[ -]?\d{5}',  # 3[47]XX XXXXXX XXXXX
    _discover=r'6(?:011|5\d{2})[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}',  # 6011-XXXX-XXXX-XXXX or 65XX-XXXX-XXXX-XXXX
)

# Visa, Mastercard, Amex, Discover
STRICT_CREDIT_CARD = re.compile(r'|'.join(_cards.values()))
LOOSE_CREDIT_CARD = re.compile(r'[0-9-]{13,20}')


class _DeprecatedRegex(object):
    """Warn about deprecated expressions, but keep their functionality."""
    def __init__(self, regex: re.Pattern, old: str, new=str.upper):
        if callable(new):
            new = new(old)
        self.msg = f'\nThe `{old}` constant has been renamed `{new}` and is deprecated.  Use:\n\n\t>>> from re101 import {new}\n'
        self.regex = regex
        self.old = old
        self.new = new

    def __getattr__(self, name):
        """Call __getattr__ for the newly-named re.Pattern."""
        if 'name' in {'old' 'new', 'regex', 'msg'}:
            return getattr(self, name)
        warnings.warn(self.msg, FutureWarning, stacklevel=2)
        return eval(self.new).__getattribute__(name)


email = _DeprecatedRegex(regex=EMAIL, old='email')
mult_whitespace = _DeprecatedRegex(regex=MULT_WHITESPACE, old='mult_whitespace')
mult_spaces = _DeprecatedRegex(regex=MULT_SPACES, old='mult_spaces')
word = _DeprecatedRegex(regex=WORD, old='word')
adverb = _DeprecatedRegex(regex=ADVERB, old='adverb')
ipv4 = IPv4 = _DeprecatedRegex(regex=IPV4, old='ipv4')
moneysign = _DeprecatedRegex(regex=MONEYSIGN, old='moneysign')

zipcode = _DeprecatedRegex(regex=US_ZIPCODE, old='zipcode', new='US_ZIPCODE')
state = _DeprecatedRegex(regex=US_STATE, old='state', new='US_STATE')
nanp_phonenum = _DeprecatedRegex(regex=US_PHONENUM, old='state', new='US_PHONENUM')

# Functions, classes that make re.Patterns with __new__(), and constants
# ---------------------------------------------------------------------
__all__ = (
    'not_followed_by',
    'followed_by',
    'Number',
    'Integer',
    'Decimal',
    'extract_pw',
    'extract_un',
)
# Bring uppercase constants into the namespace.
_locals = locals()
__all__ = __all__ + tuple(
    i for i in _locals if i.isupper() and not i.startswith('_'))
del _locals
