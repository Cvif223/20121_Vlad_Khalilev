
#qtable
#qgraphicsviev - для отрисовки доски
#qgraphicsitem - для отрисовки клетки
#qthread
#qwidget
#.movethread для того чтобы signalslot отработал
#qconcurent +
#qrunable
file_out = open("output.txt", "a")
class Figure:
    pass

class Cell:
    def __init__(self):
        self._is_free: bool = True
        self._is_under_attack: bool = False

    @property
    def is_free(self):
        return self._is_free

    @is_free.setter
    def is_free(self, value):
        if not isinstance(value, bool):
            raise ValueError("Значение должно быть типа bool")
        self._is_free = value

    @property
    def is_under_attack(self):
        return self._is_under_attack

    @is_under_attack.setter
    def is_under_attack(self, value):
        if not isinstance(value, bool):
            raise ValueError("Значение должно быть типа bool")
        self._is_under_attack = value

    def __repr__(self):
        if not self._is_free:
            return "*"  # Фигура
        if self._is_under_attack:
            return "!"  # Клетка под атакой
        return "0"      # Свободная клетка

    def __str__(self):
        return self.__repr__()

class Board:
    def __init__(self, N: int):
        self._board: list[list[Cell]] = [[Cell() for _ in range(N)] for _ in range(N)]
        self.N = N

    @property
    def board(self):
        return self._board

    def __getitem__(self, key):
        x, y = key
        if 0 <= x < self.N and 0 <= y < self.N:
            return self._board[x][y]
        else:
            raise IndexError("Координаты выходят за границы доски")

    def __setitem__(self, key, value):
        x, y = key
        if 0 <= x < self.N and 0 <= y < self.N:
            self._board[x][y].is_free = False
        else:
            raise IndexError("Координаты выходят за границы доски")

    def __repr__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self._board)

class Game:
    def __init__(self, board: Board, L, e):
        self._board = board
        self._N = board.N
        self._L = L
        self._e = e
        self._Total_number_of_solutions = 0


    def _attacked_figures(self, x, y, cords_param = False):
        positions = set()
        turns = [(x + 1, y + 1), (x + 2, y + 2), (x + 1, y - 1),
                 (x + 2, y - 2), (x - 1, y + 1), (x - 2, y + 2),
                 (x - 1, y - 1), (x - 2, y - 2), (x + 3, y),
                 (x - 3, y), (x, y + 3), (x, y - 3)]
        for n, m in turns:
            if 0 <= n < self._board.N and 0 <= m < self._board.N and self._board[n, m].is_free == True and self._board[n, m].is_under_attack == False:
                positions.add((n, m))
                self._board[n, m].is_under_attack = True
        if cords_param == True:
            return positions



    def start(self):
        for x, y in self._e:
            if 0 <= x < self._board.N and 0 <= y < self._board.N:
                self._board[x, y].is_free = False  # Устанавливаем фигуру
                self._attacked_figures(x, y)
            else:
                print(f"Координаты ({x}, {y}) выходят за пределы доски.")
        self.place_figures(self._L)


    def place_figures(self, l, current_solution=[], positions_now={0: (0, 0)}):
        """
        :param l: Сколько ещё фигур надо ставить
        :param current_solution: Текущие размещённые фигуры
        :param positions_now: Позиции поставленных фигур
        """
        if l == 0:
            # Если все фигуры размещены, сохраняем решение
            self._Total_number_of_solutions += 1
            tmp = f"{(current_solution + self._e)}"
            file_out.write(f"{tmp.replace('),', ')')[1: -1]}\n")
            return

        # Перебираем все возможные позиции на доске
        for x in range(positions_now[self._L - l][0], self._N):
            start_y = positions_now[self._L - l][1] if x == positions_now[self._L - l][0] else 0
            for y in range(start_y, self._N):
                if self._board[x, y].is_free and not self._board[x, y].is_under_attack:
                    # Размещаем фигуру
                    positions_now[self._L - l + 1] = (x, y)
                    self._board[x, y].is_free = False
                    current_solution.append((x, y))
                    cords = self._attacked_figures(x, y, cords_param=True)

                    # Рекурсивно размещаем оставшиеся фигуры
                    self.place_figures(l - 1, current_solution, positions_now)

                    # Откатываем изменения
                    self._board[x, y].is_free = True
                    current_solution.pop()

                    # Восстанавливаем состояние атакованных клеток
                    for x2, y2 in cords:
                        self._board[x2, y2].is_under_attack = False


if __name__ == "__main__":
    import time
    start = time.perf_counter()

    # Тестируемый код

    file = open("input.txt", 'r')
    file_out = open("output.txt", "w")
    N, L, K = map(int, file.readline().strip().split())
    existing_positions = [tuple(map(int, file.readline().strip().split())) for _ in range(K)]
    print(N, L, K, existing_positions)
    print()

    b = Board(N)
    game = Game(b, L, existing_positions)
    game.start()
    print(game._Total_number_of_solutions)



    result = sum(i * i for i in range(1000000))
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.6f} секунд")
    #7.621688 секунд
    #pyside6-uic ui_main.ui -o ui_main.py
