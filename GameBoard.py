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
        alphabetAxis = ['\t', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M']
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


    def putToken(self, args):
        self.stringToIndex(args)
        if self.board[self.x_val][self.y_val] == '□':
            print("Placing the token")
            self.board[self.x_val][self.y_val] = 'X'
            self.printBoard()
            return True

        if self.board[self.x_val][self.y_val] != '□':
            print("That location is already taken")
            return False

        # Check if available
        # If assigned, ask to enter again
        # If available, assign index to player token

    def moveToken(self):
        print("Moving the token")
        # Check if token exists at location and is assigned to player
        # If not, ask to enter again
        # Ask the position they'd like to move to
        # call putToken function


    def stringToIndex(self, input):
        # check if within a to m, and 1 to 10
        input.replace(" ", "")
        if len(input) > 3 or input[0].upper() not in "ABCDEFGHIJK" or int(input[1:]) > 10:
            print("That is an invalid input")
        else:
            self.y_val = (ord(input[0].lower()) - 97)  # -97 to get the index.. a-97 = 0, etc.
            self.x_val = int(input[1:]) - 1

            print(self.x_val, self.y_val )
