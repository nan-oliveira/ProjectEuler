def tn(n):
    return n * (n + 1) / 2

def pn(n):
    return n * (3*n - 1) / 2

def hn(n):
    return n * (2*n - 1)

list_t = [tn(a) for a in range(2, 1_000_00)]
list_p = [pn(a) for a in range(2, 1_000_00)]
list_h = [hn(a) for a in range(2, 1_000_00)]

intersecao = list(set(list_t) & set(list_p) & set(list_h))
print(intersecao)