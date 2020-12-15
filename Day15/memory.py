
def getInput():
    return [15, 12, 0, 14, 3, 1]


def findNumber(input, n):
    memory = {}

    currentTurn = 0
    lastNumber = -1
    for i in input:
        # SPEAK lastNumber
        memory[lastNumber] = currentTurn
        lastNumber = i
        currentTurn += 1

    while currentTurn < n:
        if lastNumber in memory:
            nextNumber = currentTurn - memory.get(lastNumber)
        else:
            nextNumber = 0
        memory[lastNumber] = currentTurn
        lastNumber = nextNumber
        # print(lastNumber)
        currentTurn += 1

    print(lastNumber)


if __name__ == "__main__":
    # findNumber([1, 3, 2], 2020)  # 1
    # findNumber([2, 1, 3], 2020)  # 10
    # findNumber([3, 1, 2], 2020)  # 1836
    # findNumber([0, 3, 6], 10)
    # findNumber(getInput(), 2020)
    findNumber(getInput(), 30000000)
