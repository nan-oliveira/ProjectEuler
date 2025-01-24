def primeFactors(n):
    # Print the number of two's that divide n
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(n ** 0.5) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i== 0:
            factors.add(i)
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.add(n)
    return factors

for i in range(2, 1_000_000):
    num_1 = i
    num_2 = i + 1
    num_3 = i + 2
    num_4 = i + 3

    if len(primeFactors(num_1)) != 4:
        continue
    if len(primeFactors(num_2)) != 4:
        continue
    if len(primeFactors(num_3)) != 4:
        continue
    if len(primeFactors(num_4)) != 4:
        continue

    print(num_1)
    print(num_2)
    print(num_3)
    print(num_4)
    break