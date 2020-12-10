
def readFile(path='./Day10/input.txt'):
    f = open(path, 'r')
    nums = []
    for l in f:
        nums.append(int(l))

    return nums


def countCombos():
    nums = sorted(readFile())
    maxNum = nums[-1]

    cache = [0] * (maxNum + 1)

    print(len(cache))
    print(len(nums))
    # I know there is a one & 2
    cache[1] = 1
    cache[2] = 1 + cache[1]
    idx = 2
    if nums[3] == 3:
        cache[3] = 3
        idx = 3

    while idx < len(nums):
        num = nums[idx]

        cache[num] = cache[num - 1] + cache[num-2] + cache[num-3]
        print(num, cache[num], cache[num - 1],  cache[num-2], cache[num-3])
        idx += 1

    print(cache[-1])


def findJolts():
    nums = sorted(readFile())

    threeJumps = 1  # FUCKING DEVICE
    oneJumps = 0
    prevNum = 0
    for num in nums:
        diff = num - prevNum
        if diff > 3:
            print('WAT NO!')

        elif diff == 3:
            threeJumps += 1
        elif diff == 1:
            oneJumps += 1

        prevNum = num

    print(oneJumps * threeJumps)


if __name__ == "__main__":
    # findJolts()
    countCombos()
