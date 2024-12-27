s = {1, 2, 3}
s2 = {2, 3, 4}
s.difference_update(s2)
print(s)
s.symmetric_difference(s2)

print(hash(2222222222222222222222222222222222))
print(hash(1146726781610422613))
s = {'2', 1146726781610422613}
print(s)
print(hash("2"))
"""
union | - объединение
intersection & - пересечение
difference "-" - разность
symmetric_difference ^ - строгая разность - совпадения выкидываются
с update операторы печатаются со знаком =
=|
=&
=-
"""

s = {x for x in range(10)}
print(s)
s.discard(2)
print(s)
myset = frozenset(s)
print(myset)
s = frozenset()
y = (x for x in range(15))
y = tuple(y)
print(y)
y = str(y)
print(y)