p = int(input("Введите любое число:"))
p1 = p
p2 = 0
while p != 0:
    k = (p % 10)
    p = p // 10
    p2 = p2 * 10 + k
if p1 == p2:
    print("True")

