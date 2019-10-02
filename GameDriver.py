from GameBoard import GameBoard

if __name__ == '__main__':

    # Initializations
    roundCounter = 0
    isFirstPlayerTurn = True
    player = " "
    gameBoard = GameBoard()

    print("The Game has Started!")
    gameBoard.printBoard()

    while True:
        roundCounter = roundCounter + 1
        print("Round: " + str(roundCounter))

        # Choosing the Player's turn
        if isFirstPlayerTurn:
            player = "Player 1"
            playerToken = "X"
            isFirstPlayerTurn = False
        else:
            player = "Player 2"
            playerToken = "O"
            isFirstPlayerTurn = True

        # Player action input
        while True:
            action = input(
                "It's " + player + "'s turn! What would you like to do? [P]ut a new token or [M]ove an existing one?").upper()
            if action not in "PM" or len(action) != 1:
                print("The entry was not correct please try again")
                continue
            break

        # Action Process

        if action == 'P':
            # implementation for putting a token
            print("P is a valid move")
            validPutAction = False
            while not validPutAction:
                indexMove = input("Enter the index of your put action (Letter followed by number):").upper()
                validPutAction = gameBoard.putToken(indexMove, playerToken)


        elif action == 'M':
            # implementation for Moving a token
            print("M is a valid move")
            validMoveAction = False
            while not validMoveAction:
                indexMove = input("Enter the index of your move (Letter followed by number):").upper()
                validMoveAction = gameBoard.moveToken(indexMove, playerToken)

        # Print the Board
        gameBoard.printBoard()

        # Check if a player won
