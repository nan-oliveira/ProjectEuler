count = 0
n = 1

while True:
    valid_count = sum(1 for x in range(1, 10) if 10**(n-1) <= x**n < 10**n)
    if valid_count == 0:
        break
    count += valid_count
    n += 1

print("Total count:", count)