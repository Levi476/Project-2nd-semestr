# Создание пустого игрового поля
board = [' ' for _ in range(9)]

# Функция для отображения игрового поля
def draw_board():
    print('---------')
    for i in range(3):
        print(f'| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |')
        print('---------')

# Функция для хода игрока
def make_move(player):
    valid_input = False
    while not valid_input:
        move = input(f"Ход игрока {player} (введите число от 1 до 9): ")
        try:
            move = int(move)
            if move >= 1 and move <= 9 and board[move-1] == ' ':
                valid_input = True
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ход. Попробуйте еще раз.")
    board[move-1] = player

# Функция для проверки победителя
def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Победа в рядах
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Победа в столбцах
        [0, 4, 8], [2, 4, 6]  # Победа по диагоналям
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Основной игровой цикл
current_player = 'X'
draw_board()

while True:
    make_move(current_player)
    draw_board()
    if check_winner(current_player):
        print(f"Игрок {current_player} победил!")
        break
    elif ' ' not in board:
        print("Ничья!")
        break
    current_player = 'O' if current_player == 'X' else 'X'