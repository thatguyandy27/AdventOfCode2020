def readFile(path='./Day11/input.txt'):
    f = open(path, 'r')
    lines = f.readlines()
    floor = []
    for l in lines:
        row = []
        for c in l:
            if c == '.':
                row.append(-1)
            elif c == 'L':
                row.append(0)

        floor.append(row)

    return floor


def getNeighborsCount(floor, i, j):
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1),
                 (i, j-1),  (i, j+1),
                 (i + 1, j - 1), (i + 1, j), (i+1, j+1)]

    maxi = len(floor)
    maxj = len(floor[0])
    count = 0
    for neighbor in neighbors:
        (i, j) = neighbor
        if i >= 0 and j >= 0 and i < maxi and j < maxj and floor[i][j] != -1:
            count += floor[i][j]

    return count


def runSimulation(floor):
    update = []
    change = False
    count = 0
    for i in range(len(floor)):
        row = floor[i]
        newRow = []

        for j in range(len(row)):
            if floor[i][j] == -1:
                newRow.append(-1)
            else:
                neighborCount = getNeighborsCount(floor, i, j)

                if neighborCount == 0:
                    newRow.append(1)
                elif neighborCount >= 4:
                    newRow.append(0)
                else:
                    newRow.append(row[j])

                change = change or newRow[j] != row[j]
                count += newRow[j]

        update.append(newRow)

    return update, change, count


def getNeighborsCount2(floor, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),  (0, 1),
                  (1, - 1), (1, 0), (1, 1)]

    maxi = len(floor)
    maxj = len(floor[0])
    count = 0
    for direction in directions:
        (di, dj) = direction
        x = i + di
        y = j + dj

        neighbor = 0
        while x >= 0 and y >= 0 and x < maxi and y < maxj:
            if floor[x][y] == -1:
                x = x + di
                y = y + dj
            else:
                neighbor = floor[x][y]
                break

        count += neighbor

    return count


def runSimulation2(floor):
    update = []
    change = False
    count = 0
    for i in range(len(floor)):
        row = floor[i]
        newRow = []

        for j in range(len(row)):
            if floor[i][j] == -1:
                newRow.append(-1)
            else:
                neighborCount = getNeighborsCount2(floor, i, j)

                if neighborCount == 0:
                    newRow.append(1)
                elif neighborCount >= 5:
                    newRow.append(0)
                else:
                    newRow.append(row[j])

                change = change or newRow[j] != row[j]
                count += newRow[j]

        update.append(newRow)

    return update, change, count


def findFinalCount():
    floor = readFile()
    change = True
    count = 0
    round = 0
    while change:
        round += 1
        print('Round {}'.format(round))
        floor, change, count = runSimulation(floor)

    print(count)


def findFinalCount2():
    floor = readFile()
    change = True
    count = 0
    round = 0
    while change:
        round += 1
        print('Round {}'.format(round))
        floor, change, count = runSimulation2(floor)

    print(count)


if __name__ == "__main__":
    # print(findFinalCount())
    print(findFinalCount2())
