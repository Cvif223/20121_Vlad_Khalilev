s, num = "ХалилевВладислав", 5
end = ""
for i in range(0, len(s), num + num - 2):#представляем в удобном виде (условно переворачиваем зигзаг набок)
    c = 0
    if c < num:
        t = ""
        try:
            for j in range(i, i + num):
                t = s[j] + t
        except:
            end = end + " " + t
            break
    end = " " + end + " " + t + ' '
    try:
        for k in range(num - 2):
            end = end + s[j + k + 1]
    except: continue
end = [x for x in list(end.split(" ")) if x != ""]

end_end = ''
chet = 0
for i in range(len(end)):#добиваем пробелами по чётности и нечётности
    chet += 1
    if chet % 2 == 0:
        end[i] = " " + end[i] + " "
    if chet % 2 != 0 and i == len(end) - 1:
        end[i] = " " * (num - len(end[i])) + end[i]
print(end)

for i in range(num):#выводим на экран
    for j in range(len(end)):
        if end[j][num - i - 1] != " ":
            end_end += end[j][num - i - 1]
print(end_end)
"""print(end_end.join(""))"""
"""for i in range(num):
    if i == 0 or i == num - 1:
        chetni = 0
        for j in range(len(end)):
            chetni += 1
            if chetni % 2 != 0:
                try:end_end += end[j][num - i - 1]
                except:continue
    else:
        chetni = 0
        for j in range(len(end)):
            chetni += 1
            if chetni % 2 != 0:
                try:end_end += end[j][num - i - 1]
                except:continue
            else:
                try:end_end += end[j][num - i - 3]
                except:continue
"""





"""for x in end.split(" "):
    if len(x) !=  num:

        print(" " + x)
    else: print(x)"""