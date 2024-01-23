from enum import Enum

ROWS, COLS = (3, 3)


class PlayerTurn(Enum):
    X = 1
    O = 2


class YesOrNo(Enum):
    YES = 1
    NO = 2


def parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def print_board_game(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if col < 2:
                print(f'{board[row][col]} | ', end='')
            elif col == 2:
                print(f'{board[row][col]}', end='')
        print('')
        if row < 2:
            print('- - - - -')


def switch_player(player_num):
    if player_num == 1:
        return 2
    else:
        return 1


def validate_user_input(board, player_turn):
    while True:
        print(f'Player {player_turn} turn:')

        while True:
            row = input('Enter row number between 0 and 2: ')
            parsed_row = parse_int(row)

            if parsed_row is None:
                print('Invalid Input!')
            elif parsed_row > 2 or parsed_row < 0:
                print('Please enter a number between 0 and 2')
                print('Cell already occupied!')
            else:
                break

        while True:
            col = input('Enter column number between 0 and 2: ')
            parsed_col = parse_int(col)

            if parsed_col is None:
                print('Invalid Input!')
            elif parsed_col > 2 or parsed_col < 0:
                print('Please enter a number between 0 and 2')
            else:
                break

        if board[parsed_row][parsed_col] != ' ':
            print('Cell already occupied!')
        elif player_turn == 1:
            board[parsed_row][parsed_col] = PlayerTurn(1).name
            break
        else:
            board[parsed_row][parsed_col] = PlayerTurn(2).name
            break

    return board[parsed_row][parsed_col]


def check_winner(board, player):
    if board[0][0] == PlayerTurn(1).name and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        print(f'Player {player} has won!')
        return True
    elif board[0][0] == PlayerTurn(2).name and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        print(f'Player {player} has won!')
        return True
    elif board[0][1] == PlayerTurn(1).name and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        print(f'Player {player} has won!')
        return True
    elif board[0][1] == PlayerTurn(2).name and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        print(f'Player {player} has won!')
        return True
    elif board[0][2] == PlayerTurn(1).name and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        print(f'Player {player} has won!')
        return True
    elif board[0][2] == PlayerTurn(2).name and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        print(f'Player {player} has won!')
        return True
    elif board[0][0] == PlayerTurn(1).name and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        print(f'Player {player} has won!')
        return True
    elif board[0][0] == PlayerTurn(2).name and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        print(f'Player {player} has won!')
        return True
    elif board[1][0] == PlayerTurn(1).name and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        print(f'Player {player} has won!')
        return True
    elif board[1][0] == PlayerTurn(2).name and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        print(f'Player {player} has won!')
        return True
    elif board[2][0] == PlayerTurn(1).name and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        print(f'Player {player} has won!')
        return True
    elif board[2][0] == PlayerTurn(2).name and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        print(f'Player {player} has won!')
        return True
    elif board[0][0] == PlayerTurn(1).name and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print(f'Player {player} has won!')
        return True
    elif board[0][0] == PlayerTurn(2).name and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print(f'Player {player} has won!')
        return True
    elif board[0][2] == PlayerTurn(1).name and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print(f'Player {player} has won!')
        return True
    elif board[0][2] == PlayerTurn(2).name and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print(f'Player {player} has won!')
        return True


def start_game():
    game_board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    player = 1
    count_turn = 0

    print_board_game(game_board)
    print()

    while True:
        validate_user_input(game_board, player)
        print()
        print_board_game(game_board)
        print()
        win = check_winner(game_board, player)
        count_turn += 1
        if win:
            break
        elif count_turn == 9:
            print('It is a draw!')
            break
        player = switch_player(player)


def continue_game():
    while True:
        option = input('Do you want to continue playing? Type YES or NO: ').upper().strip()

        if option.isalpha():
            if option == YesOrNo(1).name:
                start_game()
            elif option == YesOrNo(2).name:
                return print('Thanks for playing!')
            else:
                print('Please choose between YES or NO: ')
        else:
            print('Invalid Option!')


def main():
    start_game()
    continue_game()


if __name__ == '__main__':
    main()
