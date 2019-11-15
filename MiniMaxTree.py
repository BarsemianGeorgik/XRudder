import sys

from MiniMaxNode import MiniMaxNode


class MiniMaxTree:

    def __init__(self):
        self.root = None

    def setRoot(self, root):
        self.root = root

    def getRootValue(self):
        return self.root.getHeuristicValue()

    def getAIComputedMove(self):
        return self.root.getGameBoard()

    def computeMiniMax(self):
        maxChildList = self.root.getChildren()  # AI's possible moves
        maxValue = -sys.maxsize - 1  # -infinity

        for maxNode in maxChildList:
            minChildList = maxNode.getChildren()  # Player's possible moves
            minValue = sys.maxsize  # +infinity
            for minNode in minChildList:
                print("leaf node value: ", minNode.heuristic())  # setting leafs values
                if minNode.getHeuristicValue() < minValue:
                    maxNode.setHeuristicValue(minNode.getHeuristicValue())  # changes the parents heuristic value
                    minValue = minNode.getHeuristicValue()
                    #print("setting the min value to :", maxValue)
            if maxNode.getHeuristicValue() > maxValue:
                self.root.setGameBoard(maxNode.getGameBoard())  # changes the root gameboard to be the best move so far
                self.root.setHeuristicValue(maxNode.getHeuristicValue())  # sets the roots heuristic value to be the best it can do
                maxValue = maxNode.getHeuristicValue()
                #print("setting the max value to :", maxValue)
