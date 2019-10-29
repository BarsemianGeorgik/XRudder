from GameBoard import GameBoard
from Player import Player
from MiniMaxNode import MiniMaxNode
from MiniMaxTree import MiniMaxTree

if __name__ == '__main__':

    # Initializations
    turnCounter = 0
    movesActionsRemaining = 30

    #Player  initilization
    p1 = Player("Player 1", "X")
    p2 = Player("Player 2", "O")

    isFirstPlayerTurn = True
    player = " "
    gameBoard = GameBoard()

    player1Win = False
    player2Win = False
    aIEnabeled = False

    while True:
        enablingAI = input(
            "Would you wanna play against an AI? [Y]es or [N]o?").upper()
        if enablingAI not in "YN" or len(enablingAI) != 1:
            print("The entry was not correct please try again")
            continue
        break;

    if enablingAI == 'Y':
        aIEnabeled = True

    print("The Game has Started!")
    gameBoard.printBoard()
    while (not player1Win) & (not player2Win) & ((movesActionsRemaining != 0) & (p1.tokensRemaining != 0) & (p2.tokensRemaining != 0)) :
        turnCounter = turnCounter + 1

        # Choosing the Player's turn
        if isFirstPlayerTurn:
            player = p1
            isFirstPlayerTurn = False
        else:
            player = p2
            isFirstPlayerTurn = True

        #checking if its AI turn if its enabled
        action = 'A'
        player.printPlayerStatus()
        if (player != p2) or (not aIEnabeled):
            # Player action input
            while True:
                if turnCounter <= 2:
                    print(player.name + " Place your first token!")
                    action = 'P'
                elif player.tokensRemaining == 0:
                    print(player.name + " has run out of tokens. You can only move existing tokens.")
                    action = 'M'
                elif movesActionsRemaining == 0 and player.tokensRemaining != 0:
                    print("Players have run out of move actions. You can only put new tokens on the board. ")
                    action = 'P'
                elif movesActionsRemaining == 0 and player.tokensRemaining == 0:
                    print(player.name + " has no remaining tokens or moves. Turn ending.")

                else:
                    action = input(
                        "It's " + player.name + "'s turn! What would you like to do? [P]ut a new token or [M]ove an existing one?").upper()
                if action not in "PM" or len(action) != 1:
                    print("The entry was not correct please try again")
                    continue
                break

        # Action Process

        if action == 'P':
            # implementation for Putting a token
            print("P is a valid move")
            validPutAction = False
            while not validPutAction:
                indexMove = input("Enter the index of your put action (Letter followed by number):").upper()
                validPutAction = gameBoard.putToken(indexMove, player.tokenCharacter)
                if validPutAction:
                    #print("Removing one token from total")
                    player.tokensRemaining = player.tokensRemaining - 1
                    player.printPlayerStatus()


        elif action == 'M':
            # implementation for Moving a token
            print("M is a valid move")
            validMoveAction = False
            while not validMoveAction:
                indexMove = input("Enter the index of your move (Letter followed by number):").upper()
                validMoveAction = gameBoard.moveToken(indexMove, player.tokenCharacter)
                movesActionsRemaining - 1

        elif action == 'A':
            print("AI is calculating it's move")
            miniMaxTree = MiniMaxTree()
            # creating all Ai moves
            # creating all player moves followed by AI
            # give a heuristic to each of those player's move
            # Add player nodes to it's parent AI node
            # Add all AI nodes to the root Node
            # set the root node to the minimaxTree
            # gameBoard = miniMaxTree.getAIComputedMove()

        # Print the Board
        gameBoard.printBoard()

        # Check if a player won
        player1Win = gameBoard.didPlayerTokenWin("X", "O")
        player2Win = gameBoard.didPlayerTokenWin("O", "X")

    if player1Win:
        print("Player 1 won the game")
    elif player2Win:
        print("Player 2 won the game")
    else:
        print("Game Over: End of round")
