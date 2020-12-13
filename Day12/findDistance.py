
def loadFile(path='./Day12/input.txt'):
    f = open(path, 'r')
    path = []
    for l in f:
        path.append((l[0], int(l[1:])))

    return path


DIR_TO_NUM = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
NUM_TO_DIR = ['N', 'E', 'S', 'W']


def getTurnDirection(currDir, degrees):
    turns = degrees // 90
    num = DIR_TO_NUM[currDir]

    newDir = (num + turns) % 4

    return NUM_TO_DIR[newDir]


def findDistance():
    path = loadFile()

    x = 0
    y = 0
    direction = 'E'

    for (cmd, dst) in path:
        # print('CMD: {}, DST: {}'.format(cmd, dst))

        if cmd == 'R':
            direction = getTurnDirection(direction, dst)
        elif cmd == 'L':
            direction = getTurnDirection(direction, -dst)
        else:
            moveDir = cmd
            if cmd == 'F':
                moveDir = direction

            if moveDir == 'N':
                y += dst
            elif moveDir == 'S':
                y -= dst
            elif moveDir == 'E':
                x += dst
            else:
                x -= dst

        # print('X: {}, Y: {}, D: {}'.format(x, y, direction))

    print('X: {}, Y: {}'.format(x, y))
    print(abs(x) + abs(y))


def findDistance2():
    path = loadFile()

    x = 10
    y = 1
    shipX = 0
    shipY = 0

    for (cmd, dst) in path:
        if cmd == 'N':
            y += dst
        elif cmd == 'S':
            y -= dst
        elif cmd == 'E':
            x += dst
        elif cmd == 'W':
            x -= dst
        elif cmd == 'F':
            shipX += dst * x
            shipY += dst * y
        elif cmd == 'R':
            turns = dst // 90
            for t in range(turns):
                x, y = (y, -x)
        else:
            turns = dst // 90
            for t in range(turns):
                x, y = (-y, x)

    print('X: {}, Y: {}'.format(shipX, shipY))
    print(abs(shipX) + abs(shipY))


if __name__ == "__main__":
    # findDistance()
    findDistance2()
