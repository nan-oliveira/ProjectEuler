import numpy as np

count = 0
mult = []
for i in range(1, 1_000_000):
    aux = str(i)
    for j in aux:
        count += 1
        if count in [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]:
            print(count, j)
            mult.append(int(j))
        if count == 1_000_000:
            break

print(np.prod(mult))