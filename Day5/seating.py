FILE_PATH = './Day5/input.txt'


def readFile(path):
    f = open(path, 'r')

    return f.readlines()


def findRow(boardingPass):
    minV = 0
    maxV = 127
    for i in range(7):
        mid = (maxV - minV) // 2 + minV
        if boardingPass[i] == 'F':
            maxV = mid
        else:
            mid += 1
            minV = mid

    if minV == maxV:
        return minV

    return minV


def findSeat(boardingPass):
    minV = 0
    maxV = 7
    for i in range(7, 10):
        mid = (maxV - minV) // 2 + minV
        if boardingPass[i] == 'L':
            maxV = mid
        else:
            mid += 1
            minV = mid

    if minV == maxV:
        return minV

    return minV


def getSeatId(row, seat):
    return row * 8 + seat


def getMaxSeatId():
    passes = readFile(FILE_PATH)
    maxId = 0
    for p in passes:
        row = findRow(p)
        seat = findSeat(p)
        seatId = getSeatId(row, seat)
        maxId = max(seatId, maxId)

    return maxId


def findMissingSeat():
    seats = []
    for r in range(128):
        seats.append([False, False, False, False, False, False, False, False])

    passes = readFile(FILE_PATH)
    for p in passes:
        row = findRow(p)
        seat = findSeat(p)
        # print(seats[row][seat])
        seats[row][seat] = True

    ids = []
    for r in range(128):
        for s in range(8):
            if seats[r][s]:
                seatId = getSeatId(r, s)
                ids.append(seatId)

    seatIds = set(ids)
    minId = min(ids)
    maxId = max(ids)

    for id in range(minId + 1, maxId):
        prevId = id - 1
        nextId = id + 1
        if prevId in seatIds and nextId in seatIds and id not in seatIds:
            print('{}, {} = {} '.format(prevId, nextId, id))

    # for r in range(128):
    #     for s in range(8):
    #         if not seats[r][s]:
    #             seatId = getSeatId(r, s)
    #             prevId = seatId - 1
    #             nextId = seatId + 1
    #             if prevId in seatIds and nextId in seatIds:
    #                 print('{}, {} = {} '.format(r, s, seatId))
    # print(ids)
    # print(seatIds)
    # for id in seatIds:
    #     prevId = id - 1
    #     nextId = id + 1
    #     # print(prevId, id, nextId)
    #     if prevId in seatIds and nextId in seatIds:
    #         print(id)


if __name__ == "__main__":
    # maxId = getMaxSeatId()
    # print(maxId)
    findMissingSeat()
    # print(findSeat('BFFFBBFLLL'))
    # print(findSeat('BFFFBBFLLR'))
    # print(findSeat('BFFFBBFLRL'))
    # print(findSeat('BFFFBBFLRR'))
    # print(findSeat('BFFFBBFRLL'))
    # print(findSeat('BFFFBBFRLR'))
    # print(findSeat('BFFFBBFRRL'))
    # print(findSeat('BFFFBBFRRR'))
