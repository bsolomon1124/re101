import re
from re import Pattern

import pytest

import re101

# Each key is a variable defined in re101.py.  Each key is a dictionary
# consisting of both valid and invalid cases for testing.

SEARCH_CASES = {
    'EMAIL': {
        'valid': [
            'b@d.net',
            '1@d.net',
            'b@domain.net',
            'bob123@alice123.com',
            'BOB.123bob@Alice.net',
            'very.common@example.com',
            'niceandsimple@example.com',
            'a.little.lengthy.but.fine@dept.example.com',
            'disposable.style.email.with+156@example.com',
            'disposable.style.email.with+symbol@example.com',
            '"very.unusual.@.unusual.com"@example.com',
        ],
        'invalid': [
            'hfij#kjdfvkl',
            'Abc.example.com',
            'this is not true',
            '@foo.com',
            'asterisk_domain@foo.*',
            'not allowed @example.com',
        ],
    },
    'IPV4': {
        'valid': [
            '192.0.2.1',
            '192.168.0.1',
            '105.007.0.9',
            '192.168.000.001',
            '01.02.03.04',
            '0.200.200.100',
            '007.200.200.100',
        ],
        'invalid': [
            '2001:db8::0/96',
            '192.168.008.010',
            '2001:db8::1000',
            '08.200.200.100',
            '257.0.0.0',
        ],
    },
    'US_PHONENUM': {
        'valid': [
            '610-249-3976',
            '1-213-555-0123',
            '234-911-5678',
            '675-0100',
            '+1 484 799 4985',
            '1 484 799 4985',
            '1 8005551234',
            '4847985154',
            '1 (484) 799-4985',
            '1.484.799.4985',
            '1(484)799-4985',
            '(484) 799-4985',
        ],
        'invalid': ['159-2653', '1 159 2653', '123-234-5678', '314-159-2653'],
    },
    'STRICT_URL': {
        'valid': [
            'https://www.google.com',
            'https://www.sec.gov/edgar/searchedgar/companysearch.html',
        ],
        'invalid': ['www.google.com', 'google.com', 'https:// this is a website.com/ext'],
    },
    'LOOSE_URL': {
        'valid': [
            'https://www.google.com',
            'https://www.sec.gov/edgar/searchedgar/companysearch.html',
            'www.google.com',
            'www.group.me',
        ],
        'invalid': ['https:// this is a website.com/ext', 'www. this is a website.com/ext'],
    },
    'LOOSE_URL_DOMAIN': {
        'valid': [
            'group.me',
            'bit.ly/',
            'https://www.google.com',
            'https://www.sec.gov/edgar/searchedgar/companysearch.html',
        ],
        'invalid': [],
    },
    'USERNAME': {
        'valid': [
            'username is abcdef',
            'username: abcd__ie8',
            'USERNAME : CAPTAIN_KIRK',
        ],
        'invalid': ['Username cannot be found', 'Invalid password'],
    },
    'PASSWORD': {
        'valid': [
            'pw is abcdef',
            'password: abcd__ie8',
            'PASSWORD : CAPTAIN_KIRK',
        ],
        'invalid': ['Password cannot be found', 'Invalid password'],
    },
    'STRICT_SSN': {
        'valid': ['123-45-6789', 'my ssn is 123-45-6789'],
        'invalid': ['123-456789', 'my ssn is 123 45 6789', '123456789'],
    },
    'LOOSE_SSN': {
        'valid': [
            '123-45-6789',
            'my ssn is 123-45-6789',
            '123 45 6789',
            'my ssn is 123456789',
        ],
        'invalid': ['12345678', '12-345-67890'],
    },
    'STRICT_CREDIT_CARD': {
        'valid': ['4400 6940 3849 3940', '3791-485930-30495'],
        'invalid': ['1234567890'],
    },
    'US_PASSPORT': {
        'valid': ['767898909', '31195855', 'C03005899', '100003106', '457098126', 'C03004786'],
        'invalid': ['1234567890', 'CC123456', '1345_6789'],
    },
}

