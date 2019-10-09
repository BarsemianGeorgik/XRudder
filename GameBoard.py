class GameBoard:

    def __init__(self):
        self.board = [['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ],
                      ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', ], ]

        self.x_val = 0
        self.y_val = 0

    def didPlayerTokenWin(self, playerToken, adversaryToken):
        gameOver = False
        for x in range(1, 9):
            for j in range(1, 11):
                if playerToken == self.board[x][j]:
                    # check top left , top right, bottom left and bottom right
                    if ((playerToken == self.board[x - 1][j - 1]) & (playerToken == self.board[x - 1][j + 1])
                            & (playerToken == self.board[x + 1][j - 1]) & (playerToken == self.board[x + 1][j + 1])):
                        # Check if opponent has blocked the player X
                        if (((adversaryToken != self.board[x][j - 1]) & (adversaryToken != self.board[x][j + 1]))
                                | ((adversaryToken == self.board[x][j - 1]) & (adversaryToken != self.board[x][j + 1]))
                                | ((adversaryToken != self.board[x][j - 1]) & (adversaryToken == self.board[x][j + 1]))):
                            gameOver = True
        return gameOver

    def printBoard(self):
        alphabetAxis = ['\t', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        print("============= GAME STATUS ============= ")
        rowNumber = 10
        for row in self.board:
            print(str(rowNumber), end='\t ')
            for elem in row:
                print(elem, end=' ')
            rowNumber = rowNumber - 1
            print()

        for x in alphabetAxis:
            print(x, end=' ')
        print()

    def putToken(self, args, playerToken):
        # Check if available
        # If assigned, ask to enter again
        # If available, assign index to player token
        valid = self.stringToIndex(args)
        if valid:
            if self.board[self.x_val][self.y_val] == '□':
                print("Placing the token")
                self.board[self.x_val][self.y_val] = playerToken
                return True

            else:
                print("Invalid location")
                return False
        else:
            return False

    def moveToken(self, args, playerToken):
        print("Moving the token")
        # Check if valid input
        valid = self.stringToIndex(args)
        if valid:
            # check if token exists
            if self.board[self.x_val][self.y_val] == playerToken:
                prevX = self.x_val
                prevY = self.y_val

                validPutAction = False
                while not validPutAction:
                    indexMove = input(
                        "Enter the index which you'd like to move to (Letter followed by number):").upper()
                    validPutAction = self.putToken(indexMove, playerToken)
                print("previous slots: " + str(prevX) + " " + str(prevY))
                self.board[prevX][prevY] = '□'
                return True

            elif self.board[self.x_val][self.y_val] != playerToken:
                print("That field does not contain your token. Please try again")
                return False
        else:
            return False

    def stringToIndex(self, userInput):
        # check if within a to m, and 1 to 10
        userInput.replace(" ", "")
        if len(userInput) > 3 or userInput[0].upper() not in "ABCDEFGHIJKL" or int(userInput[1:]) > 10:
            print("That is an invalid input")
            return False
        else:
            self.y_val = (ord(userInput[0].lower()) - 97)  # -97 to get the index.. a-97 = 0, etc.
            self.x_val = 10 - int(userInput[1:])
            print("valid index")
            print(self.x_val, self.y_val)
            return True
