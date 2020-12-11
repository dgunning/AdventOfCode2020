from day04 import get_passports, is_strictly_valid, is_valid
from tools import get_puzzle_input

puzzle_input = get_puzzle_input('dec04')


def get_test_passports(text: str):
    return list(get_passports(text.strip().splitlines()))


def test_puzzle_input():
    assert puzzle_input[0].startswith('eyr:2024')
    assert puzzle_input[-1].startswith('cid:294')


def test_passports():
    passports = list(get_passports(puzzle_input))
    assert len(passports) == 282
    assert passports[0]['eyr'] == '2024'
    assert passports[-1]['cid'] == '294'


def test_invalid_passports():
    passports = get_test_passports(
        """
        eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
    
        iyr:2019
        hcl:#602927 eyr:1967 hgt:170cm
        ecl:grn pid:012533040 byr:1946
    
        hcl:dab227 iyr:2012
        ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
    
        hgt:59cm ecl:zzz
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007
        
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:2003
        hcl:#623a2f
        
        pid:087499704 hgt:190in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        
        pid:087499704 hgt:190 ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        
        pid:087499704 hgt:190in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#123abz
        
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:123abc
        
        pid:087499704 hgt:74in ecl:wat iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        
        pid:0123456789 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
            """
    )

    assert passports[0]['eyr'] == '1972'
    assert is_valid(passports[0])

    for p in passports:
        assert not is_strictly_valid(p)


def test_passport_pid():
    passport = get_test_passports(
        """
        pid:0123456789 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f
        """)[0]
    assert not is_strictly_valid(passport)


def test_valid_passports():
    passports = get_test_passports(
        """
    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f
    
    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
    
    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022
    
    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
                """
    )

    assert len(passports) == 4
    assert passports[0]['eyr'] == '2030'
    assert is_valid(passports[0])

    for p in passports:
        assert is_strictly_valid(p)
