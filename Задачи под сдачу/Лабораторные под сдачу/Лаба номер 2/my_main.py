import numpy as np

def read_input(file_path):
    with open(file_path, 'r') as file:
        N, L, K = map(int, file.readline().strip().split()) # где L - количество фигур, которые ещё предстоит разместить
        #print(file.readline().strip().split())
        existing_positions = [tuple(map(int, file.readline().strip().split())) for _ in range(K)]
        #print(existing_positions)
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


    return True  # Клетка безопасна для размещения новой фигуры
file = open("output.txt", mode="w")
Total_number_of_solutions = 0
def place_figures(chessboard, l, current_solution=[], positions_now = {0: (0, 0)}):
    """
    :param chessboard: Доска
    :param l: С этим параметром я определяю сколько ещё фигур надо ставить и какая сейчас фигура по счёту
    :param positions_now: Сохранил сюда позиции поставленных фигур и их нумерацию (ключём). позиция, которая там уже указана, это для передвижения самой первой фигуры.
    """

    if l == 0:
        # Если все фигуры размещены, сохраняем решение
        global Total_number_of_solutions
        Total_number_of_solutions += 1
        file.write(f"{current_solution + e}\n")
        #print(chessboard)
        return
    # Перебираем все возможные позиции на доске
    for x in range(positions_now[L - l][0], N):
        for y in range(positions_now[L - l][1] if x == positions_now[L - l][0] else 0, N): # Иду дальше от самой последней поставленной (если на ряду с ней, то правее, ниже- с нуля)
            if is_safe(chessboard, x, y):
                # Если позиция безопасна, размещаем фигуру
                positions_now[L - l + 1] = (x, y)
                chessboard[x, y] = 8  # Устанавливаем фигуру
                current_solution.append((x, y))  # Запоминаем позицию

                # Получаем возможные ходы для размещенной фигуры
                possible_moves, save_to_del = move_piece(chessboard, current_solution, need_moves=True)
                # Рекурсивно пытаемся разместить оставшиеся фигуры
                place_figures(chessboard, l - 1, current_solution)

                # Убираем фигуру и откатываемся
                chessboard[x, y] = 0
                current_solution.pop()
                for x1, y1 in save_to_del:
                    chessboard[x1, y1] = 0

# Запуск размещения фигур
place_figures(chessboard, L)
file.close()
print(Total_number_of_solutions)