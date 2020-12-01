
FILE_PATH = './Day1/input.txt'


def getNumbers(path):
    f = open(path, "r")
    numbers = []
    for x in f:
        numbers.append(int(x))
    return numbers


def find2020():
    numbers = getNumbers(FILE_PATH)
    numSet = set(numbers)

    if len(numbers) != len(numSet):
        print("WARNING: DUPE NUMBERS")

    for n in numbers:
        diff = 2020 - n
        if diff in numSet:
            print("FOUND: {} * {} = {}".format(n, diff, n * diff))
            return

    print("ERROR NOT FOUND.  YOU IS WRONG ")


def createSums(numbers):
    sums = {}
    size = len(numbers)
    for i in range(size):
        n1 = numbers[i]
        for j in range(i + 1, size):
            n2 = numbers[j]
            sum = n1 + n2
            if sum < 2020:
                sumList = sums.get(sum, [])
                sumList.append(set([i, j]))
                sums[sum] = sumList
    return sums


def findThree2020():
    numbers = getNumbers(FILE_PATH)
    sums = createSums(numbers)
    # print(sums.keys())
    numSet = set(sums.keys())
    # print(numSet)
    for i in range(len(numbers)):
        n = numbers[i]
        diff = 2020 - n
        # print(diff)
        if diff in numSet:
            print("CANDIDATE FOUND: {} + {} ".format(n, diff))
            for sumSet in sums[diff]:
                if not i in sumSet:
                    diffIndicies = list(sumSet)
                    i2 = diffIndicies[0]
                    i3 = diffIndicies[1]
                    print(i, i2, i3)
                    product = numbers[i] * numbers[i2] * numbers[i3]
                    print("INDEXES: {} - {} - {}".format(i, i2, i3))
                    print(
                        "FOUND: {} * {} * {} = {}" .format(numbers[i], numbers[i2], numbers[i3], product))
                return

            print("CANDIDATE FAILED")

    print("ERROR NOT FOUND.  YOU IS WRONG ")


if __name__ == "__main__":
    # find2020()
    findThree2020()
