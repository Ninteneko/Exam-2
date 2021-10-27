# file for Exam 2
forbidden = [
    [0,0,0,0],
    [1,1,1,1],
    [2,2,2,2]
]

goal = [1,2,1,2]
code = [1,2,1,0]

#numberMisplaced(code) #heuristic
def goalcheck(code):
    for i in range(len(code)):
        if code[i] != goal[i]:
            return False
    return True

#changeDigit(code, index)
#sortFringe(fringe)
#search(startNode)
#addSuccessor(currentNode, fringe)
#start()
