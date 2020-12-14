
def readFile(path='./Day13/input.txt'):
    f = open(path, 'r')
    lines = f.readlines()
    id = int(lines[0])
    busses = lines[1]

    return id, busses


def getBusIds(busses):
    bussArray = busses.split(',')
    ids = []
    for id in bussArray:
        if id != 'x':
            ids.append(int(id))

    return ids


def findEarliestBus():
    id, busses = readFile()
    busIds = getBusIds(busses)

    bestBusId = 0
    # timeStamp = 0
    bestWaitTime = id * id

    for busId in busIds:
        waitTime = id % busId
        # trip = id // bid

        if waitTime != 0:
            waitTime = busId - waitTime
            # trip += 1

        if bestWaitTime > waitTime:
            bestWaitTime = waitTime
            bestBusId = busId

    print('{} * {} = {}'.format(bestBusId, bestWaitTime, bestBusId * bestWaitTime))


def getOffsets(busses):
    busIds = busses.split(',')
    offsets = []
    for i in range(len(busIds)):
        bId = busIds[i]
        if bId != 'x':
            x = int(bId)
            offsets.append(((x - i) % x, x))

    return offsets


def crt(nums):
    N = 1
    for b, id in nums:
        N *= id

    n = []
    for b, id in nums:
        n.append(N // id)

    x = []
    for i in range(len(nums)):
        x.append(pow(n[i], -1, nums[i][1]))

    b = list(map(lambda x: x[0], nums))

    products = []
    for i in range(len(nums)):
        products.append(b[i] * n[i] * x[i])
    # print(b)
    # print(n)
    # print(x)
    # print(products)
    total = sum(products)
    # print(total)
    # print(N)
    print(total % N)


def findSubsequentDepartures():
    _, busses = readFile()
    offsets = getOffsets(busses)

    N = 1
    for offset, id in offsets:
        N *= id

    n = []
    for offset, id in offsets:
        n.append(N // id)
        # print(n)

    x = []

    for i in range(len(offsets)):
        xi = pow(n[i], -1, offsets[i][1])
        # print(xi)
        x.append(n[i] * offsets[i][0] * xi)
        # print(x)

    print(sum(x) % N)

    # offset, maxId = max(offsets, key=lambda x: x[1])

    # i = 1
    # found = False
    # while not found:
    #     multiple = maxId * i
    #     found = True
    #     for (o, id) in offsets:
    #         expected = multiple - (offset - o)
    #         remainder = expected % id
    #         if remainder != 0:
    #             found = False
    #             break

    #     i += 1
    #     print(multiple)

    # print(offset)


def findSubsequentDepartures2(path='./Day13/input.txt'):
    _, busses = readFile(path)
    offsets = getOffsets(busses)
    print(offsets)
    crt(offsets)


if __name__ == "__main__":
    # findEarliestBus()
    findSubsequentDepartures()
    findSubsequentDepartures2()
    # crt([(3, 5), (1, 7), (6, 8)])
