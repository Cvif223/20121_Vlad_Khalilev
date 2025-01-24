import numpy as np

def read_input(file_path):
    with open(file_path, 'r') as file:
        N, L, K = map(int, file.readline().strip().split()) # где L - количество фигур, которые ещё предстоит разместить
        #print(file.readline().strip().split())
        existing_positions = [tuple(map(int, file.readline().strip().split())) for _ in range(K)]
        print(existing_positions)
    return N, L, existing_positions
N, L, e = read_input("input.txt")


def create_brd(n):
    # Создаем шахматное поле
    brd = np.zeros((n, n), dtype=int)
    return brd
chessboard = create_brd(N)


def position_fgrs(field, coordinates):
    #Позиционирует фигуру(ы) на шахматной доске
    for x, y in coordinates:
        if 0 <= x < field.shape[0] and 0 <= y < field.shape[1]:
            field[x, y] = 8  # Устанавливаем фигуру
        else:
            print(f"Координаты ({x}, {y}) выходят за пределы доски.")
    return chessboard
placed_figures = position_fgrs(chessboard, e)

def position_trgts(field, coordinates, need_moves=False):
    #Позиционирует ходы на шахматной доске
    for x, y in coordinates:
        if 0 <= x < field.shape[0] and 0 <= y < field.shape[1]:
            field[x, y] = 1  # Устанавливаем фигуру
        else:
            print(f"Координаты ({x}, {y}) выходят за пределы доски.")
    if need_moves:
        return chessboard, coordinates
    return chessboard

def move_piece(chessboard, placed_fgr, need_moves=False):
    #Выполняет ходы для фигур на шахматной доске
    moves = []

    for x, y in placed_fgr:
        # Диагональные ходы
        diagonal_moves = [(x + 1, y + 1), (x + 2, y + 2), (x + 1, y - 1), (x + 2, y - 2), (x - 1, y + 1), (x - 2, y + 2), (x - 1, y - 1), (x - 2, y - 2)]
        # Вертикальные ходы
        vertical_moves = [(x + 3, y), (x - 3, y)]
        # Горизонтальные ходы
        horizontal_moves = [(x, y + 3), (x, y - 3)]

        all_moves = diagonal_moves + vertical_moves + horizontal_moves

        # Проверка допустимости ходов
        for new_x, new_y in all_moves:
            if 0 <= new_x < chessboard.shape[0] and 0 <= new_y < chessboard.shape[1] and chessboard[new_x, new_y] == 0:
                moves.append((new_x, new_y))
    if need_moves:
        return position_trgts(placed_figures, moves, need_moves=True)
    return position_trgts(placed_figures, moves)
new_board = move_piece(chessboard, e)
"""
На данном этапе имеем доску с единицами там куда уже точно не сможем поставить ни одну фигуру,
ведь она будет находиться либо под боем имеющейся, либо на размещённой фигуре
"""
print(new_board)


def is_safe(chessboard, x, y):
    # Проверка на занятость клетки
    if chessboard[x, y] in [1, 8]:
        return False  # Клетка занята

    # Проверка на атаку других фигур (8)
    directions = [
        (1, 1), (2, 2), (1, -1), (2, -2), (-1, 1), (-2, 2), (-1, -1), (-2, -2),
        (3, 0), (-3, 0),
        (0, 3), (0, -3)
    ]

    for dx, dy in directions:
        nx, ny = x, y
        while 0 <= nx < chessboard.shape[0] and 0 <= ny < chessboard.shape[1]:
            nx += dx
            ny += dy
            if 0 <= nx < chessboard.shape[0] and 0 <= ny < chessboard.shape[1]:
                if chessboard[nx, ny] == 8:  # Если находим фигуру 8, то клетка под атакой
                    return False

    return True  # Клетка безопасна для размещения новой фигуры

file = open("output.txt", mode="w")
def place_figures(chessboard, L, current_solution=[]):
    if L == 0:
        # Если все фигуры размещены, сохраняем решение
        file.write(f"{current_solution}\n")
        return

    # Перебираем все возможные позиции на доске
    for x in range(chessboard.shape[0]):
        for y in range(chessboard.shape[1]):
            if is_safe(chessboard, x, y):
                # Если позиция безопасна, размещаем фигуру
                chessboard[x, y] = 8  # Устанавливаем фигуру
                current_solution.append((x, y))  # Запоминаем позицию

                # Получаем возможные ходы для размещенной фигуры
                possible_moves, save_to_del = move_piece(chessboard, current_solution, need_moves=True)
                # Рекурсивно пытаемся разместить оставшиеся фигуры
                place_figures(chessboard, L - 1, current_solution)

                # Убираем фигуру и откатываемся
                chessboard[x, y] = 0
                current_solution.pop()
                for x1, y1 in save_to_del:
                    chessboard[x1, y1] = 0

# Запуск размещения фигур
place_figures(chessboard, L)
file.close()
