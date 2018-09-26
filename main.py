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