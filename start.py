# file for Exam 2
forbidden = [
    [0,0,0,0],
    [1,1,1,1],
    [2,2,2,2]
]

goal = [1,2,1,2]
code = [1,2,1,0]

numberMisplaced(code) #heuristic
changeDigit(code, index)

def goalcheck(code):
    for i in range(len(code)):
        if code[i] != goal[i]:
            return False
    return True


def sortFringe(fringe):
	fringe.sort(key=lambda item: (item["depth"] + numberMisplaced(item['code'])))

def search(startNode):
	endNode = None
	fringe = [startNode]
	visited = []

	while fringe and not endNode:
		sortFringe(fringe)
		currentNode = fringe.pop(0)

		if currentNode['code'] in visited:
			continue
		visited.append(currentNode['code'])

		if goalcheck(currentNode['code']):
			endNode = currentNode
		else:
			addSuccessor(currentNode, fringe)

	return endNode

addSuccessor(currentNode, fringe) #Note how a node is defined in start()

def addSuccessor(currentNode, fringe):
	forbiddenCodes = [
		[0, 0, 0, 0],
		[1, 1, 1, 1],
		[2, 2, 2, 2]
	]
	for index in range(4):
		newCode = changeDigit(currentNode["code"], index)
		if not newCode in forbiddenCodes:
			newNode = {
				"code": newCode ,
				"depth": currentNode["depth"] + 1,
				"plan": currentNode["plan"] + [newCode],
				"parent": currentNode
			}
			fringe.append(newNode)

def start(input):
	startNode = {
		"code": input,
		"depth": 0,
		"plan": [input], #a list of past codes
		"parent": None
	}

	endNode = search(startNode)

	if endNode:
		for code in endNode["plan"]:
			print(code)
	else:
		print("No Solution Found")

start([0, 1, 2, 0])