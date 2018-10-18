import re

import re101

SRE_PATTERN = type(re.compile(''))


def _validate_one(string, regex):
    return bool(regex.match(string))


def _test_valid_invalid(valid, invalid, regex):
    assert all(_validate_one(i, regex) for i in valid)
    assert sum(_validate_one(i, regex) for i in invalid) == 0


def test_valid_invalid():
    for k, v in cases.items():
        regex = getattr(re101, k)
        # Make sure we didn't acidentally insert a special class.
        assert isinstance(regex, SRE_PATTERN)
        _test_valid_invalid(valid=v['valid'], invalid=v['invalid'],
                            regex=regex)


# Each key is a variable defined in re101.py.  Each key is a dictionary
# consisting of both valid and invalid cases for testing.

cases = {

    'email': dict(
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
            'this is"not\allowed@example.com',
            'a"b(c)d,e:f;gi[j\k]l@example.com',
            'this\ still"not\allowed@example.com'
            ]
        ),

    'ipv4': dict(
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

    'nanp_phonenum': dict(
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
        )
    }


# TODO

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
