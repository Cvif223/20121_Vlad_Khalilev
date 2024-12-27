street = [("sber",10),("Tin",5),("Vol",6),("Ker",12)]
for i, (k, v) in enumerate(street):
    street[i] = (v, k, i + 1)
algoritmo = [0, street[0][0]]
final_plan = [("none", 0), (street[0][1], street[0][2])]
flag = True
for i, (vol, bank, num_street) in enumerate(street[1:], 2):
    algoritmo.append(vol)
    if algoritmo[i-2] + algoritmo[i] < algoritmo[i-1]:
        algoritmo[i] = algoritmo[i-1]
        flag = True
        if final_plan[-2][1] - final_plan[-1][1] > 1:
            final_plan.append((street[i - 2][1], street[i - 2][2]))

    else:
        algoritmo[i] = algoritmo[i-2] + algoritmo[i]
        if num_street - final_plan[-1][1] > 1:
            final_plan.append((street[i - 1][1], street[i - 1][2]))
            flag = False
        else:

            if num_street - street[i - 2][2] > 0:
                final_plan.pop(-1)
                final_plan.append((bank, num_street))
final_plan.pop(0)
print(final_plan)