import random
class Cell:

    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value == 0:
            return True
        return False


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = ((Cell(), Cell(), Cell()),
                     (Cell(), Cell(), Cell()),
                     (Cell(), Cell(), Cell()))

    def init(self):
        self.pole = ((Cell(), Cell(), Cell()),
                     (Cell(), Cell(), Cell()),
                     (Cell(), Cell(), Cell()))

    def show(self):
        print(f"{self.pole[0][0].value} {self.pole[0][1].value} {self.pole[0][2].value} \n{self.pole[1][0].value} {self.pole[1][1].value} {self.pole[1][2].value} \n{self.pole[2][0].value} {self.pole[2][1].value} {self.pole[2][2].value}")

    def __getitem__(self, lst):
        if lst[0] not in [0, 1, 2] or lst[1] not in [0, 1, 2]:
            raise IndexError("некорректно указанны индексы")
        return self.pole[lst[0]][lst[1]].value

    def __setitem__(self, key, value):
        if key[0] not in [0, 1, 2] or key[1] not in [0, 1, 2]:
            raise IndexError("некорректно указанны индексы")
        self.pole[key[0]][key[1]].value = value

    def human_go(self):
        #наверное предполагается пользовательский ввод???
        x, y = input("Напишите координаты клетки, в которую хотите сделать ход в формате 'x y'")
        if bool(self.pole[x][y]):
            self.pole[x][y].value = self.HUMAN_X
        else:print("клетка занята")

    def computer_go(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if bool(self.pole[x][y]):
            self.pole[x][y].value = self.HUMAN_X
        else:
            self.computer_go()

    def __bool__(self):
        for x in range(0, 2):
            for y in range(0, 2):
                if self.pole[x][y].value == 0:
                    return True
        return False

    def is_human_win(self):
        if self.pole[0][0].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[2][2].value == self.HUMAN_X:
            return True
        if self.pole[0][2].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[2][0].value == self.HUMAN_X:
            return True
        if self.pole[0][0].value == self.HUMAN_X and self.pole[0][1].value == self.HUMAN_X and self.pole[0][2].value == self.HUMAN_X:
            return True
        if self.pole[1][0].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[1][2].value == self.HUMAN_X:
            return True
        if self.pole[2][0].value == self.HUMAN_X and self.pole[2][1].value == self.HUMAN_X and self.pole[2][2].value == self.HUMAN_X:
            return True
        if self.pole[0][0].value == self.HUMAN_X and self.pole[1][0].value == self.HUMAN_X and self.pole[2][0].value == self.HUMAN_X:
            return True
        if self.pole[0][1].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[2][1].value == self.HUMAN_X:
            return True
        if self.pole[0][2].value == self.HUMAN_X and self.pole[1][2].value == self.HUMAN_X and self.pole[2][2].value == self.HUMAN_X:
            return True
        return False

    def is_computer_win(self):
        if self.pole[0][0].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[2][2].value == self.COMPUTER_O:
            return True
        if self.pole[0][2].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[2][0].value == self.COMPUTER_O:
            return True
        if self.pole[0][0].value == self.COMPUTER_O and self.pole[0][1].value == self.COMPUTER_O and self.pole[0][2].value == self.COMPUTER_O:
            return True
        if self.pole[1][0].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[1][2].value == self.COMPUTER_O:
            return True
        if self.pole[2][0].value == self.COMPUTER_O and self.pole[2][1].value == self.COMPUTER_O and self.pole[2][2].value == self.COMPUTER_O:
            return True
        if self.pole[0][0].value == self.COMPUTER_O and self.pole[1][0].value == self.COMPUTER_O and self.pole[2][0].value == self.COMPUTER_O:
            return True
        if self.pole[0][1].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[2][1].value == self.COMPUTER_O:
            return True
        if self.pole[0][2].value == self.COMPUTER_O and self.pole[1][2].value == self.COMPUTER_O and self.pole[2][2].value == self.COMPUTER_O:
            return True
        return False

    def is_draw(self):
        if self.is_computer_win() or self.is_human_win():
            return False
        if not self.__bool__():
            return True
        return False





cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"
assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"
game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"
try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
game.init()
game.show()
assert game.is_human_win() == False and game.is_computer_win() == False and game.is_draw() == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win() and game.is_computer_win() == False and game.is_draw() == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win() == False and game.is_computer_win() and game.is_draw() == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"