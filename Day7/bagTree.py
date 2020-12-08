

def getRuleName(rule):
    adj, color, _ = rule.strip().split(' ')
    return '{} {}'.format(adj, color)


def generateNode(rule):
    pRule, cRules = list(map(lambda x: x.strip(), rule.split('contain')))
    parent = getRuleName(pRule)

    cList = cRules.split(', ')
    children = []
    for c in cList:
        if c != 'no other bags.':
            count, adj, color, _ = c.strip().split(' ')
            count = int(count)
            id = '{} {}'.format(adj, color)
            children.extend([id] * count)

    return parent, children


def readFile(path='./Day7/input.txt'):
    f = open(path, 'r')
    nodes = {}
    for l in f:
        parent, children = generateNode(l)
        nodes[parent] = children

    return nodes


def findBags(id='shiny gold'):
    nodes = readFile()
    positive = set([])
    visited = set([])

    for node in nodes:
        dfs(node, nodes, id, positive, visited)

    return len(positive) - 1  # shiny gold bag don't count :(


def dfs(node, nodes, id, positive, visited):
    if node in positive:
        return True
    if node in visited:
        return False

    visited.add(node)
    if node == id:
        positive.add(node)
        return True

    children = nodes[node]
    for c in children:
        found = dfs(c, nodes, id, positive, visited)
        if found:
            positive.add(node)
            return True

    return False


def countTree(id='shiny gold'):
    nodes = readFile()
    visited = {}

    return getNodeCount(id, nodes, visited) - 1


def getNodeCount(id, nodes, visited):
    if id in visited:
        return visited[id]

    children = nodes[id]

    count = 1
    for c in children:
        count += getNodeCount(c, nodes, visited)

    visited[id] = count
    return visited[id]


if __name__ == "__main__":
    # print(findBags())
    print(countTree())
