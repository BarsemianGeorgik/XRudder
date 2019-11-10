from GameBoard import GameBoard
from Player import Player
from MiniMaxNode import MiniMaxNode
from MiniMaxTree import MiniMaxTree

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
    while (not player1Win) & (not player2Win) & (
            (movesActionsRemaining != 0) & (p1.tokensRemaining != 0) & (p2.tokensRemaining != 0)):
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
                    player.printPlayerStatus()
                    player.printPlayerTokens()
                    gameBoard.possibleMoves(player)


        elif action == 'M':
            # implementation for Moving a token
            print("M is a valid move")
            validMoveAction = False
            while not validMoveAction:
                indexMove = input("Enter the index of your move (Letter followed by number):").upper()
                validMoveAction = gameBoard.moveToken(indexMove, player)
                movesActionsRemaining - 1
                player.printPlayerTokens()

        elif action == 'A':
            print("AI is calculating it's move")
            miniMaxTree = MiniMaxTree()
            AI_moves = []
            AI_nodes = []
            player_moves = []  # list of lists of player moves
            player_nodes = []  #  list of lists of player nodes
            temp = []
            rootnode = MiniMaxNode(gameBoard.board, 0)  # create node of the current gameboard
            miniMaxTree.setRoot(rootnode)  # set as the root node
            AI_moves.extend(gameBoard.allPutOptions(p1))  # calculate all put options for AI
            AI_moves.extend(gameBoard.possibleMoves(p1))  # calculate all move options for AI

            for each in AI_moves:  # make each AI move a node
                AI_nodes.append.MiniMaxNode(each, 0)  # setting heuristic to 0 for all of them,

            for each in AI_moves:  # calculate player moves for each AI move
                moves = each.allPutOptions(p2)
                moves.extend(each.possibleMoves(p2))
                player_moves.append(moves)
                for move in moves:
                    minimaxnode = MiniMaxNode(move, 0)
                    minimaxnode.calculateHeuristic()
                    temp.append.MiniMaxNode(move, 0)  # make playernode
                    #  call heuristic function on the playermoves when created (can make it in the node class itself)
                player_nodes.append(temp)
                moves = []  # clear player move array
                temp = []
            i = 0
            #  iterate through
            for each in AI_nodes:
                each.setChildren(player_nodes[i])
                i = i + 1
            rootnode.setChildren(AI_nodes)
            gameBoard = miniMaxTree.getAIComputedMove()
            # creating all AI moves
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
