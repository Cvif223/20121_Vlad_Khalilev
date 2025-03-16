d = {"I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000
     }

def func(str):
    new_str = []
    for i, vol in enumerate(str):

        if i != 0 and d.get(str[i - 1]) < d.get(vol):
            new_str.pop(-1)
            new_str.append(d.get(vol) - d.get(str[i - 1]))
        else:
            new_str.append(d.get(vol))
    print(sum(new_str))
func("IM")



"""if i != 0 and i != 1 and d.get(str[i - 1]) < d.get(vol) and d.get(str[i - 2]) < d.get(vol):
            new_str.pop(-1)
            new_str.pop(-1)
            new_str.append(d.get(vol) - (d.get(str[i - 1]) + d.get(str[i - 2])))"""