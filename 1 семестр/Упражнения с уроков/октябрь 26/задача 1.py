s = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
d1 = {}
for value in s:
    d1.setdefault(str(sorted(value)), []).append(value)
for j in d1.values():
    print(j)