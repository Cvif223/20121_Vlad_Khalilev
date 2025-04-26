from abc import ABC, abstractmethod
from random import choice
from string import ascii_lowercase

def generate_random_name(len=5):
    name = ""
    for _ in range(len):
        name += choice(ascii_lowercase)
    return name

from collections import deque

def repack_boxes(*args: "Box"):
    c = len(args)
    step = 0
    my_objects = deque() #deque - очередь (быстрая вставка в начало и конец)
    for include_lst in args:
        my_objects.extendleft(include_lst.empty())

    while my_objects:
        args[step%c].add(my_objects.pop())
        step += 1





class Box(ABC):
    @abstractmethod
    def add(self, items):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass

class Item:
    def __init__(self, name, v):
        self.name = name
        self.value = v

    def __repr__(self):
        return f"{self.name}"



class ListBox(Box):
    def __init__(self):
        self.lst = list()

    def add(self, *args):
        for a in args:
            self.lst.append(a)

    def empty(self):
        tmp_list = self.lst.copy()
        self.lst.clear()
        return tmp_list

    def count(self):
        return len(self.lst)


    def __repr__(self):
        return f"{[x for x in self.lst]}"

class DictBox(Box):
    def __init__(self):
        self.dct = dict()

    def add(self, *args: Item):
        for a in args:
            self.dct.setdefault(a.name,[]).append(a)

    def empty(self):
        tmp_list = self.dct.values()
        self.dct = dict()
        
        """ tmp_list2 = [i for i in tmp_list]
        tmp_list3 = []
        for i in tmp_list2:
            for j in i:
                tmp_list3.append(j)"""
        return tmp_list3

    def count(self):
        return len(self.dct)

    def __repr__(self):
        return f"{[x for x in self.dct.keys()]}"



a = ListBox()
a.add(*[Item(generate_random_name(), x) for x in range(20)])



b = ListBox()
b.add(*[Item(generate_random_name(), x) for x in range(9)])


c = DictBox()
c.add(*[Item(generate_random_name(), x) for x in range(5)])


print(a)
print(b)
print(c)
print()
repack_boxes(a, b, c)
print(a)
print(b)
print(c)
