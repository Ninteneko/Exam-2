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

def start():
	startNode = {
		"code": [0, 1, 2, 0],
		"depth": 0,
		"plan": [] #a list of indices to update
		"parent": None
	}

	goalCode = [1, 2, 1, 2]

	endNode = search(startNode, goalCode)

	if endNode:
		print("Plan: ", endNode['plan'])
	else:
		print("No Solution Found")
