class Player:
    def __init__(self, name, tokenCharacter):
        self.name = name
        self.tokenCharacter = tokenCharacter
        self.tokensRemaining = 15
        self.playerTokenLocations = []

    def printPlayerStatus(self):
        print(self.name + " has " + str(self.tokensRemaining) + " tokens remaining to put.")

    def printPlayerTokens(self):
        print(self.playerTokenLocations)
