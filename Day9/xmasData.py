
def loadData(file='./Day9/input.txt'):
    f = open(file, 'r')
    numbers = []
    for l in f:
        numbers.append(int(l))

    return numbers


# def getValidSums(numbers):
#     sums = set()

#     for i in range(len(numbers)):
#         x = numbers[i]
#         for j in range(i + 1, len(numbers)):
#             y = numbers[j]
#             sums.add(x + y)

#     return sums

def isNumberValid(prevNums, number):
    sNums = sorted(prevNums)
    for i in range(len(sNums)):
        x = sNums[i]

        if x > number:
            return False

        for j in range(i + 1, len(sNums)):
            y = sNums[j]
            if x + y > number:
                break
            if x + y == number:
                return True

    return False


def findInvalidPacket():
    numbers = loadData()
    # sums = getValidSums(head)

    for i in range(25, len(numbers)):
        if not isNumberValid(numbers[i - 25: i], numbers[i]):
            print('found it {}'.format(numbers[i]))


def getMinMax(nums):
    return min(nums) + max(nums)


def findMinAndMax(number=144381670):
    numbers = loadData()

    counts = {}
    for i in range(len(numbers)):
        if numbers[i] < number:
            counts[i] = numbers[i]

    i = 0
    found = False
    while not found:
        i += 1
        keys = list(counts.keys())
        for idx in keys:
            count = counts[idx]
            if idx + i >= len(numbers):
                del counts[idx]

            newCount = count + numbers[idx + i]
            if newCount == number:
                print('found')
                print(getMinMax(numbers[idx: idx + i + 1]))
                found = True
            elif newCount > number:
                del counts[idx]
            else:
                counts[idx] = newCount


if __name__ == "__main__":
    findInvalidPacket()
    findMinAndMax()
