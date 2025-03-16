n = 3
m = 3
quest = [[0] * n for x in range(m)]
#for i in quest:
    #print(i)


dictt = {}
def go(OX = 0, OY = 0, cache = None):

    if cache is None:
        cache = {}

    if OX == n-1 and OY == m-1:
        return 1
    if OX >=n or OY >= m:
        return 0

    key = (OX,OY)

    if key in cache:
        return cache[key]

    cache[key] = go(OX + 1, OY,cache) + go(OX, OY + 1,cache)
    print(cache)
    return cache[key]

print(go(0, 0))
