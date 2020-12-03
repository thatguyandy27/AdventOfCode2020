
FILE_PATH = './Day2/input.txt'


def parseCodes(codeLine):
    policy, code = codeLine.split(':')
    times, letter = policy.split(' ')
    min, max = times.split('-')
    return {
        'min': int(min),
        'max': int(max),
        'letter': letter,
        'code': code.strip()
    }


def readCodes(path):
    f = open(path, "r")
    codes = []

    for l in f:
        codes.append(parseCodes(l))
    return codes


def countValidCodes():
    codes = readCodes(FILE_PATH)
    count = 0
    for code in codes:
        letterCount = code['code'].count(code['letter'])
        if letterCount <= code['max'] and letterCount >= code['min']:
            count += 1

    return count


def countValidCodes2():
    codes = readCodes(FILE_PATH)
    count = 0
    for code in codes:
        letterCount = 0
        if code['code'][code['min'] - 1] == code['letter']:
            letterCount += 1
        if code['code'][code['max'] - 1] == code['letter']:
            letterCount += 1
        if letterCount == 1:
            count += 1

    return count


if __name__ == "__main__":
    print(countValidCodes())
    print(countValidCodes2())
