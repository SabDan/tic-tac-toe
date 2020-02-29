print('-------------------------------')
print('        TIC TAC TOE            ')
print('-------------------------------')


# choose the players
# create the board
# choose an initial player
# until someone wins, check for winner
# show the board
# choose location, mark it
# toggle active player - their turn
# game over, active player won!

def main():
    # Board Created
    # Board is a list of rows
    # Board is a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # Chose Initial Player
    active_player_index = 0  # switches between 0 and 1
    players = ["Danielle", "Ai"]
    players_symbols = ["O", "X"]
    player = players[active_player_index]

    # Until someone wins
    while not find_winner(board):
        # show board
        player = players[active_player_index]
        player_symbols = players_symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, player_symbols):
            print("That isn't an option, try again")
            continue
        # input('paused')

        # Toggle Active Player
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)


def choose_location(board, players_symbols):
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))

    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = players_symbols
    return True


def show_board(board):
    for row in board:
        print(" | ", end=' ')  # rows are now horizontal with end=
        for cell in row:
            #cell = "_"
            players_symbols = cell if cell is not None else "_"
            """
            players_symbols = None
            if cell is None:
                players_symbols = " _ "
            else:
                players_symbols = cell
                """
            print(players_symbols, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board: ")
    print()


def find_winner(board):
    sequences = get_winning_sequence(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True
        # if not symbol1:
        #     continue
        # for cell in row:
        #     if cell != symbol1:
        #         continue
        #
        # return True

    return False


def get_winning_sequence(board):
    sequences = []
    # win by rows
    rows = board
    sequences.extend(rows)
    # win by columns
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
        ]
        sequences.append(col)

        # win by diagonals
        diagonals = [
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]
        sequences.extend(diagonals)

    return sequences


"""board = {
       'col_1': [1,2,3],
       'col_2': [4,5,6],
       'col_3': [7,8,9]
    }
"""

"""board = [
      ['cell1','cell2','cell3' ]
      ['r2_c1','r2_c2','r2_c3' ]
      ['r3_c1','r3_c2,','r3_c3' ]
  ]
"""

if __name__ == '__main__':
    main()
