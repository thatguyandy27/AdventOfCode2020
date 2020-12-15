
def readFile(path='./Day14/input.txt'):
    f = open(path, 'r')

    return f.readlines()


def updateMasks(value):
    andMask = value.replace('X', '1')
    orMask = value.replace('X', '0')

    return int(andMask, 2), int(orMask, 2)


def applyMask(value, andMask, orMask):
    return (value | orMask) & andMask


def emulate():
    commands = readFile()
    memory = {}

    andMask = 0
    orMask = 2 ^ 36 - 1
    for command in commands:
        cmd, value = command.split(' = ')
        if cmd == 'mask':
            andMask, orMask = updateMasks(value)
        else:
            # mem[33280]
            address = int(cmd[4:-1])
            memory[address] = applyMask(int(value), andMask, orMask)

    total = 0
    for key in memory:
        total += memory[key]

    print(total)


def applyAddressMask(address, mask):
    orMask = mask.replace('O', '0')
    andMask = mask.replace('0', '1').replace('O', '0')
    # print(orMask)
    # print(andMask)
    newAddr = (address | int(orMask, 2)) & int(andMask, 2)
    # print(newAddr)
    return newAddr


def generateMemoryAddresses(address, mask):
    if not 'X' in mask:
        return [applyAddressMask(address, mask)]

    addresses = []

    addresses.extend(generateMemoryAddresses(
        address, mask.replace('X', 'O', 1)))
    addresses.extend(generateMemoryAddresses(
        address, mask.replace('X', '1', 1)))

    return addresses


def emulate2(path='./Day14/input.txt'):
    commands = readFile(path)
    memory = {}

    mask = '0'
    for command in commands:
        cmd, value = command.split(' = ')
        if cmd == 'mask':
            mask = value
        else:
            # mem[33280]
            address = int(cmd[4:-1])

            addresses = generateMemoryAddresses(address, mask)
            val = int(value)
            for addr in addresses:
                memory[addr] = val

    total = 0
    for key in memory:
        total += memory[key]

    print(total)


if __name__ == "__main__":
    # emulate()
    # emulate2('./Day14/test.txt')
    emulate2()
