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

    def closetox(self, token, opptoken, x, y):
        value = 0
        #  checks if opponents token is blocking the creation of an x at this point
        if opptoken == self.board[x - 1][y - 1] or opptoken == self.board[x + 1][y + 1] \
                or opptoken == self.board[x - 1][y + 1] or opptoken == self.board[x + 1][y - 1]:
            return 0
        if (opptoken == self.board[x][y - 1]) and (opptoken == self.board[x][y + 1]):  # check if x creation has been blocked
            return 0
        else:
            if token == self.board[x][y]:  # center
                value = value + 1
            if token == self.board[x - 1][y - 1]:  # top left
                value = value + 1
            if token == self.board[x + 1][y + 1]:  # bottom right
                value = value + 1
            if token == self.board[x - 1][y + 1]:  # top right
                value = value + 1
            if token == self.board[x + 1][y - 1]:  # bottom left
                value = value + 1
            return value

    def newheuristic(self, token, opptoken):
        # how close it is to finishing an x anywhere.. even with spaces in the middle
        opponent = 0  # opponents total value
        art = 0  # ai's total value
        total = 0  # art - opponent
        temp = 0
        for x in range(1, 9):
            for y in range(1, 11):
                if token == self.board[x][y] or '.' == self.board[x][y]:
                    temp = self.closetox(token, opptoken, x, y)
                    if temp > art:
                        art = temp
                if opptoken == self.board[x][y] or '.' == self.board[x][y]:
                    temp = self.closetox(opptoken, token, x, y)
                    if temp > opponent:
                        opponent = temp

        total = art - opponent
        self.value = total
        return total



