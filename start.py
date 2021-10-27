# file for Exam 2
numberMisplaced(code) #heuristic
goalcheck(code)
changeDigit(code, index)

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

addSuccessor(currentNode, fringe)

def start(input):
	startNode = {
		"code": input,
		"depth": 0,
<<<<<<< Updated upstream
		"plan": []
=======
		"plan": [input], #a list of past codes
		"parent": None
>>>>>>> Stashed changes
	}

	endNode = search(startNode)

	if endNode:
		for code in endNode["plan"]:
			print(code)
	else:
		print("No Solution Found")

start([0, 1, 2, 0])