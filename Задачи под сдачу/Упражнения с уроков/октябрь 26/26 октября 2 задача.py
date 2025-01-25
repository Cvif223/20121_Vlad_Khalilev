a = [1, 2, 3]
def permutations(lst):
    if len(lst) == 0:
        return [[]]

    result = []
    for i in range(len(lst)):
        # берём элемент по порядку
        current = lst[i]
        others = lst[:i] + lst[i + 1:]
        for p in permutations(others):
            result.append([current] + p)
    return result
b = [tuple(x) for x in permutations(a)]
print(set(b))