FILE_PATH = './Day3/input.txt'
FILE_PATH2 = './Day3/marked.txt'


def readMap(path):
    f = open(path, "r")
    treeMap = []

    for l in f:
        treeMap.append(list(l))

    f.close()
    return treeMap


def writeMap(path, content):
    f = open(path, 'w')
    for c in content:
        f.write(''.join(c) + '\n')
    f.close()


def countTrees(xDelta=3, yDelta=1):
    map = readMap(FILE_PATH)
    treeCount = 0
    x = 0
    yMax = len(map)
    xMas = len(map[0]) - 1
    for y in range(0, yMax, yDelta):
        xIdx = x % xMas
        # print('({}, {}) = {}'.format(xIdx, y, map[y][xIdx]))
        if map[y][xIdx] == '#':
            treeCount += 1
        #     map[y][xIdx] = 'X'
        # else:
        #     map[y][xIdx] = 'O'
        x += xDelta

    # writeMap(FILE_PATH2, map)
    return treeCount


def multiplyTrees():
    path1Trees = countTrees(1, 1)
    path2Trees = countTrees(3, 1)
    path3Trees = countTrees(5, 1)
    path4Trees = countTrees(7, 1)
    path5Trees = countTrees(1, 2)

    return path1Trees * path2Trees * path3Trees * path4Trees * path5Trees


if __name__ == "__main__":
    # print(countTrees())
    print(multiplyTrees())
