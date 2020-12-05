import re

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def part1(input: str):
    passports = _parsePassport(input)
    valid_count = 0
    for p in passports:
        if all(key in p.keys() for key in req_fields):
            valid_count += 1

    return valid_count

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def part2(input: str):
    passports = _parsePassport(input)
    valid_count = 0
    for p in passports:
        if (all(key in p.keys() for key in req_fields)
                and int(p['byr']) >= 1920 and int(p['byr']) <= 2002
                and int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020
                and int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030
                and _isValidHgt(p['hgt'])
                and re.fullmatch('#[a-f,0-9]+', p['hcl'])
                and re.fullmatch('(amb|blu|brn|gry|grn|hzl|oth)', p['ecl'])
                and re.fullmatch('\d{9}', p['pid'])):
            valid_count += 1

    return valid_count


def _isValidHgt(hgt: str):
    if not re.fullmatch('\d+(cm|in)', hgt):
        return False
    unit = hgt[-2:]
    value = int(hgt[:-2])
    if unit == 'cm':
        return (value >= 150 and value <= 193)
    else:
        return (value >= 59 and value <= 76)


def _parsePassport(input: str):
    lines = re.split('\s', input)
    passport = {}
    for l in lines:
        if(len(l) == 0):
            yield passport
            passport = {}
        else:
            entry = l.split(':')
            key = entry[0]
            value = entry[1]
            passport[key] = value
    yield passport


f = open('./day04/input.txt', 'r')
input = f.read()

print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')
