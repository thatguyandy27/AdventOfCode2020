FILE_PATH = './Day4/input.txt'


def parseData(recordData):
    record = {}

    for data in recordData:
        fieldPairs = data.split(' ')
        for fieldPair in fieldPairs:
            field, value = fieldPair.split(':')
            record[field] = value

            if field not in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']:
                print('What no!!! {}'.format(field))

    return record


def readFile(path):
    f = open(path, 'r')
    records = []

    recordData = []
    for l in f:
        l = l.strip()
        if l == '':
            record = parseData(recordData)
            records.append(record)
            recordData = []
        else:
            recordData.append(l)

    records.append(parseData(recordData))

    return records


def isPassportValid(record):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in requiredFields:
        if not field in record:
            print('missingField: {}.  {}'.format(field, record))
            return False

    return True


def checkPassports():
    records = readFile(FILE_PATH)
    print('{} passports'.format(len(records)))
    count = 0
    for rec in records:
        if isPassportValid(rec):
            count += 1

    return count


def validateBYR(byr):
    if not byr.isnumeric() or len(byr) != 4:
        return False

    byrNum = int(byr)
    return byrNum >= 1920 and byrNum <= 2002


def validateIYR(iyr):
    if not iyr.isnumeric() or len(iyr) != 4:
        return False

    iyrNum = int(iyr)
    return iyrNum >= 2010 and iyrNum <= 2020


def validateEYR(eyr):
    if not eyr.isnumeric() or len(eyr) != 4:
        return False

    eyrNum = int(eyr)
    return eyrNum >= 2020 and eyrNum <= 2030


def validateHeight(height):
    if len(height) < 4:
        return False
    if height[-2:] == 'cm':
        hVal = height[:-2]
        if hVal.isnumeric():
            hNum = int(hVal)
            return hNum <= 193 and hNum >= 150

    elif height[-2:] == 'in':
        hVal = height[:-2]
        if hVal.isnumeric():
            hNum = int(hVal)
            return hNum <= 76 and hNum >= 59

    return False


def validateHCL(hcl):
    if len(hcl) != 7 or hcl[0] != '#':
        return False

    validChars = '1234567890abcdef'

    for i in range(1, len(hcl)):
        if hcl[i] not in validChars:
            return False

    return True


def validateECL(ecl):
    validClr = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

    return ecl in validClr


def validatePID(pid):
    return len(pid) == 9 and pid.isnumeric()


def validatePassport(passport):
    if not isPassportValid(passport):
        return False

    if not validateBYR(passport['byr']):
        return False
    if not validateIYR(passport['iyr']):
        return False
    if not validateEYR(passport['eyr']):
        return False
    if not validateHeight(passport['hgt']):
        return False
    if not validateHCL(passport['hcl']):
        return False
    if not validateECL(passport['ecl']):
        return False
    if not validatePID(passport['pid']):
        return False

    return True


def validatePassports():
    records = readFile(FILE_PATH)
    count = 0
    for rec in records:
        if validatePassport(rec):
            count += 1

    return count


if __name__ == "__main__":
    # print(checkPassports())
    print(validatePassports())
