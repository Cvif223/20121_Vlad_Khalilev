from typing import Union

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.my_bag = list()
        self.total_weight = 0

    def add_thing(self, thing):
        if thing.weight + self.total_weight > self.max_weight:
            raise ValueError("превышен суммарный вес предметов")
        self.total_weight = self.total_weight + thing.weight
        self.my_bag.append(thing)

    def __getitem__(self, item):
        if item > len(self.my_bag) - 1:
            raise IndexError("Неверный индекс")
        return self.my_bag[item]

    def __setitem__(self, key, value):
        if key > len(self.my_bag) - 1:
            raise IndexError("Неверный индекс")
        if self.total_weight - self.my_bag[key].weight + value.weight > self.max_weight:
            raise ValueError("Неверное")
        self.total_weight = self.total_weight - self.my_bag[key].weight + value.weight
        self.my_bag[key] = value

    def __delitem__(self, key):
        if key > len(self.my_bag) - 1:
            raise IndexError("Неверный индекс")
        del self.my_bag[key]


class Thing:
    def __init__(self, name: str, weight: Union[int, float]):
        self.name = name
        self.weight = weight


if __name__ == "__main__":
    b = Bag(700)
    b.add_thing(Thing('книга', 100))
    b.add_thing(Thing('носки', 200))
    try:
        b.add_thing(Thing('рубашка', 500))
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"
    assert b[0].name == 'книга' and b[
        0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"
    t = Thing('Python', 20)
    b[1] = t
    assert b[1].name == 'Python' and b[
        1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"
    del b[0]
    assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"
    try:
        t = b[2]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    b = Bag(700)
    b.add_thing(Thing('книга', 100))
    b.add_thing(Thing('носки', 200))
    b[0] = Thing('рубашка', 500)
    try:
        b[0] = Thing('рубашка', 700)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
