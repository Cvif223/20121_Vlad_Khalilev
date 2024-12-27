list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]

def return_elements(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    first = set1 & set2
    second = set1 ^ set2
    third = set1 - set2
    quadro = set2 - set1
    return (f"{len(first)} элемента: {', '.join(map(str, first))}\n"
            f"{len(second)} элемента: {', '.join(map(str, second))}\n"
            f"{len(third)} элемента: {', '.join(map(str, third))}\n"
            f"{len(quadro)} элемента: {', '.join(map(str, quadro))}\n"
            )
print(return_elements(list1, list2))