import copy


def printTempBoard(boardList):
    alphabetAxis = ['\t', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    print("============= GAME STATUS ============= ")
    rowNumber = 10
    for row in boardList:
        print(str(rowNumber), end='\t ')
        for elem in row:
            print(elem, end=' ')
        rowNumber = rowNumber - 1
        print()

    for x in alphabetAxis:
        print(x, end=' ')
    print()
    print()


def allPutOptions(player, board):
    boards = []
    tempboard = copy.deepcopy(board)

    for (i, row) in enumerate(board):
        for (j, value) in enumerate(row):
            if value == ".":
                print("I HERE HERE HERE HERE HERE AS MANY TIMES AS I AM MAKING A NEW BOARD FOR MY OPTIONS ")
                value = player.tokenCharacter
                tempboard[i][j] = player.tokenCharacter
                boards.append(copy.deepcopy(tempboard))  # create new board of the temporary one
                tempboard[i][j] = "."
                # print(i, j, value)
    for x in boards:
        printTempBoard(x)

    return boards


def spaghettistringToIndex(userInput):
    # check if within a to m, and 1 to 10
    userInput.replace(" ", "")
    if len(userInput) > 3 or userInput[0].upper() not in "ABCDEFGHIJKL" or int(userInput[1:]) > 10:
        print("That is an invalid input")
        return False
    else:
        y = (ord(userInput[0].lower()) - 97)  # -97 to get the index.. a-97 = 0, etc.
        x = 10 - int(userInput[1:])

        coordinate = str(y) + str(x)
        # print("valid index")
        # print(self.x_val, self.y_val)
        return coordinate


def possibleMoves(player, board):
    boards = []  # possible boards
    #   function that calculates the possible moves of a player
    #   takes list of player indexes, for every index make a list of boards
    for index in player.playerTokenLocations:
        indexof = spaghettistringToIndex(index)
        prevX = int(indexof[0])
        prevY = int(indexof[1])

        possibleIndex = []  # possible indexes of the new locations from given index

        boardIndex = 0
        # Add a new board to the list
        newBoard = copy.deepcopy(board)
        for x in range(-1, 2):
            for y in range(-1, 2):
                newX = chr(ord(index[0]) + x)
                newY = str(int(index[1:]) + y)  # done this way to handle index 10
                if newX in "ABCDEFGHIJKL" and 0 < int(newY) <= 10:
                    newXY = newX + newY

                    # check if this place is occupied
                    valid = spaghettistringToIndex(newXY)
                    newX = int(indexof[0])
                    newY = int(indexof[1])
                    if valid:
                        if board[newX][newY] == '.':
                            possibleIndex.append(newXY)

                            newBoard[newX][newY] = player.tokenCharacter
                            newBoard[prevX][prevY] = '.'

                            boards.append(copy.deepcopy(newBoard))

                            newBoard[newX][newY] = '.'

                            print("This is board #" + str(boardIndex))
                            printTempBoard(boards[boardIndex])
                            boardIndex = boardIndex + 1

        print(possibleIndex)
        print("THESE ARE MY BOARDS")
        for each in boards:
            print(each)

    return boards


class GameBoard:

    def __init__(self):
        self.board = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ], ]

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
                                | ((adversaryToken != self.board[x][j - 1]) & (
                                        adversaryToken == self.board[x][j + 1]))):
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
        print()

    def putToken(self, args, player):
        # Check if available
        # If assigned, ask to enter again
        # If available, assign index to player token
        valid = self.stringToIndex(args)
        if valid:
            if self.board[self.x_val][self.y_val] == '.':
                print("Placing the token")
                self.board[self.x_val][self.y_val] = player.tokenCharacter
                player.playerTokenLocations.append(args)
                return True

            else:
                print("Invalid location")
                return False
        else:
            return False

    def moveToken(self, args, player):
        # Check if valid input
        valid = self.stringToIndex(args)
        if valid:
            # check if token exists
            if self.board[self.x_val][self.y_val] == player.tokenCharacter:
                prevX = self.x_val
                prevY = self.y_val

                validPutAction = False
                validOneSpace = False
                while not validPutAction and not validOneSpace:
                    indexMove = input(
                        "Enter the index which you'd like to move to (Letter followed by number):").upper()

                    self.stringToIndex(indexMove)
                    # Check if the move is of only one space
                    x_delta = self.x_val - prevX
                    # print(str(x_delta) + " x difference")
                    y_delta = self.y_val - prevY
                    #  print(str(y_delta) + " y difference")

                    if -1 <= x_delta <= 1 and -1 <= y_delta <= 1:
                        validOneSpace = True
                        print("That's a valid one space move")

                        if validOneSpace:
                            validPutAction = self.putToken(indexMove, player)

                    elif not validOneSpace:
                        print("That is not a valid one space move. Try again. ")
                if validPutAction:
                    self.board[prevX][prevY] = '.'
                    print("Moving the token")
                    print(args.upper() + " is being removed from the player's list.")
                    player.playerTokenLocations.remove(args.upper())
                    return True

            elif self.board[self.x_val][self.y_val] != player.tokenCharacter:
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
            # print("valid index")
            # print(self.x_val, self.y_val)
            return True

    # return new boards for the put option
