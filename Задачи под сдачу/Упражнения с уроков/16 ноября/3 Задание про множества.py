nums = [1, 2, 3, 4]
def perm(st):
    global_list = list(set(st.copy()))
    mn = dict()
    for i in range(len(global_list)):
        tmp = global_list.copy()
        tmp.pop(i)
        mn.setdefault(len(st) - 1, []).append({*tmp})
    while list(mn.keys())[-1] > 1:
        i = list(mn.values())[-1]
        def many_mn(lst):
            for i, v in enumerate(lst):
                for j in lst[i + 1:]:
                    mn.setdefault(len(v & j), []).append(v & j)
        many_mn(i)
    final = set()
    final.add(tuple(global_list))
    for i in mn.values():
        for j in i:
            if j != set():
                final.add(tuple(j))
    return (sorted(final))
a = (perm(nums))
b = []
for i in a:
    b.append([*i])
print(b)
print(len(b))