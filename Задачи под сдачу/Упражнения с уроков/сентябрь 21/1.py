"""f = str(input("Введите строку: "))"""
f = "qweasdfdqw"
l = 0
t = False
st_global = ""
st_last = ""
for r in range(len(f)):
    st_new = st_last + f[r]
    if f[r] in st_last:
        t = True
    while t:
        if f[l] == f[r]:
            t = False
        st_new = st_new[1:]
        l += 1
    if len(st_new) > len(st_global):
        st_global = st_new
    st_last = st_new
print(st_global)