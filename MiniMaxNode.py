class MiniMaxNode:
    def __init__(self, board):
        #"constructor to initiate this object"
        # store board
        self.board = board
        # minimax value
        self.value = 0
        # child to null
        self.children = None
        # identifies if either move or put
        self.type = ""


    def getHeuristicValue(self):
       # "method to compare the value with the node data"
        return self.value

    def setHeuristicValue(self, value):
        self.value = value

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def getGameBoard(self):
        return self.board

    def setGameBoard(self, board):
        self.board = board

#  Naive heuristic
#  heuristic value starts at 5, take away 1 the closer it gets to creating an x
#  looks at all the tokens as the center of the x, checks the opponents tokens aren't in the way
#  or that it's been blocked
#  can change the X/Os to be passed tokens
    def calculateHeuristic(self):
        val = 5;
        tempval = 5;
        for x in range(1, 9):
            for y in range(1, 11):
                if 'X' == self.board[x][y]:
                    if ('O' == self.board[x][y-1]) and ('O' == self.board[x][y+1]):
                        print("x formation was blocked at ", x, ",", y)
                    if 'O' == self.board[x - 1][y - 1] or 'O' == self.board[x + 1][y + 1] \
                            or 'O' == self.board[x - 1][y + 1] or 'O' == self.board[x + 1][y - 1]:
                        print("x formation has been blocked here")
                    else:
                        print("Found middle of an x")
                        tempval = tempval - 1
                        if 'X' == self.board[x - 1][y - 1]:  # top left
                            tempval = tempval - 1
                        if 'X' == self.board[x + 1][y + 1]:  # bottom right
                            tempval = tempval - 1
                        if 'X' == self.board[x - 1][y + 1]:  # top right
                            tempval = tempval - 1
                        if 'X' == self.board[x + 1][y - 1]:  # bottom left
                            tempval = tempval - 1
                        if tempval < val:  # see if somewhere else it's closer to making an x
                            val = tempval

                        tempval = 5  # return tempval to 5
        value = val  # changes node value

