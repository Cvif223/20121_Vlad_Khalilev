a = int(input("Число: "))
b = 0
flag = False
if a < 0:
    flag = True
a = abs(a)
while a != 0:
    k = a % 10
    a //= 10
    b = (b * 10) + k
if flag:
    b = -b
if -2**7 <= b <= 2**7 - 1:
    print(b)
else:
    print("no solution")-123
