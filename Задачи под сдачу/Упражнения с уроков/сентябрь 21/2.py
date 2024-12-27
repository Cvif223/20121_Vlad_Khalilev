"""f = input("Строка: ")"""
f = "It Was Cool"
final = ""
tmp = ""
for i in f:
    if i == " ":
        final = " " + tmp + final
        tmp = ""
    else:
        tmp += i
final = tmp + final
print(final.capitalize())