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
        self.stringToIndex(args)
        if self.board[self.x_val][self.y_val] == '□':
            print("Placing the token")
            self.board[self.x_val][self.y_val] = playerToken
            self.printBoard()
            return True

        if self.board[self.x_val][self.y_val] != '□':
            print("That location is already taken")
            return False

    def moveToken(self, args, playerToken):
        print("Moving the token")
        # Check if token exists at location and is assigned to player
        self.stringToIndex(args)
        if self.board[self.x_val][self.y_val] == playerToken:
            prevX = self.x_val
            prevY = self.y_val
            indexMove = input("Enter the index which you'd like to move to (Letter followed by number):").upper()

            while self.putToken(indexMove, playerToken) == False:
                indexMove = input("Enter the index which you'd like to move to (Letter followed by number):").upper()
                self.putToken(indexMove, playerToken)
            print(prevX)
            print(prevY)
            self.board[prevX][prevY] = '□'

            return True

        if self.board[self.x_val][self.y_val] != playerToken:
            print("That field does not contain your token. Please try again")
            return False
        # If not, ask to enter again
        # Ask the position they'd like to move to
        # call putToken function

    def stringToIndex(self, input):
        # check if within a to m, and 1 to 10
        input.replace(" ", "")
        if len(input) > 3 or input[0].upper() not in "ABCDEFGHIJKL" or int(input[1:]) > 10:
            print("That is an invalid input")
        else:
            self.y_val = (ord(input[0].lower()) - 97)  # -97 to get the index.. a-97 = 0, etc.
            self.x_val = 10 - int(input[1:])

            print(self.x_val, self.y_val)
