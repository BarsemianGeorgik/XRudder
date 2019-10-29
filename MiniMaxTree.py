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
        maxChildList = self.root.getChildren()
        maxValue = -sys.maxsize - 1

        for maxNode in maxChildList:
            minChildList = maxNode.getChildren()
            minValue = sys.maxsize
            for minNode in minChildList:
                if minNode.getHeuristicValue() < minValue:
                    maxNode.setHeuristicValue(minNode.getHeuristicValue())
                    minValue = minNode.getHeuristicValue()
            if maxNode.getHeuristicValue() > maxValue:
                self.root.setGameBoard(maxNode.getGameBoard())
                self.root.setHeuristicValue(maxNode.getHeuristicValue())
                maxValue = maxNode.getHeuristicValue()