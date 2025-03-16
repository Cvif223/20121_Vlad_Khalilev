spis = [["name1 surname1", 12345],
        ["name2 surname2"],
        ["name3 surname3", 12354],
        ["name4 surname4", 12435]
        ]

def santa_users(list):
    d = dict()
    for i in list:
        def non(a, b=None):
            nonlocal d
            d[a] = b
        if len(i) == 2:
            non(i[0], i[1])
        else:
            non(i[0])
    return d

print(santa_users(spis))