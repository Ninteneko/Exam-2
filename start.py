# file for Exam 2

goal = [1,2,1,2]

def changeDigit(code,index):
	newCode = []
	for i in range(len(code)):
		if i == index:
			newCode.append((code[i]+1)%3)
		else:
			newCode.append(code[i])
	return newCode

def numberMisplaced(code):
	counter = 0
	for i in range(len(code)):
		if code[i] != goal[i]:
			counter+=1
	return counter

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
		print("plan:")
		for code in endNode["plan"]:
			print(code)
		print("\nlength: ")
		print(len(endNode["plan"]))
	else:
		print("No Solution Found")

start([0, 1, 2, 0]) 
