
def readFile(path='./Day6/input.txt'):
    f = open(path, 'r')

    records = []
    record = []

    for l in f:
        l = l.strip()
        if l == '':
            records.append(record)
            record = []
        else:
            record.append(l)

    records.append(record)
    return records


def getAnswersForGroup(record):
    answered = set()
    for answers in record:
        answered.update(answers)

    return answered


def getTotalQuestionsAnswered():
    records = readFile()
    total = 0

    for record in records:
        answered = getAnswersForGroup(record)
        total += len(answered)

    return total


def getAnswersForWholeGroup(record):
    answered = {}
    for user in record:
        for answer in user:
            answered[answer] = answered.get(answer, 0) + 1

    return answered, len(record)


def getTotalQuestionsAllAnswered():
    records = readFile()
    total = 0

    for record in records:
        answered, groupTotal = getAnswersForWholeGroup(record)
        for k in answered:
            if answered[k] == groupTotal:
                total += 1
    return total


if __name__ == "__main__":
    # print(getTotalQuestionsAnswered())
    print(getTotalQuestionsAllAnswered())
