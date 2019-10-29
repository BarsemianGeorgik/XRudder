class MiniMaxNode:
    def __init__(self, board, miniMaxVal):
        #"constructor to initiate this object"
        # store board
        self.board = board
        # minimax value
        self.value = miniMaxVal
        # child to null
        self.children = None

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
