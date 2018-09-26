x = 'X'
o = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9


def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ('y', 'n'):
        response = int(input(question))
    return response


def ask_number(question, low, high):
    """Ask for number within a range"""
    response = None
    while response not in range(low, high)
        response = int(input(question))
    return response


def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no('Do you require the first move? (y/n): ')
    if go_first == 'y':
        print('\n Then take the first move. You will need it.')
        computer = o
        human = x
    else:
        print('\nYour bravery will be your undoing... I will go first.')
        computer = o
        human = x
    return computer, human


def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display game board on screen."""
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('t', '-----')
    print('\n\t', board[3], '|', board[4], '|', board[5])
    print('t', '-----')
    print('\n\t', board[6], '|', board[7], '|', board[8], '\n')
    print('t', '-----')


def legal_moves(board):
    """Create list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:

            moves.append(square)
            return moves



def winner(board):
    """Determine the winner of the game."""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
        return None


def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Where will you move? (0 - 8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('\nThat square is already occupied, foolish human, Choose andother.\n')
        print('Fine...')
        return move


def computer_move(board, computer, human):
    """Make computer move."""

    # make a copy to work with since function will be changing list.
    board = board[:]

    # the best moves to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print('I shall take square number',)

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print move
            return move
        # done checking this move so,