from GameBoard import GameBoard
from Player import Player
from MiniMaxNode import MiniMaxNode
from MiniMaxTree import MiniMaxTree
import copy

if __name__ == '__main__':

    # Initializations
    turnCounter = 0
    movesActionsRemaining = 30

    # Player  initialization
    p1 = Player("Player 1", "X")
    p2 = Player("Player 2", "O")

    isFirstPlayerTurn = True
    player = " "
    gameBoard = GameBoard()

    player1Win = False
    player2Win = False
    aIEnabled = False

    while True:
        enablingAI = input(
            "Would you wanna play against an AI? [Y]es or [N]o?").upper()
        if enablingAI not in "YN" or len(enablingAI) != 1:
            print("The entry was not correct please try again")
            continue
        break;

    if enablingAI == 'Y':
        aIEnabled = True

    print("The Game has Started!")
    gameBoard.printBoard()

    moveOrPutRemain = True

    while (not player1Win) and (not player2Win) and moveOrPutRemain:
        turnCounter = turnCounter + 1

        # Choosing the Player's turn
        if isFirstPlayerTurn:
            player = p1
            isFirstPlayerTurn = False
        else:
            player = p2
            isFirstPlayerTurn = True

        # checking if its AI turn if its enabled
        action = 'A'
        player.printPlayerStatus()
        if (player != p2) or (not aIEnabled):
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
                validPutAction = gameBoard.putToken(indexMove, player)
                if validPutAction:
                    # print("Removing one token from total")
                    player.tokensRemaining = player.tokensRemaining - 1




        elif action == 'M':
            # implementation for Moving a token
            print("M is a valid move")
            validMoveAction = False
            while not validMoveAction:
                indexMove = input("Enter the index of your move (Letter followed by number):").upper()
                validMoveAction = gameBoard.moveToken(indexMove, player)
                movesActionsRemaining = movesActionsRemaining - 1
                player.printPlayerTokens()

        elif action == 'A':

            beforeAITokenSize = len(gameBoard.getAITokens(p2))

            print("AI is calculating it's move")
            miniMaxTree = MiniMaxTree()
            AI_moves = []   #array of AI intial moves
            AI_nodes = []   #array of AI move nodes
            player_moves = []  # list of lists of player moves
            player_nodes = []  # list of lists of player nodes
            temp = []

            rootnode = MiniMaxNode(gameBoard.board)  # create node of the current gameboard
            miniMaxTree.setRoot(rootnode)  # set as the root node

            # ******
            # Only calculate puts if AI still has tokens left ****
            # ******
            AI_moves.extend(gameBoard.allPutOptions(p2))  # calculate all put options for AI

            # if ai has moves left, calculate possible moves
            if movesActionsRemaining > 0 and len(p2.playerTokenLocations) != 0:
                AI_moves.extend(gameBoard.possibleMoves(p2))  # calculate all move options for AI

            for each in AI_moves:  # make each AI move a node
                AI_nodes.append(MiniMaxNode(each.board))  # setting heuristic to 0 for all of them

            for each in AI_moves:  # calculate player moves for each AI move
                moves = []
                if p1.tokensRemaining > 0:
                  moves = each.allPutOptions(p1)

                if movesActionsRemaining > 0 and len(p1.playerTokenLocations) != 0:
                    moves.extend(each.possibleMoves(p1))
                # ELSEIF player can't do anything return original game board? cause they can't move..
                player_moves.append(moves)
                for move in moves:
                    minimaxnode = MiniMaxNode(move.board)  # create player nodes

                    # find out which token the AI has
                    # 
                    minimaxnode.finalheuristic('O', 'X')  # call heuristic function on leaf nodes
                    temp.append(copy.deepcopy(minimaxnode))  # add to array of player nodes for specific AI move

                player_nodes.append(temp)
                moves = []  # clear player move array
                temp = []
            i = 0
            #  iterate through
            for each in AI_nodes:
                each.setChildren(player_nodes[i])
                i = i + 1
            rootnode.setChildren(AI_nodes)
            miniMaxTree.computeMiniMax()

            gameBoard.board = miniMaxTree.getAIComputedMove()

            afterAITokenSize = len(gameBoard.getAITokens(p2))

            # Checking if the AI has chosen to play a token or move a token
            if beforeAITokenSize < afterAITokenSize:
                p2.tokensRemaining = p2.tokensRemaining - 1

            elif beforeAITokenSize == afterAITokenSize:
                movesActionsRemaining = movesActionsRemaining - 1



        # Print the Board
        gameBoard.printBoard()
        player.printPlayerStatus()
        player.printPlayerTokens()

        print("Moves remaining: " + str(movesActionsRemaining))

        # Check if a player won
        player1Win = gameBoard.didPlayerTokenWin("X", "O")
        player2Win = gameBoard.didPlayerTokenWin("O", "X")

        moveOrPutRemain = (movesActionsRemaining > 0) or (p1.tokensRemaining > 0) or (p2.tokensRemaining > 0)

    if player1Win:
        print("Player 1 won the game")
    elif player2Win:
        print("Player 2 won the game")
    else:
        print("Game Over: End of round")
