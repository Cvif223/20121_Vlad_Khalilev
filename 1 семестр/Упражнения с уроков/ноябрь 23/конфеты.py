from functools import lru_cache
@lru_cache(maxsize=None)

def Stirling_number(n, k, is_first = True):
    if is_first:
        if k > n:
            return "no solution"
        for K in range(k):
            for N in range(n):
                Stirling_number(N, K)
    if k == 0:
        if n > 0:
            return 0
        if n == 0:
            return 1
    if k > n:
        return 0
    return k * Stirling_number(n - 1, k, is_first=False) + Stirling_number(n - 1, k - 1, is_first=False)

print(Stirling_number(4, 3))
print(Stirling_number(3, 2))
print(Stirling_number(4, 7))
print(Stirling_number(6, 6))
print(Stirling_number(15, 9))