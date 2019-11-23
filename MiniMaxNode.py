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

    def finalheuristic(self, token, opptoken,opponent, art):
        previoushigh = -300
        total = 0
        for x in range(1, 9):
            for y in range(1, 11):
                value = 0
                temp = 0
                #  this is where we can block opponent building their their x in using a square first
                #  checks to make sure that it's not us building our x
                # makes x start blocking at 3
                if token == self.board[x][y] and not (
                        token == self.board[x - 1][y - 1] or token == self.board[x + 1][y + 1] or token ==
                        self.board[x - 1][y + 1] or token == self.board[x + 1][y - 1]):
                    if opptoken == self.board[x - 1][y - 1]:
                        temp -= 1
                    if opptoken == self.board[x + 1][y + 1]:
                        temp -= 1
                    if opptoken == self.board[x - 1][y + 1]:
                        temp -= 1
                    if opptoken == self.board[x + 1][y - 1]:
                        temp -= 1
                    if temp <= -3:
                        value += 6
                    if temp <= -4:
                        value += 3
                total += value
                # checks if opponent is building an x with a center already
                if opptoken == self.board[x][y]:
                    if opptoken == self.board[x][y]:  # center
                        temp -= 1
                    if opptoken == self.board[x - 1][y - 1]:  # top left
                        temp -= 1
                    if opptoken == self.board[x + 1][y + 1]:  # bottom right
                        temp -= 1
                    if opptoken == self.board[x - 1][y + 1]:  # top right
                        temp -= 1
                    if opptoken == self.board[x + 1][y - 1]:  # bottom left
                        temp -= 1
                    # value = value + temp
                    if temp <= -3 and (token == self.board[x - 1][y - 1]
                                       or token == self.board[x + 1][y + 1] \
                                       or token == self.board[x - 1][y + 1] or token == self.board[x + 1][y - 1]):
                        value += 9
                    if temp <= -4 and (token == self.board[x - 1][y - 1]
                                       or token == self.board[x + 1][y + 1] \
                                       or token == self.board[x - 1][y + 1] or token == self.board[x + 1][y - 1]):
                        value += 7
                total = total + value
                value = 0
                #  allows us to build our x, checking to make sure no opptoken is blocking our way
                # create a function instead that is called when the puts have run out
                # I need to add the last ai's token to the diamond somehow (SPECIAL CASE SCENARIO)
                #if art.tokensRemaining <= 1 and opponent.tokensRemaining <= 0:
                if (token == self.board[x][y] or token == '.') and not (
                        opptoken == self.board[x - 1][y - 1] or opptoken == self.board[x + 1][y + 1] \
                        or opptoken == self.board[x - 1][y + 1] or opptoken == self.board[x + 1][y - 1]):
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
                        if value > previoushigh:
                            previoushigh = value
                            if value == 5:
                                total += 100
                #  we gonna make a diamond
                # elif (token == self.board[x][y]) and not (opptoken == self.board[x - 1][y - 1] or opptoken == self.board[x][y - 1] or opptoken == self.board[x][y + 1] or opptoken == self.board[x + 1][y] or opptoken == self.board[x - 1][y] or opptoken == self.board[x + 1][y + 1] or opptoken == self.board[x - 1][y + 1] or opptoken == self.board[x + 1][y - 1]):
                #     if token == self.board[x][y]:
                #         value = value + 2
                #     if token == self.board[x][y+1]:
                #         value = value + 2
                #     if token == self.board[x][y-1]:
                #         value = value + 2
                #     if token == self.board[x-1][y]:
                #         value = value + 2
                #     if token == self.board[x+1][y]:
                #         value = value + 2
                #     if value > previoushigh:
                #         previoushigh = value
                #         if value == 5:
                #             total += 100  # may want to take this line out ..
        total = total + previoushigh
        self.value = total
        return total
