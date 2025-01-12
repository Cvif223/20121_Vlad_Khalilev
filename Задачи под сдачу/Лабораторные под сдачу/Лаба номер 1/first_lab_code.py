f = open("Input").readline()
a = [int(x) for x in f.split(" ")]
Xs = a[1:-1]
N = a[0]
S = a[-1]
#print(Xs, N, S, sep="\n")
def recursion_comb(index = 1, final = f"{Xs[0]}", summ_for_now = Xs[0]):
    if index == N:
        if summ_for_now == S:
            return final
        return None

    s1 = recursion_comb(index + 1, final + " + " + str(Xs[index]), summ_for_now + Xs[index])
    if s1 is not None:
        #print(final, "1")
        return s1

    s2 = recursion_comb(index + 1, final + " - " + str(Xs[index]), summ_for_now - Xs[index])
    if s2 is not None:
        #print(final, "2")
        return s2
print(recursion_comb())