
def parseCommand(line):
    command, arg = line.split(' ')
    return (command, int(arg))


def readFile(path='./Day8/input.txt'):
    f = open(path, 'r')

    commands = []
    for l in f:
        commands.append(parseCommand(l))

    return commands


def findAccumulator():
    visited = set()

    commands = readFile()
    cmdIdx = 0
    accumulator = 0

    while cmdIdx not in visited:
        visited.add(cmdIdx)
        cmd, arg = commands[cmdIdx]
        if cmd == 'acc':
            accumulator += arg
            cmdIdx += 1
        elif cmd == 'jmp':
            cmdIdx += arg
        else:
            cmdIdx += 1

    return accumulator


def findChange():
    visited = set()

    commands = readFile()
    found, result = tryChange(0, commands, False, 0, visited)
    if not found:
        print('you have done it wrong')

    return result


def tryChange(idx, commands, haveChanged, accumulator, visited):
    if idx >= len(commands):
        return True, accumulator

    if idx in visited:
        return False, -1

    visited.add(idx)
    cmd, arg = commands[idx]

    if cmd == 'acc':
        result, nextAccumulator = tryChange(
            idx + 1, commands, haveChanged, accumulator + arg, visited)
    elif cmd == 'jmp':
        result, nextAccumulator = tryChange(
            idx + arg, commands, haveChanged, accumulator, visited)

        if not result and not haveChanged:
            result, nextAccumulator = tryChange(
                idx + 1, commands, True, accumulator, visited)
    else:
        result, nextAccumulator = tryChange(
            idx + 1, commands, haveChanged, accumulator, visited)

        if not result and not haveChanged:
            result, nextAccumulator = tryChange(
                idx + arg, commands, True, accumulator, visited)

    visited.remove(idx)

    return result, nextAccumulator


if __name__ == "__main__":
    # print(findAccumulator())
    print(findChange())
