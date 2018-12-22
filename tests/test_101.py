import re
from typing.re import Pattern

import pytest

import re101

# Each key is a variable defined in re101.py.  Each key is a dictionary
# consisting of both valid and invalid cases for testing.

SEARCH_CASES = {

    'EMAIL': dict(
        valid=[
            'b@d.net',
            '1@d.net',
            'b@domain.net',
            'bob123@alice123.com',
            'BOB.123bob@Alice.net'
            'very.common@example.com',
            'niceandsimple@example.com',
            'a.little.lengthy.but.fine@dept.example.com',
            'disposable.style.email.with+156@example.com',
            'disposable.style.email.with+symbol@example.com',
            '"very.unusual.@.unusual.com"@example.com'
            ],
        invalid=[
            'hfij#kjdfvkl',
            'Abc.example.com',
            'this is not true',
            '@foo.com',
            'A@b@c@example.com',
            'asterisk_domain@foo.*',
            'just"not"right@example.com',
            'not allowed @example.com',
            r'a"b(c)d,e:f;gi[j\k]l@example.com',
            ]
        ),

    'IPV4': dict(
        valid=[
            '192.0.2.1',
            '192.168.0.1',
            '105.007.0.9',
            '192.168.000.001',
            '01.02.03.04',
            '0.200.200.100',
            '007.200.200.100'
            ],
        invalid=[
            '2001:db8::0/96',
            '192.168.008.010',
            '2001:db8::1000',
            '08.200.200.100',
            '257.0.0.0',
            ]
        ),

    'US_PHONENUM': dict(
        valid=[
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
        invalid=[
            '159-2653',
            '1 159 2653',
            '123-234-5678',
            '314-159-2653'
            ]
        ),

    'STRICT_URL': dict(
        valid=[
            'https://www.google.com',
            'https://www.sec.gov/edgar/searchedgar/companysearch.html'
            ],
        invalid=[
            'www.google.com',
            'google.com',
            'https:// this is a website.com/ext'
            ]
        ),

    'LOOSE_URL': dict(
        valid=[
            'https://www.google.com',
            'https://www.sec.gov/edgar/searchedgar/companysearch.html',
            'www.google.com',
            'www.group.me'
            ],
        invalid=[
            'https:// this is a website.com/ext',
            'www. this is a website.com/ext'
            ]
        ),

    'LOOSE_URL_DOMAIN': dict(
        valid=[
            'group.me',
            'bit.ly/',
            'https://www.google.com',
            'https://www.sec.gov/edgar/searchedgar/companysearch.html'
            ],
        invalid=[

            ]
        ),

    'USERNAME': dict(
        valid=[
            'username is abcdef',
            'username: abcd__ie8'
            'USERNAME : CAPTAIN_KIRK',
            ],
        invalid=[
            'Username cannot be found',
            'Invalid password'
            ]
        ),

    'PASSWORD': dict(
        valid=[
            'pw is abcdef',
            'password: abcd__ie8'
            'PASSWORD : CAPTAIN_KIRK',
            ],
        invalid=[
            'Password cannot be found',
            'Invalid password'
            ]
        ),

    'STRICT_SSN': dict(
        valid=[
            '123-45-6789',
            'my ssn is 123-45-6789'
            ],
        invalid=[
            '123-456789',
            'my ssn is 123 45 6789',
            '123456789'
            ]
        ),

    'LOOSE_SSN': dict(
        valid=[
            '123-45-6789',
            'my ssn is 123-45-6789'
            '123 45 6789',
            'my ssn is 123456789'
            ],
        invalid=[
            '12345678',
            '12-345-67890'
            ]
        ),

    'STRICT_CREDIT_CARD': dict(
        valid=[
            '4400 6940 3849 3940',
            '3791-485930-30495'
            ],
        invalid=[
            '1234567890'
            ]
        ),

    'US_PASSPORT': dict(
        valid=[
            '767898909',
            '31195855',
            'C03005899',
            '100003106',
            '457098126',
            'C03004786'
            ],
        invalid=[
            '1234567890',
            'CC123456',
            '1345_6789'
            ]
        )
    }

class_cases = {

    'Decimal': dict(
        valid=[
            '1.',
            '2.0',
            '0.2',
            '.2',
            '.225',
            '25.05',
            '250.50',
            '0.',
            '1,225,000.0',
            '4,500.5'
            '255.05',
            '.05',
            '+.05',
            '-.05',
            '+2.',
            '-2.5'
            ],
        invalid=[
            '2,000',
            '6,999,999',
            '4000',
            '4',
            '0',
            '076'
            ]
        ),

    'Integer': dict(
        valid=[
            '2,000',
            '6,999,999',
            '4000',
            '50000',
            '4',
            '0',
            '076'
            ],
        invalid=[
            '2,,000',
            '299,1234,12345',
            '4000,000',
            '4.00',
            '4.',
            '.1',
            '0.1',
            '$100',
            '2,000,000.00'
            ]
        ),

    'Number': dict(
        valid=[
            '2,000',
            '6,999,999',
            '4000',
            '50000',
            '4',
            '0',
            '076',
            '1.',
            '2.0',
            '0.2',
            '.2',
            '.225',
            '25.05',
            '250.50',
            '0.',
            '1,225,000.0',
            '4,500.5'
            '255.05',
            '.05',
            '+.05',
            '-.05',
            '+2.',
            '-2.5'
            ],
        invalid=[
            '2,,000',
            '299,1234,12345',
            '$100',
            '2,0002,00022.002'
            '076.00.004.00'
            ]
        ),
    }


@pytest.mark.parametrize(
    'regex,string',
    [(getattr(re101, k), i) for k, v in SEARCH_CASES.items() for i in v['valid']]
)
def test_regex_search_positive_constant(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert bool(regex.search(string))


@pytest.mark.parametrize(
    'regex,string',
    [(getattr(re101, k), i) for k, v in SEARCH_CASES.items() for i in v['invalid']]
)
def test_regex_search_negative_constant(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert not bool(regex.search(string))


MATCH_CASES = {
    'EMAIL': dict(
        invalid=[
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
        )
}


@pytest.mark.parametrize(
    'regex,string',
    [(getattr(re101, k), i) for k, v in MATCH_CASES.items() for i in v['invalid']]
)
def test_regex_search_negative_constant(regex: Pattern, string: str):
    assert isinstance(regex, Pattern)
    assert not bool(regex.match(string))


def test_deprecated_regex():
    depr = [getattr(re101, i) for i in dir(re101)
            if isinstance(getattr(re101, i), re101._DeprecatedRegex)]
    assert depr  # TODO
