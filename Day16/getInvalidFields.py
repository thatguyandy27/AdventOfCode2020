
def loadRanges(path='./Day16/rules.txt'):
    f = open(path, 'r')

    ranges = []
    for l in f:
        r = l.split(': ')[1]
        r1, r2 = r.split(' or ')

        num1, num2 = r1.split('-')
        ranges.append((int(num1), int(num2)))
        num1, num2 = r2.split('-')
        ranges.append((int(num1), int(num2)))

    return ranges


def loadRanges2(path='./Day16/rules.txt'):
    f = open(path, 'r')
    fields = []
    ranges = []
    for l in f:
        field, r = l.split(': ')
        fields.append(field)
        r1, r2 = r.split(' or ')
        fieldRanges = []
        num1, num2 = r1.split('-')
        fieldRanges.append((int(num1), int(num2)))
        num1, num2 = r2.split('-')
        fieldRanges.append((int(num1), int(num2)))
        ranges.append(fieldRanges)

    return fields, ranges


def loadTickets(path='./Day16/neighbors.txt'):
    tickets = []
    f = open(path, 'r')

    for l in f:
        ticket = []
        data = l.split(',')
        for d in data:
            ticket.append(int(d))
        tickets.append(ticket)

    return tickets


def loadTicketNumbers(path='./Day16/neighbors.txt'):
    tickets = []
    f = open(path, 'r')

    for l in f:
        ticket = []
        data = l.split(',')
        for d in data:
            ticket.append(int(d))
        tickets.extend(ticket)

    return tickets


def getMaxTicketNum(tickets):
    m = 0
    for t in tickets:
        m = max(t, m)
    return m


def getValidNumbers(ranges, maxNum):
    ranges = sorted(ranges, key=lambda x: x[0])

    numbers = [False] * (maxNum + 1)

    ri = 0
    i = 0

    (rMin, rMax) = ranges[0]
    while i <= maxNum:
        for t in range(rMin, rMax + 1):
            numbers[t] = True

        i = rMax + 1
        ri += 1
        if ri == len(ranges):
            break

        (rMin, rMax) = ranges[ri]
        while rMax < ri:
            ri += 1
            (rMin, rMax) = ranges[ri]

        # skip those already done
        rMin = max(i, rMin)

    return numbers


def getValidTickets(tickets):
    nums = loadTicketNumbers()
    maxNum = getMaxTicketNum(nums)
    ranges = loadRanges()
    validNumbers = getValidNumbers(ranges, maxNum)

    validTickets = []
    l = len(tickets)

    for i in range(len(tickets)):
        ticket = tickets[i]
        valid = True
        for tVal in ticket:
            if not validNumbers[tVal]:
                valid = False

        if valid:
            validTickets.append(ticket)

    return validTickets


def tryTestData():
    invalid = 0
    tickets = loadTicketNumbers('./Day16/test_neighbors.txt')
    maxNum = getMaxTicketNum(tickets)
    ranges = loadRanges('./Day16/test_rules.txt')
    validNumbers = getValidNumbers(ranges, maxNum)

    for i in tickets:
        if not validNumbers[i]:
            invalid += i

    print(invalid)


def loadMyTicket():
    return [191, 139, 59, 79, 149, 83, 67, 73, 167, 181, 173, 61, 53, 137, 71, 163, 179, 193, 107, 197]


def cleanupPotentialMatches(validFields, field, column, myTicket):
    cleanup = [(field, column)]

    while len(cleanup) > 0:
        (field, c) = cleanup.pop()
        for c2 in range(len(myTicket)):
            if c2 != c and field in validFields[c2]:
                validFields[c2].remove(field)
                if len(validFields[c2]) == 1:
                    validField = validFields[c2].pop()
                    validFields[c2].add(validField)
                    cleanup.append((validField, c2))

    return validFields


def getDepartureNumbers():
    fields, ranges = loadRanges2()
    tickets = getValidTickets(loadTickets())
    myTicket = loadMyTicket()
    tickets.append(myTicket)

    validFields = []
    for c in range(len(myTicket)):
        validFields.append(set(range(len(fields))))

    ticktIndex = 0
    for c in range(len(myTicket)):
        valid = validFields[c]
        for ticket in tickets:
            ticketValue = ticket[c]

            fieldsToRemove = []
            for validField in valid:
                fieldRanges = ranges[validField]
                isValid = False
                for (minR, maxR) in fieldRanges:
                    if minR <= ticketValue and maxR >= ticketValue:
                        isValid = True

                if not isValid:
                    print('{} IS NOT IN  {}'.format(ticketValue, fieldRanges))
                    print('Field {} is not valid for {}'.format(validField, c))
                    fieldsToRemove.append(validField)

            for v in fieldsToRemove:
                valid.remove(v)

                if len(valid) == 0:
                    print('--------ERROR--------')
                    print(valid)
                    print('----------------')
            # have whittled it down to one.  Remove from all others
            if len(valid) == 1:
                validField = valid.pop()
                valid.add(validField)
                print('----------------')
                print(valid)
                print('----------------')
                validFields = cleanupPotentialMatches(
                    validFields, validField, c, myTicket)

                break

    result = 1
    print(validFields)
    for i in range(len(validFields)):
        if len(validFields[i]) != 1:
            print("FAILURE {}: {} ".format(i, validFields[i]))

        fieldNumber = validFields[i].pop()
        fieldName = fields[fieldNumber]
        if fieldName.startswith('departure '):
            print('column: {} is {}'.format(fieldNumber, fieldName))
            result = result * myTicket[i]

    print(result)


if __name__ == "__main__":
    # tryTestData()
    # getInvalidNumbers()
    getDepartureNumbers()
