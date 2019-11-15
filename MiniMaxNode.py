class MiniMaxNode:
    def __init__(self, board):
        #"constructor to initiate this object"
        # store board
        self.board = board
        # minimax value
        self.value = -5
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

    def heuristic(self):
        # for the heuristic to work we need to really need to maximize the difference of the opponent
        # we don't actually
        #print("hi")
        val = 0
        # how close self is to creating an x
        for x in range(1, 9):
            for y in range(1, 11):
                if 'O' == self.board[x][y]:
                    if ('X' == self.board[x][y-1]) and ('X' == self.board[x][y+1]):
                       # print("x formation was blocked at ", x, ",", y)
                        val = val - 1
                    if 'X' == self.board[x - 1][y - 1] or 'X' == self.board[x + 1][y + 1] \
                            or 'X' == self.board[x - 1][y + 1] or 'X' == self.board[x + 1][y - 1]:
                        val = val - 1
                    else:
                      #  print("Found middle of an x")
                        val = val + 1
                        if 'O' == self.board[x - 1][y - 1]:  # top left
                            val = val + 1
                        if 'O' == self.board[x + 1][y + 1]:  # bottom right
                            val = val + 1
                        if 'O' == self.board[x - 1][y + 1]:  # top right
                            val = val + 1
                        if 'O' == self.board[x + 1][y - 1]:  # bottom left
                            val = val + 1
        for x in range(1, 9):
            for y in range(1, 11):
                if 'X' == self.board[x][y]:
                    if ('O' == self.board[x][y-1]) and ('O' == self.board[x][y+1]):
                        val = val + 1
                    if 'O' == self.board[x - 1][y - 1] or 'O' == self.board[x + 1][y + 1] \
                            or 'O' == self.board[x - 1][y + 1] or 'O' == self.board[x + 1][y - 1]:
                        val = val + 1
                    else:
                       # print("Found middle of an x")
                        val = val - 1
                        if 'X' == self.board[x - 1][y - 1]:  # top left
                            val = val - 1
                        if 'X' == self.board[x + 1][y + 1]:  # bottom right
                            val = val - 1
                        if 'X' == self.board[x - 1][y + 1]:  # top right
                            val = val - 1
                        if 'X' == self.board[x + 1][y - 1]:  # bottom left
                            val = val - 1
        self.value = val - 2
        return val - 2
        # how close opponent is to creating an x



#  Naive heuristic
#  heuristic value starts at 5, take away 1 the closer it gets to creating an x
#  looks at all the tokens as the center of the x, checks the opponents tokens aren't in the way
#  or that it's been blocked
#  can change the X/Os to be passed tokens
    def calculateHeuristic(self):
        val = 0;
        tempval = 0;
        for x in range(1, 9):
            for y in range(1, 11):
                if 'O' == self.board[x][y]:
                    if ('X' == self.board[x][y-1]) and ('X' == self.board[x][y+1]):
                        print("x formation was blocked at ", x, ",", y)
                        val = val + 1
                    if 'X' == self.board[x - 1][y - 1] or 'X' == self.board[x + 1][y + 1] \
                            or 'O' == self.board[x - 1][y + 1] or 'O' == self.board[x + 1][y - 1]:
                        print("x formation has been blocked here")
                        val = val + 1
                    else:
                        print("Found middle of an x")
                        tempval = tempval - 1
                        if 'O' == self.board[x - 1][y - 1]:  # top left
                            tempval = tempval - 1
                        if 'O' == self.board[x + 1][y + 1]:  # bottom right
                            tempval = tempval - 1
                        if 'O' == self.board[x - 1][y + 1]:  # top right
                            tempval = tempval - 1
                        if 'O' == self.board[x + 1][y - 1]:  # bottom left
                            tempval = tempval - 1
                        #if tempval > val:  # see if somewhere else it's closer to making an x
                        #val = tempval

                        #tempval = 0  # return tempval to 5
        value = tempval  # changes node value
        return tempval