class_cases = {
    'Decimal': {
        'valid': [
            '2.0',
            '0.2',
            '.2',
            '.225',
            '25.05',
            '250.50',
            '1,225,000.0',
            '4,500.5',
            '255.05',
            '.05',
        ],
        'invalid': [
            '2,000',
            '6,999,999',
            '4000',
            '4',
            '0',
            '076',
        ],
    },
    'Integer': {
        'valid': ['2,000', '6,999,999', '4000', '50000', '4', '0', '076'],
        'invalid': [
            '2,,000',
            '299,1234,12345',
            '4.00',
            '.1',
            '0.1',
            '$100',
            '2,000,000.00',
        ],
    },
    'Number': {
        'valid': [
            '2,000',
            '6,999,999',
            '4000',
            '50000',
            '4',
            '0',
            '076',
            '2.0',
            '0.2',
            '.2',
            '.225',
            '25.05',
            '250.50',
            '1,225,000.0',
            '4,500.5',
            '255.05',
            '.05',
        ],
        'invalid': [
            '2,,000',
            '299,1234,12345',
            '$100',
            '2,0002,00022.002',
            '076.00.004.00',
        ],
    },
}


@pytest.mark.parametrize(
    ('regex', 'string'),
    [(getattr(re101, k), i) for k, v in SEARCH_CASES.items() for i in v['valid']],
)
def test_regex_search_positive_constant(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert bool(regex.search(string))


# ---------------------------------------------------------------------
# Additional search-based coverage for regexes not covered above.

EXTRA_SEARCH_CASES = {
    'LOOSE_EMAIL': {
        'valid': ['me@here', 'a.b.c@d.e.f'],
        'invalid': ['no at sign', ''],
    },
    'MULT_WHITESPACE': {
        'valid': ['hello  world', 'a\t\tb', 'x\n\ny'],
        'invalid': ['single spaces here', ''],
    },
    'MULT_SPACES': {
        'valid': ['a  b', 'x     y'],
        'invalid': ['a\t\tb', 'single'],
    },
    'WORD': {
        'valid': ['hello', 'word1 word2'],
        'invalid': ['!!!', '   '],
    },
    'ADVERB': {
        'valid': ['really', 'quickly jumped'],
        'invalid': ['jump', 'run fast'],
    },
    'E164_PHONENUM': {
        'valid': ['+14155551234', '14155551234'],
        'invalid': ['abc', ''],
    },
    'IPV6': {
        'valid': ['2001:db8::1', '::1', 'fe80::1'],
        'invalid': ['not an ip', '999.999.999.999'],
    },
    'US_ZIPCODE': {
        'valid': ['90210', '19104-1234', 'zip is 02139'],
        'invalid': ['1234', 'abcde'],
    },
    'US_STATE': {
        'valid': ['I live in CA', 'NY, NY', 'from TX'],
        'invalid': ['ZZ', 'XX'],
    },
    'US_ADDRESS': {
        'valid': ['223 Park Lane', '500 5th Ave', '42 Wallaby Way'],
        'invalid': ['no address here', 'lowercase rd.'],
    },
    'DOB': {
        'valid': ['dob: 1990-01-01', 'date of birth is 01/02/1990'],
        'invalid': ['no birth info here'],
    },
    'LOOSE_CREDIT_CARD': {
        'valid': ['4400-6940-3849-3940', '4400694038493940'],
        'invalid': ['12345', 'abcdef'],
    },
    'STRICT_URL': {
        'valid': ['file:///tmp/foo', 'ftp://example.com/file'],
        'invalid': ['bare text'],
    },
}


@pytest.mark.parametrize(
    ('regex', 'string'),
    [(getattr(re101, k), i) for k, v in EXTRA_SEARCH_CASES.items() for i in v['valid']],
)
def test_extra_regex_search_positive(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert regex.search(string) is not None


@pytest.mark.parametrize(
    ('regex', 'string'),
    [(getattr(re101, k), i) for k, v in EXTRA_SEARCH_CASES.items() for i in v['invalid']],
)
def test_extra_regex_search_negative(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert regex.search(string) is None


# MONEYSIGN is a string constant, not a compiled Pattern.
def test_moneysign_is_string_of_currency_symbols():
    assert isinstance(re101.MONEYSIGN, str)
    assert '$' in re101.MONEYSIGN
    assert '\u20ac' in re101.MONEYSIGN  # euro
    assert '\u00a3' in re101.MONEYSIGN  # pound


@pytest.mark.parametrize(
    ('regex', 'string'),
    [(getattr(re101, k), i) for k, v in SEARCH_CASES.items() for i in v['invalid']],
)
def test_regex_search_negative_constant(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert not bool(regex.search(string))


MATCH_CASES = {
    'EMAIL': {
        'invalid': [
            'hfij#kjdfvkl',
            'Abc.example.com',
            'this is not true',
            '@foo.com',
            'A@b@c@example.com',
            'asterisk_domain@foo.*',
            'just"not"right@example.com',
            'not allowed @example.com',
            r'stil not allowed@example.com',
            r'a"b(c)d,e:f;gi[j\k]l@example.com',
        ]
    }
}


@pytest.mark.parametrize(
    ('regex', 'string'),
    [(getattr(re101, k), i) for k, v in MATCH_CASES.items() for i in v['invalid']],
)
def test_regex_match_negative_constant(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert not bool(regex.match(string))


# ---------------------------------------------------------------------
# Number / Integer / Decimal classes.


@pytest.mark.parametrize(
    ('cls', 'string'),
    [(getattr(re101, k), s) for k, v in class_cases.items() for s in v['valid']],
)
def test_number_class_search_positive(cls, string):
    regex = cls()
    assert isinstance(regex, Pattern)
    assert regex.search(string) is not None


@pytest.mark.parametrize(
    ('cls', 'string'),
    [(getattr(re101, k), s) for k, v in class_cases.items() for s in v['invalid']],
)
def test_number_class_search_negative(cls, string):
    regex = cls()
    assert isinstance(regex, Pattern)
    assert regex.search(string) is None


@pytest.mark.parametrize('cls', [re101.Number, re101.Integer, re101.Decimal])
@pytest.mark.parametrize('leading_zeros', [True, False])
@pytest.mark.parametrize('commas', [True, False])
def test_number_class_options_produce_pattern(cls, leading_zeros, commas):
    regex = cls(allow_leading_zeros=leading_zeros, allow_commas=commas)
    assert isinstance(regex, Pattern)


def test_integer_without_leading_zeros_rejects_leading_zero():
    regex = re101.Integer(allow_leading_zeros=False)
    assert regex.search('076') is None
    assert regex.search('42') is not None


def test_integer_without_commas_rejects_commas():
    regex = re101.Integer(allow_commas=False)
    assert regex.search('1,000') is None
    assert regex.search('1000') is not None


def test_number_class_accepts_re_flags():
    regex = re101.Number(flags=re.MULTILINE)
    assert regex.flags & re.MULTILINE


# ---------------------------------------------------------------------
# Helper factories & extract_* functions.


def test_followed_by_and_not_followed_by():
    fb = re101.followed_by('cat')
    nfb = re101.not_followed_by('cat')
    text = 'big cat and old dog'
    assert fb.findall(text) == ['big']
    # "cat" itself is also a word not followed by "cat"
    assert 'old' in nfb.findall(text)
    assert 'big' not in nfb.findall(text)


def test_make_userinfo_re_matches_colon_equal_is():
    regex = re101.make_userinfo_re(r'token')
    for text in ['token: abc', 'token=abc', 'TOKEN is abc']:
        m = regex.search(text)
        assert m is not None
        assert m.group('token') == 'abc'


def test_extract_pw_and_un():
    text = 'username: alice, password = hunter2'
    assert re101.extract_un(text) == ['alice,']
    assert re101.extract_pw(text) == ['hunter2']


def test_extract_dob():
    assert re101.extract_dob('DOB: 1990-01-01') == ['1990-01-01']
    assert re101.extract_dob('no info') == []


def test_extract_us_drivers_license_by_state():
    assert re101.extract_us_drivers_license('A1234567', state='CA') == ['A1234567']
    assert re101.extract_us_drivers_license('A1234567', state='ca') == ['A1234567']


def test_extract_us_drivers_license_no_state_returns_list():
    result = re101.extract_us_drivers_license('CA id A1234567')
    assert isinstance(result, list)
    assert 'A1234567' in result


# ---------------------------------------------------------------------
# Package metadata / exports.


def test_package_metadata():
    assert re101.__version__ == '1.0.0'
    assert re101.__license__ == 'MIT'


def test_all_entries_are_importable():
    for name in re101.__all__:
        assert hasattr(re101, name), f'missing export: {name}'


def test_no_deprecated_wrapper_remains():
    assert not hasattr(re101, '_DeprecatedRegex')
    for legacy in ('email', 'ipv4', 'zipcode', 'nanp_phonenum'):
        assert not hasattr(re101, legacy), f'legacy alias {legacy!r} should be gone'
