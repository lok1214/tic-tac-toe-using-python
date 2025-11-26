board = [' ' for _ in range(10)]
board[0] = '#' 

def display_board(board):
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---|---|---')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('\n')

def place_marker(board, marker, position):
    board[position] = marker

def check_win(board, marker):
    return (
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        (board[7] == marker and board[5] == marker and board[3] == marker) or
        (board[9] == marker and board[5] == marker and board[1] == marker)
    )

def is_space_free(board, position):
    return board[position] == ' '

def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

def get_player_move(board):
    while True:
        try:
            position = int(input('Choose your next position (1-9): '))
            if position in range(1, 10) and is_space_free(board, position):
                return position
            else:
                print('That position is either out of range or already taken. Try again.')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')

def play_game():
    print('Welcome to Tic-Tac-Toe!')
    
    game_board = [' '] * 10
    game_board[0] = '#' 
    
    player1_marker = 'X'
    player2_marker = 'O'
    current_marker = player1_marker
    
    game_on = True

    while game_on:
        display_board(game_board)
        
        print(f"It is Player '{current_marker}'s turn.")
        
        position = get_player_move(game_board)
        place_marker(game_board, current_marker, position)
        
        if check_win(game_board, current_marker):
            display_board(game_board)
            print(f'Congratulations! Player "{current_marker}" has won the game!')
            game_on = False
        
        elif is_board_full(game_board):
            display_board(game_board)
            print('The game is a tie!')
            game_on = False
            
        else:
            current_marker = player2_marker if current_marker == player1_marker else player1_marker

if __name__ == "__main__":
    play_game()
