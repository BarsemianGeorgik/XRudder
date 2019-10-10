class Player:
    def __init__(self, name, tokenCharacter):
        self.name = name
        self.tokenCharacter = tokenCharacter
        self.tokensRemaining = 15

    def printPlayerStatus(self):
        print(self.name + " has " + str(self.tokensRemaining) + " tokens remaining to put.")
