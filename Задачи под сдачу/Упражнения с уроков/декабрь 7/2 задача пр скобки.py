def add_new_bkt(n, s="", opened=0, closed=0, ln=0):
    if opened < closed or n * 2 < ln or opened > n:
        return 0
    if ln == 2 * n:
        print(s)
        return 1
    return add_new_bkt(n, s + "(", opened + 1, closed, ln + 1) + add_new_bkt(n, s + ")", opened, closed + 1, ln + 1)
print(add_new_bkt(3))