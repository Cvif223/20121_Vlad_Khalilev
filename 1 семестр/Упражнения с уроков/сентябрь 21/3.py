f = "[[]{[()]}]()({})"
f_max = ""
for i in range(len(f) - 1):
    for j in range(i + 2, len(f) + 1):
        f_glob = f[i:j]
        tmp = f_glob
        while "{}" in tmp or "()" in tmp or "[]" in tmp:
            if "{}" in tmp:
                tmp = tmp.replace("{}", "", 1)
            if "()" in tmp:
                tmp = tmp.replace("()", "", 1)
            if "[]" in tmp:
                tmp = tmp.replace("[]", "", 1)
        if tmp == "":
            if len(f_max) < len(f_glob):
                f_max = f_glob
if f_max == "": print("False")
elif len(f_max) == len(f): print("True")
else: print(f_max)











"""print(f[i:j])
        if ruined:
            continue
        if "{]" not in f[i:j] and "{)" not in f[i:j] and "{]" not in f[i:j] and "[}" not in f[i:j] and "[)" not in f[i:j] and "(]" not in f[i:j] and "(}" not in f[i:j]:"""

#     Иной вариант max для строки 15
# f_max = max(f_max,f_glob, key=len)


"""
square = "[]"
round = "()"
figure = '{}'
"""