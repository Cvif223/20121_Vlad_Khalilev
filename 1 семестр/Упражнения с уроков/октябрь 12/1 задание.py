a = [4,-5,-7,12,-2,5]
C = -5
N = len(a)
a.sort()
m = [max(a) + 1]
for a1 in range(len(a) - 2):
    for a2 in range(a1 + 1, len(a) - 1):
        l = a2 + 1
        r = N - 1
        while r > l:
            if abs(a[a1]+a[a2]+a[l]+a[r] - C) < abs(sum(m) - C):
                m = [a[a1], a[a2], a[l], a[r]]
            if a[a1] + a[a2] + a[r] + a[l] > C:
                r -= 1
            else:
                l += 1
print(m)
print(sum(m))                                           #m = a[a1], a[a2], a[l], a[r]