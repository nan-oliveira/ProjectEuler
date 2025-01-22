from math import comb

count = 0
for n in range(1, 100 + 1):
    for r in range(1, n+1):
        if comb(n, r) > 10 ** 6:
            count += 1
print(count)