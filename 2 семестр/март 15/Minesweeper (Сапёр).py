import numpy as np
import random


class GamePole:
    _single = None
    def __init__(self, N, M, total_mines):
        self.N: int = N
        self.M: int = M
        self.total_mines: int = total_mines
        # в идеале нужны кортежи а не списки
        self.__pole_cells = tuple(tuple(Cell() for _ in range(N)) for _ in range(M))

    #надо разобраться в new
    def __new__(cls, *args, **kwargs):
        if cls._single == None:
            cls._single = super().__new__(cls)
        return cls._single

    @property
    def pole(self):
        return self.__pole_cells

    def show_pole(self):
        print(*self.__pole_cells, sep="\n")

    def place_bomb(self):
        n = random.randint(0, self.N - 1)
        m = random.randint(0, self.M - 1)
        if self.__pole_cells[m][n].is_mine == True:
            self.place_bomb()
        else:
            self.__pole_cells[m][n].is_mine = True

    def init_pole(self):
        for _ in range(self.total_mines):
            self.place_bomb()
        for i in range(self.M):
            for j in range(self.N):
                if self.__pole_cells[i][j].is_mine == True:
                    continue
                else:
                    counter = 0
                    if i >= 1 and self.__pole_cells[i - 1][j].is_mine == True:
                        counter += 1
                    if i >= 1 and j >= 1 and self.__pole_cells[i - 1][j - 1].is_mine == True:
                        counter += 1
                    if j >= 1 and self.__pole_cells[i][j - 1].is_mine == True:
                        counter += 1
                    if j >= 1 and i <= self.M - 2 and self.__pole_cells[i + 1][j - 1].is_mine == True:
                        counter += 1
                    if i <= self.M - 2  and self.__pole_cells[i + 1][j].is_mine == True:
                        counter += 1
                    if i <= self.M - 2 and j <= self.N - 2 and self.__pole_cells[i + 1][j + 1].is_mine == True:
                        counter += 1
                    if j <= self.N - 2 and self.__pole_cells[i][j + 1].is_mine == True:
                        counter += 1
                    if j <= self.N - 2 and i >= 1 and self.__pole_cells[i - 1][j + 1].is_mine == True:
                        counter += 1
                    self.__pole_cells[i][j].number = counter

    def open_cell(self, i, j):
        if i < self.N and i >= 0 and j < self.M and j >= 0:
            return True
        raise IndexError('некорректные индекы i, j клетки игрового поля')

class Cell:
    def __init__(self):
        self.__is_mine: bool = False
        self.__number: int = 0
        self.__is_open: bool = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool):
        if type(value) != bool:
            raise ValueError("Недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: int):
        if type(value) != int or value > 8 or value < 0:
            raise ValueError("Недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool):
        if type(value) != bool:
            raise ValueError("Недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return True if self.__is_open == False else False

    def __repr__(self):
        return "*" if self.__is_mine else str(self.__number)

"""pole = GamePole(7, 5, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0, 1]:
    pole.open_cell(0, 1)
if pole.pole[3, 4]:
    pole.open_cell(3, 4)
#pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()"""

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1
cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"
cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"
try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
p.init_pole()
p.show_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1
assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)
try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 19 or jj < 0 or jj > 9: #я тут поменял местами 9 и 19, тк ii это строка, а jj- столбец
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"